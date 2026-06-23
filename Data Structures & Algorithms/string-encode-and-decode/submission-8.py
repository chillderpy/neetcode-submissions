class Solution:

    def encode(self, strs: List[str]) -> str:
        if (strs == []):
            return '他'
        return '我'.join(strs)
    def decode(self, s: str) -> List[str]:
        if (s == '他'):
            return []
        return s.split('我')