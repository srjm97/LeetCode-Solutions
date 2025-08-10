class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_string = str(n)
        l = len(n_string)
        n_dict = {}
        print(type(n_string))
        for i in range(0,l):
            n_dict[n_string[i]] = n_dict.get(n_string[i], 0) + 1
        for i in range(0,32):
            tmp = 2 ** i
            tmp_string = str(tmp)
            l_tmp = len(tmp_string)
            if l_tmp < l:
                continue
            elif l_tmp > l:
                break
            tmp_dict = {}
            for j in range(0,l_tmp):
                tmp_dict[tmp_string[j]] = tmp_dict.get(tmp_string[j], 0) + 1
            if n_dict == tmp_dict:
                return True
        return False