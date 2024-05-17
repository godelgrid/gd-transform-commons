from typing import Any, Dict

from gdtransform.transform import transformation


@transformation(name='noop-transformation')
def noop_transformation(data: Dict[str, Any]):
    # do nothing
    pass
