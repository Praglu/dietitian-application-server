from rest_framework.exceptions import ValidationError


class AbstractCommand(object):
    def _raise_account_validation_error(self, error):
        raise ValidationError(
            detail={
                'user': error.value.format(
                    pk=self.user.pk,
                ),
            },
        )
