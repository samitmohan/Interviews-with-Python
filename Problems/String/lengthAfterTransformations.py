'''
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/?envType=daily-question&envId=2025-05-13
Keep a set of alphabets
    
abcyy
two transformations
first trans
a -> b 
b -> c
c -> d
y -> z
y -> z

second
b -> c
c -> d
d -> e
z -> ab
z -> ab
cdeabab

third
c -> d
d -> e
e -> f
a -> b
b -> c
a -> b
b -> c
defbcbc

t is in range 10^5 -> bruteforce won't work.
is there a pattern here?

Gist of the problem  (Bruteforce)

final_str = ''
for every_t in range(t):
    for ch in s:
        if ch == 'z': 
            final_str += 'ab'
        else:
            final_str += chr(ord(ch) + 1)
    s = final_str
    ans = len(s)
    final_str = ''
return ans

# OR

for _ in range(t):
    s = ''.join('ab' if ch == 'z' else chr(ord(ch) + 1) for ch in s)
return len(s)

OR 

char_Freq = counter(s)
for _ in range(t):
    ans = {}
    for ch, freq in char_freq:
        if ch == 'z':
            ans['a'] = ans.get('a', 0) + freq
            ans['b'] = ans.get('b', 0) + freq
        else:
            new_ch = (chr(ord(ch) + 1)
            ans[new_ch] = ans.get(new_ch, 0) + freq
    char_Freq = ans
return len(char_freq.items())


b -> c
c -> d
y -> z
y -> z

Every transformation is deterministic and character-wise. 
The only length-changing operation is when 'z' turns into 'ab', increasing the total count by 1 for every 'z'

Since I only care about length -> I can only increment length by 1 when I encounter z and also need to keep freq of char that
lead to z (not all)

Count of each character (z, maybe y) — but just enough to compute future zs.
Don’t need to know how many of every character exists — just how many new zs get in the next round.

y becomes z
x becomes y -> becomes z next round
a becomes b -> becomes z after 25 rounds
Can track how many of each letter will become z in future.
freq[26] : a-to-z array


>>> for ch in s:
...     a[ord(ch) - ord('a')] += 1
...     
>>> a
[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]


freq[25] = count of number of zs -> all of that changes to ab
new_freq[0] += freq[25] and new_freq[1] += freq[25] # new number of ab's are number of zs in prevs freq arr
ans += freq[25] # only count number of final z length
freq = new_freq

s = "az":
Initial freq:
    'a': 1 → freq[0] = 1
    'z': 1 → freq[25] = 1
after 1 transformation:
'a' becomes 'b' → next_freq[1] += 1
'z' becomes 'ab' → next_freq[0] += 1, next_freq[1] += 1
new length = 2 (original) + 1 ('z' → 'ab') = 3

'a': 1
'b': 2

And so on...

'''

def lengthAfterTransformations(s: str, t: int) -> int:
    freq = [0] * 26 
    ans = len(s)
    for ch in s:
        freq[ord(ch) - ord('a')] += 1 # [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
    for _ in range(t):
        new_freq = [0] * 26 
        # for i in range(25): # a to y
        for i in range(max(0, 25 - t), 25):  # 'a' to 'y', but skip early ones
            new_freq[i+1] += freq[i] # a becomes b, b becomes c (count)
        # for z
        new_freq[0] += freq[25] # number of z -> change to ab
        new_freq[1] += freq[25] 
        ans += freq[25] # final ans is just the count of z's
        freq = new_freq # update
    return ans
    

'''
More optimisation-:
During the loop, instead of blindly looping i in range(25) (all characters)
loop only through characters where: 25 - i <= t
'''

def main():
    print(lengthAfterTransformations(s = "abcyy", t = 2)) # 7
    print(lengthAfterTransformations( s = "azbk", t = 1)) # 5
main()