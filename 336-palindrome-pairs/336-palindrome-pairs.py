class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dic={word:i for i,word in enumerate(words)}
        ans=set()
        for k in range(len(words)):
            word=words[k]
            if not word:
                continue
            if word==word[::-1] and "" in dic:
                ans.add((k,dic[""]))
                ans.add((dic[""],k))
            for i in range(len(word)):
                left=word[:i]
                ltarget=word[i:][::-1]
                if left==left[::-1] and ltarget!=word and ltarget in dic:
                    ans.add((dic[ltarget],k))
                j=len(word)-i
                right=word[j:]
                target=word[:j][::-1]
                if right==right[::-1] and target!=word and target in dic:
                    ans.add((k,dic[target]))
        return list(ans)