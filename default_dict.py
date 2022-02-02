from collections import defaultdict
from typing import Dict, List

mah_default_dict: Dict[str, List[int]] = defaultdict(list)
mah_default_dict['test'].append(0)

print(mah_default_dict)