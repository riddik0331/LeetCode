class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        start_comb = '0' * (10 - turnedOn) + '1' * turnedOn
        start_num = int(start_comb, base=2)
        end_num = int(start_comb[::-1], base=2)
        res = []
        while start_num <= end_num:
            comb = format(start_num, '010b')
            if comb.count('1') == turnedOn:
                hours = int(comb[:4], base=2)
                minutes = int(comb[4:], base=2)
                if hours <= 11 and minutes <= 59:
                    if minutes in range(10):
                        minutes = '0' + str(minutes)
                    else:
                        minutes = str(minutes)
                    valid_time = f'{hours}:{minutes}'
                    res.append(valid_time)
            start_num += 1

        return res
