from typing import Dict, Generator, List, Union

from belvo.resources.base import Resource
from belvo.utils import clean_none_values


class Incomes(Resource):
    endpoint = "/api/incomes/"

    def create(
        self,
        link: str,
        *,
        token: str = None,
        encryption_key: str = None,
        save_data: bool = True,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Union[List[Dict], Dict]:

        data = {
            "link": link,
            "save_data": save_data,
            "token": token,
            "encryption_key": encryption_key,
        }

        return self.session.post(
            self.endpoint, data=clean_none_values(data), raise_exception=raise_exception, **kwargs
        )

    def list(self, **kwargs) -> Generator:
        raise NotImplementedError()

    def get(self, id: str, **kwargs) -> Dict:
        raise NotImplementedError()

    def delete(self, id: str) -> bool:
        raise NotImplementedError()

    def resume(
        self, session: str, token: str, *, link: str = None, raise_exception: bool = False, **kwargs
    ) -> Union[List[Dict], Dict]:
        raise NotImplementedError()
