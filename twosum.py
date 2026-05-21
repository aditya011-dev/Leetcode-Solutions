# TWO SUM — Complete Solution
# ============================
# Problem: Find two numbers in array that add up to target
# Return their indexes (positions)

def twoSum(nums, target):

    # ----------------------------------------
    # STEP 1: Create our notebook (hash map)
    # ----------------------------------------
    # Remember: hash map = dictionary in Python
    # It stores things as KEY → VALUE pairs
    # Just like contacts: "Mom" → "98765-43210"
    #
    # Here we will store: NUMBER → INDEX
    # Example: if we see number 2 at position 0
    # we store: {2: 0}
    # This means "I have seen number 2 at index 0"
    #
    # Why? So later when we need 2, we can find it
    # INSTANTLY instead of searching whole array!
    # ----------------------------------------
    seen = {}   # empty notebook, nothing seen yet


    # ----------------------------------------
    # STEP 2: Loop through every number ONCE
    # ----------------------------------------
    # enumerate() gives us both:
    #   i   → the index (position) 0, 1, 2, 3...
    #   num → the actual number 2, 7, 11, 15...
    #
    # Without enumerate:  for num in nums
    #                     → gives 2, 7, 11, 15
    #
    # With enumerate:     for i, num in enumerate(nums)
    #                     → gives (0,2), (1,7), (2,11), (3,15)
    #
    # We need index too because problem asks us
    # to RETURN indexes, not the numbers themselves!
    # ----------------------------------------
    for i, num in enumerate(nums):


        # ----------------------------------------
        # STEP 3: Calculate what number we NEED
        # ----------------------------------------
        # This is the core math of the problem
        #
        # If target = 9 and current number = 2
        # We need 9 - 2 = 7
        #
        # If target = 9 and current number = 7
        # We need 9 - 7 = 2
        #
        # This needed number is called "complement"
        # complement = the missing piece of the puzzle 🧩
        # ----------------------------------------
        complement = target - num


        # ----------------------------------------
        # STEP 4: Check if we've seen complement before
        # ----------------------------------------
        # This is where hash map magic happens! ✨
        #
        # "if complement in seen" checks our notebook
        # INSTANTLY in O(1) time!
        #
        # No need to loop through array again!
        # No need to search anything!
        # Just check notebook — YES or NO — instant!
        #
        # If YES → we found our pair! 🎉
        # If NO  → keep going, write current num down
        # ----------------------------------------
        if complement in seen:

            # ----------------------------------------
            # STEP 5: Return the answer
            # ----------------------------------------
            # We found both numbers!
            #
            # seen[complement] → gives us the INDEX
            #                    where complement was
            #
            # i → current index we're at right now
            #
            # Example:
            # seen = {2: 0}  ← 2 was at index 0
            # complement = 2
            # seen[complement] = seen[2] = 0
            # i = 1 (we're currently at index 1)
            #
            # So return [0, 1] ✅
            # ----------------------------------------
            return [seen[complement], i]


        # ----------------------------------------
        # STEP 6: Write current number in notebook
        # ----------------------------------------
        # If complement was NOT found, we're not done yet
        # So write current number + its index in notebook
        # 
        # Why? Because future numbers might NEED
        # current number as their complement!
        #
        # Example:
        # We're at num=2, complement needed was 7
        # 7 not found yet, so write: seen = {2: 0}
        # Later when num=7, it'll look for 2
        # And find it instantly in our notebook! ⚡
        #
        # KEY → VALUE
        # num  → i
        # 2    → 0    meaning "saw number 2 at index 0"
        # ----------------------------------------
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9

result = twoSum(nums, target)  # actually RUN it

print(result)                  # actually SEE the output