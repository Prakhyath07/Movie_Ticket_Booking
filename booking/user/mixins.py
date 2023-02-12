class UserQuerySetMixin():
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs1 =qs.filter(user = user)
        # qs2 = qs.filter(public = True)
        # qsFinal = (qs1 | qs2).distinct()
        return qs1

class UserEditSetMixin():
    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        qs1 =qs.filter(user = user)
        return qs1