from typing import Dict, List, Union

from belvo.resources.base import Resource
from belvo.utils import clean_none_values


class Owners(Resource):
    endpoint = "/api/owners/"

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
