from typing import Optional, List

import fastapi
from starlette.routing import Route


class Bot:
    def __init__(self):
        self._session: Optional[fastapi.FastAPI] = None

    @property
    def session(self) -> Optional[fastapi.FastAPI]:
        if self._session is None:
            self._session = fastapi.FastAPI()
        return self._session

    def set_routes(self, routes: List[Route]):
        if self._session:
            for route in routes:
                self._session.add_route(path=route.path,
                                        route=route.endpoint,
                                        methods=route.methods if route.methods else None,
                                        name=route.name if route.name else None,
                                        include_in_schema=route.include_in_schema
                                        )
