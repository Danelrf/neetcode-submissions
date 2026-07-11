class Solution:
    def isValid(self, s: str) -> bool:
        print(f"starting {s}")
        if len(s)%2: # Length must be even
            return False
        
        tracker = []
        next_to_close = ""

        for el in s:
            # print(f"processing {el}, tracker is {tracker}, next_to_close is {next_to_close}")
            if el not in ("[","]","(",")","{","}"):
                
                print(f"tracker is {tracker}, el is {el}")

                return False
            
            if el in "[":
                tracker.append(el)
                next_to_close = "]"

            if el == "(":
                tracker.append(el)
                next_to_close = ")"
                
            if el == "{":
                tracker.append(el)
                next_to_close = "}"

            if el in [")","]","}"]:
                if el != next_to_close or len(tracker) == 0:

                    return False 
                
                tracker.pop()

                if len(tracker) == 0:
                    next_to_close == "" 
                    continue

                if tracker[-1] == "[":
                    next_to_close = "]"
                if tracker[-1] == "{":
                    next_to_close = "}"
                if tracker[-1] == "(":
                    next_to_close = ")"

            
        return not bool(len(tracker))