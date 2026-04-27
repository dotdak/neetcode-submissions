class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        encoded = []
        for s in strs:
            word = []
            for ch in s:
                # Use a separator-safe encoding approach
                word.append(str(ord(ch)))
            encoded.append(",".join(word))
        return "!".join(encoded)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        decoded = []
        for encoded_word in s.split("!"):
            if not encoded_word:
                decoded.append("")
                continue
            word = []
            for ch_code in encoded_word.split(","):
                word.append(chr(int(ch_code)))
            decoded.append("".join(word))

            
        return decoded