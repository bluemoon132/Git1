class Lama:
    def convert(self, number):
        dict1 = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                 5: 'V', 4: 'IV', 1: 'I'}
        arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        converted_num = ''
        i = 0
        while number > 0:
            for j in range(number // arr[i]):
                converted_num += dict1[arr[i]]
                number -= arr[i]
            i += 1
        return converted_num
value_lama = Lama()

print(value_lama.convert(int(input())))
