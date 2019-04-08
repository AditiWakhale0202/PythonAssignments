map_vowel = {}
S = "JootaJapani"
print S
k = len(S)
vowel_list = ['a', 'e', 'i', 'o', 'u']
start_indx = -1
long = 0
for k in range(len(S)):
    if S[k] in vowel_list:
        if start_indx == -1:
            start_indx = k
        long = long + 1
    else:
        if start_indx != -1:
            map_vowel.update({start_indx: long})
        start_indx = -1
        long = 0
if start_indx !=-1 and start_indx not in map_vowel:
    map_vowel.update({start_indx:long})



final_len = 0
last_key = -1
start = False
end = False
if 0 in map_vowel:
    start = True

for keys in map_vowel:
    last_key = keys if keys > last_key else last_key
if last_key + map_vowel[last_key] == len(S):
    end = True


def get_max(vowel_dict, *keys):
    key_list = keys
    maxme = 0
    for k in vowel_dict:
        if k not in key_list:
            maxme = vowel_dict[k] if maxme < vowel_dict[k] else maxme
    return maxme


if start == True and end == True:
    final_len = map_vowel[0] + get_max(map_vowel, 0, last_key) + map_vowel[last_key]
elif start == True and end == False:
    final_len = map_vowel[0] + get_max(map_vowel, 0)
elif start == False and end == True:
    final_len = map_vowel[last_key] + get_max(map_vowel, last_key)
else:
    final_len = get_max(map_vowel)

print final_len
