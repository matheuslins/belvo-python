from typing import Union, List, Dict

from belvo.base_resource import Resource


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

        data = {"link": link, "save_data": save_data}

        if token:
            data.update(token=token)
        if encryption_key:
            data.update(encryption_key=encryption_key)

        return self.session.post(
            self.endpoint, data=data, raise_exception=raise_exception, **kwargs
        )
