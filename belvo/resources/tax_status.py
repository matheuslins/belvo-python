from typing import Dict, List, Union

from belvo.resources.base import Resource
from belvo.utils import clean_none_values


class TaxStatus(Resource):
    endpoint = "/api/tax-status/"

    def create(
        self,
        link: str,
        *,
        attach_pdf: bool = False,
        encryption_key: str = None,
        save_data: bool = True,
        raise_exception: bool = False,
        **kwargs: Dict,
    ) -> Union[List[Dict], Dict]:

        data = {
            "link": link,
            "attach_pdf": attach_pdf,
            "save_data": save_data,
            "encryption_key": encryption_key,
        }

        return self.session.post(
            self.endpoint, data=clean_none_values(data), raise_exception=raise_exception, **kwargs
        )

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
