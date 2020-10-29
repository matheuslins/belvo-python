from typing import Dict

from belvo.base_resource import Resource


class Institutions(Resource):
    endpoint = "/api/institutions/"

    def delete(self, id: str) -> bool:
        raise NotImplementedError()

    def resume(
        self,
        session: str,
        token: str,
        *,
        link: str = None,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Dict:
        raise NotImplementedError()
