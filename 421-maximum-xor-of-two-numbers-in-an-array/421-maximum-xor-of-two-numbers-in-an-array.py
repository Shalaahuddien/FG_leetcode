class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        # zero left-paddiung to ensure L bits for each number
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            cur_xor = 0
            for bit in num:
                # insert new num in trie
                node = node.setdefault(bit, {})

                # to compute max xor of that new number with all previously inserted
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    cur_xor = (cur_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    cur_xor = cur_xor << 1
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, cur_xor)
        return max_xor