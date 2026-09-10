class Solution:
    def intToRoman(self, num: int) -> str:
        di = {1:"I" ,  5:"V" ,  10:"X",  50:"L" ,  100:"C", 500:"D",  1000:"M"}
        n = []
        st = []
        while num > 0:
            p = num%10
            num = num // 10
            n.append(p)
        pow = len(n)-1
        i = len(n) -1
        while i >= 0:
            curr = n[i]
            to = curr*(10**pow)
            if curr == 4:
                if to < 5:
                    st.append("".join("IV"))
                elif to < 50:
                    st.append("".join("XL"))
                elif to < 500:
                    st.append("".join("CD"))
                to = 0
            elif curr == 9:
                if to < 10:
                    st.append("".join("IX"))
                elif to < 100:
                    st.append("".join("XC"))
                elif to < 1000:
                    st.append("".join("CM"))
                to = 0
            else:
                if curr > 5:
                    if to <10:
                        d = to - 5
                        st.append("".join("V"+'I'*d))
                    elif to < 100:
                        d = (to - 50)//10
                        st.append("".join("L"+'X'*d))
                    elif to < 1000:
                        d = (to - 500)//100
                        st.append("".join("D"+"C"*d))
                if curr < 5:
                    if to <5:
                        st.append("".join("I"*curr))
                    elif to < 50:
                        st.append("".join("X"*curr))
                    elif to < 500:
                        st.append("".join("C"*curr))
                    elif to < 5000:
                        st.append("".join("M"*curr))
                else:
                    if to == 5:
                        st.append("V")
                    elif to == 50:
                        st.append("L")
                    elif to == 500:
                        st.append("D")
            i -= 1
            pow -= 1

        s = ""
        for j in range(len(st)):
            c = st[j]
            s += c
        print(s)
        return s
        