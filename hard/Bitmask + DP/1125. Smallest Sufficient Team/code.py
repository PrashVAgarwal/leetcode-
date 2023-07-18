class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = {skill:i for i,skill in enumerate(req_skills)}
        dp={0:[]}
        
        for i,p in enumerate(people):
            val=0
            for skill in p:
                val |= 1<<skills[skill]
                
            for prevSkills, team in list(dp.items()):
                newSkills = prevSkills | val
                
                #if newSkills == prevSkills:
                 #   continue
                
                # len(dp[newSkills]) > len(team) +1 means that the newSkills entry is in our dp so we check if its team length is greater than the current team's length +1. As if we add the new person's skill to the prev_skills, we can get newSkills with a length of len(team)+1, so we update the newSkills
                if newSkills not in dp or len(dp[newSkills]) > len(team) +1:
                    dp[newSkills]=team + [i]
                    
        return dp[(1<<len(req_skills))-1]
