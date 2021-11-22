from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        set_ = set()
        for email in emails:
            if (valid_email := self.is_valid(email)) is not None:
                set_.add(valid_email)
        return len(set_)


    def is_valid(self, email):
        local, domain = email.split('@')
        local = local.replace(".", "").split("+")[0]

        return f"{local}@{domain}"

print(Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(Solution().numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
print(Solution().numUniqueEmails(["+123@abc.com"]))
