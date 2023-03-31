class Solution:
    def compress(self, chars):

        ans = []

        cout = 1
        for i in range(len(chars) - 1):

            if chars[i] == chars[i + 1]:
                cout += 1

            elif chars[i] != chars[i + 1] and cout >= 10:
                ans.append(chars[i])

                val = []
                while cout > 0:
                    val.append(cout % 10)
                    cout = cout // 10


                for i in val[::-1]:
                    ans.append(str(i))

                cout = 1

            elif chars[i] != chars[i + 1] and cout > 1:
                ans.append(chars[i])
                ans.append(str(cout))
                cout = 1

            elif chars[i] != chars[i + 1] and cout == 1:
                ans.append(chars[i])



        if cout >= 10:

            ans.append(chars[i])

            val = []

            while cout > 0:
                val.append(cout % 10)

                cout = cout // 10

            for i in val[::-1]:
                ans.append(str(i))

            cout = 1


        elif cout > 1:

            ans.append(chars[-1])

            ans.append(str(cout))

        else:

            ans.append(chars[-1])

        print(ans)
        return len(ans)

ans = Solution()
chars = ["o","o","o","o","o","o","o","o","o","o"]
print(ans.compress((chars)))



