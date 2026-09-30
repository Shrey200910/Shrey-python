def mutate_list(lst: list) -> None:
    """
    Mutate `lst` in place by appending the value 4 to it.
    Do not reassign lst to a new object. Return nothing.
    """
    lst.append(4)


def reassign_list(lst: list) -> list:
    """
    Create a brand-new list [9, 9, 9] and return it, without
    mutating the original `lst` in any way.
    """
    return [9, 9, 9]


def observe_through_alias(original: list) -> dict:
    """
    Inside this function:
      1. Create `alias = original` (a second variable pointing
         at the same object).
      2. Mutate `original` by appending 100 to it.
      3. Reassign `original` to a brand-new list [0, 0, 0]
         (do not mutate this new list into alias's object).

    Return a dictionary:
      {
        "alias_after_mutation": <contents of alias right after step 2>,
        "alias_after_reassignment": <contents of alias right after step 3>,
        "original_final": <contents of original at the end>
      }
    """
    alias = original
    original.append(100)
    alias_after_1 = list(alias)
    original = [0, 0, 0]
    alias_after_2 = list(alias)
    return {
        "alias_after_mutation": alias_after_1,
        "alias_after_reassignment": alias_after_2,
        "original_final": original
      }
