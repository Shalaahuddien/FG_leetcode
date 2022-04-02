class AuthenticationManager:

    def __init__(self, timeToLive: int) -> None:
        self.ttl = timeToLive
        self.expiry = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        self.expiry[tokenId] = self.ttl + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        if tokenId in self.expiry:
            self.expiry.move_to_end(tokenId)
            self.expiry[tokenId] = self.ttl + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evict_expired(currentTime)
        return len(self.expiry)

    def evict_expired(self, currentTime: int) -> None:
        while self.expiry and next(iter(self.expiry.values())) <= currentTime:
            self.expiry.popitem(last=False)
            
            
# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)