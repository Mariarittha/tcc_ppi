from django.contrib.auth.mixins import UserPassesTestMixin


class AdmPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador"):
            return True
        return False

class FiloPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Filomena"):
            return True
        return False