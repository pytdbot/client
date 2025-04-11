from typing import Union, List
from .. import types


class TDLibFunctions:
    """A class that include all TDLib functions"""

    async def getAuthorizationState(
        self,
    ) -> Union["types.Error", "types.AuthorizationState"]:
        r"""Returns the current authorization state\. This is an offline method\. For informational purposes only\. Use updateAuthorizationState instead to maintain the current authorization state\. Can be called before initialization

        Returns:
            :class:`~pytdbot.types.AuthorizationState`
        """

        return await self.invoke(
            {
                "@type": "getAuthorizationState",
            }
        )

    async def setTdlibParameters(
        self,
        use_test_dc: bool = False,
        database_directory: str = "",
        files_directory: str = "",
        database_encryption_key: bytes = b"",
        use_file_database: bool = False,
        use_chat_info_database: bool = False,
        use_message_database: bool = False,
        use_secret_chats: bool = False,
        api_id: int = 0,
        api_hash: str = "",
        system_language_code: str = "",
        device_model: str = "",
        system_version: str = "",
        application_version: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the parameters for TDLib initialization\. Works only when the current authorization state is authorizationStateWaitTdlibParameters

        Parameters:
            use_test_dc (:class:`bool`):
                Pass true to use Telegram test environment instead of the production environment

            database_directory (:class:`str`):
                The path to the directory for the persistent database; if empty, the current working directory will be used

            files_directory (:class:`str`):
                The path to the directory for storing files; if empty, database\_directory will be used

            database_encryption_key (:class:`bytes`):
                Encryption key for the database\. If the encryption key is invalid, then an error with code 401 will be returned

            use_file_database (:class:`bool`):
                Pass true to keep information about downloaded and uploaded files between application restarts

            use_chat_info_database (:class:`bool`):
                Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts\. Implies use\_file\_database

            use_message_database (:class:`bool`):
                Pass true to keep cache of chats and messages between restarts\. Implies use\_chat\_info\_database

            use_secret_chats (:class:`bool`):
                Pass true to enable support for secret chats

            api_id (:class:`int`):
                Application identifier for Telegram API access, which can be obtained at https://my\.telegram\.org

            api_hash (:class:`str`):
                Application identifier hash for Telegram API access, which can be obtained at https://my\.telegram\.org

            system_language_code (:class:`str`):
                IETF language tag of the user's operating system language; must be non\-empty

            device_model (:class:`str`):
                Model of the device the application is being run on; must be non\-empty

            system_version (:class:`str`):
                Version of the operating system the application is being run on\. If empty, the version is automatically detected by TDLib

            application_version (:class:`str`):
                Application version; must be non\-empty

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setTdlibParameters",
                "use_test_dc": use_test_dc,
                "database_directory": database_directory,
                "files_directory": files_directory,
                "database_encryption_key": database_encryption_key,
                "use_file_database": use_file_database,
                "use_chat_info_database": use_chat_info_database,
                "use_message_database": use_message_database,
                "use_secret_chats": use_secret_chats,
                "api_id": api_id,
                "api_hash": api_hash,
                "system_language_code": system_language_code,
                "device_model": device_model,
                "system_version": system_version,
                "application_version": application_version,
            }
        )

    async def setAuthenticationPhoneNumber(
        self,
        phone_number: str = "",
        settings: "types.PhoneNumberAuthenticationSettings" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the phone number of the user and sends an authentication code to the user\. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitPremiumPurchase, authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Parameters:
            phone_number (:class:`str`):
                The phone number of the user, in international format

            settings (:class:`"types.PhoneNumberAuthenticationSettings"`):
                Settings for the authentication of the user's phone number; pass null to use default settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setAuthenticationPhoneNumber",
                "phone_number": phone_number,
                "settings": settings,
            }
        )

    async def checkAuthenticationPremiumPurchase(
        self, currency: str = "", amount: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether an in\-store purchase of Telegram Premium is possible before authorization\. Works only when the current authorization state is authorizationStateWaitPremiumPurchase

        Parameters:
            currency (:class:`str`):
                ISO 4217 currency code of the payment currency

            amount (:class:`int`):
                Paid amount, in the smallest units of the currency

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "checkAuthenticationPremiumPurchase",
                "currency": currency,
                "amount": amount,
            }
        )

    async def setAuthenticationPremiumPurchaseTransaction(
        self,
        transaction: "types.StoreTransaction" = None,
        is_restore: bool = False,
        currency: str = "",
        amount: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs server about an in\-store purchase of Telegram Premium before authorization\. Works only when the current authorization state is authorizationStateWaitPremiumPurchase

        Parameters:
            transaction (:class:`"types.StoreTransaction"`):
                Information about the transaction

            is_restore (:class:`bool`):
                Pass true if this is a restore of a Telegram Premium purchase; only for App Store

            currency (:class:`str`):
                ISO 4217 currency code of the payment currency

            amount (:class:`int`):
                Paid amount, in the smallest units of the currency

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setAuthenticationPremiumPurchaseTransaction",
                "transaction": transaction,
                "is_restore": is_restore,
                "currency": currency,
                "amount": amount,
            }
        )

    async def setAuthenticationEmailAddress(
        self, email_address: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the email address of the user and sends an authentication code to the email address\. Works only when the current authorization state is authorizationStateWaitEmailAddress

        Parameters:
            email_address (:class:`str`):
                The email address of the user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setAuthenticationEmailAddress", "email_address": email_address}
        )

    async def resendAuthenticationCode(
        self, reason: "types.ResendCodeReason" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Resends an authentication code to the user\. Works only when the current authorization state is authorizationStateWaitCode, the next\_code\_type of the result is not null and the server\-specified timeout has passed, or when the current authorization state is authorizationStateWaitEmailCode

        Parameters:
            reason (:class:`"types.ResendCodeReason"`):
                Reason of code resending; pass null if unknown

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "resendAuthenticationCode", "reason": reason}
        )

    async def checkAuthenticationEmailCode(
        self, code: "types.EmailAddressAuthentication" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the authentication of an email address\. Works only when the current authorization state is authorizationStateWaitEmailCode

        Parameters:
            code (:class:`"types.EmailAddressAuthentication"`):
                Email address authentication to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkAuthenticationEmailCode", "code": code}
        )

    async def checkAuthenticationCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the authentication code\. Works only when the current authorization state is authorizationStateWaitCode

        Parameters:
            code (:class:`str`):
                Authentication code to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "checkAuthenticationCode", "code": code})

    async def requestQrCodeAuthentication(
        self, other_user_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Requests QR code authentication by scanning a QR code on another logged in device\. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitPremiumPurchase, authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Parameters:
            other_user_ids (:class:`List[int]`):
                List of user identifiers of other users currently using the application

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "requestQrCodeAuthentication", "other_user_ids": other_user_ids}
        )

    async def registerUser(
        self,
        first_name: str = "",
        last_name: str = "",
        disable_notification: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Finishes user registration\. Works only when the current authorization state is authorizationStateWaitRegistration

        Parameters:
            first_name (:class:`str`):
                The first name of the user; 1\-64 characters

            last_name (:class:`str`):
                The last name of the user; 0\-64 characters

            disable_notification (:class:`bool`):
                Pass true to disable notification about the current user joining Telegram for other users that added them to contact list

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "registerUser",
                "first_name": first_name,
                "last_name": last_name,
                "disable_notification": disable_notification,
            }
        )

    async def resetAuthenticationEmailAddress(self) -> Union["types.Error", "types.Ok"]:
        r"""Resets the login email address\. May return an error with a message \"TASK\_ALREADY\_EXISTS\" if reset is still pending\. Works only when the current authorization state is authorizationStateWaitEmailCode and authorization\_state\.can\_reset\_email\_address \=\= true

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "resetAuthenticationEmailAddress",
            }
        )

    async def checkAuthenticationPassword(
        self, password: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the 2\-step verification password for correctness\. Works only when the current authorization state is authorizationStateWaitPassword

        Parameters:
            password (:class:`str`):
                The 2\-step verification password to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkAuthenticationPassword", "password": password}
        )

    async def requestAuthenticationPasswordRecovery(
        self,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Requests to send a 2\-step verification password recovery code to an email address that was previously set up\. Works only when the current authorization state is authorizationStateWaitPassword

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "requestAuthenticationPasswordRecovery",
            }
        )

    async def checkAuthenticationPasswordRecoveryCode(
        self, recovery_code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether a 2\-step verification password recovery code sent to an email address is valid\. Works only when the current authorization state is authorizationStateWaitPassword

        Parameters:
            recovery_code (:class:`str`):
                Recovery code to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "checkAuthenticationPasswordRecoveryCode",
                "recovery_code": recovery_code,
            }
        )

    async def recoverAuthenticationPassword(
        self, recovery_code: str = "", new_password: str = "", new_hint: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Recovers the 2\-step verification password with a password recovery code sent to an email address that was previously set up\. Works only when the current authorization state is authorizationStateWaitPassword

        Parameters:
            recovery_code (:class:`str`):
                Recovery code to check

            new_password (:class:`str`):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (:class:`str`):
                New password hint; may be empty

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "recoverAuthenticationPassword",
                "recovery_code": recovery_code,
                "new_password": new_password,
                "new_hint": new_hint,
            }
        )

    async def sendAuthenticationFirebaseSms(
        self, token: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends Firebase Authentication SMS to the phone number of the user\. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

        Parameters:
            token (:class:`str`):
                Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "sendAuthenticationFirebaseSms", "token": token}
        )

    async def reportAuthenticationCodeMissing(
        self, mobile_network_code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports that authentication code wasn't delivered via SMS; for official mobile applications only\. Works only when the current authorization state is authorizationStateWaitCode

        Parameters:
            mobile_network_code (:class:`str`):
                Current mobile network code

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportAuthenticationCodeMissing",
                "mobile_network_code": mobile_network_code,
            }
        )

    async def checkAuthenticationBotToken(
        self, token: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the authentication token of a bot; to log in as a bot\. Works only when the current authorization state is authorizationStateWaitPhoneNumber\. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

        Parameters:
            token (:class:`str`):
                The bot token

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkAuthenticationBotToken", "token": token}
        )

    async def logOut(self) -> Union["types.Error", "types.Ok"]:
        r"""Closes the TDLib instance after a proper logout\. Requires an available network connection\. All local data will be destroyed\. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "logOut",
            }
        )

    async def close(self) -> Union["types.Error", "types.Ok"]:
        r"""Closes the TDLib instance\. All databases will be flushed to disk and properly closed\. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent\. Can be called before initialization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "close",
            }
        )

    async def destroy(self) -> Union["types.Error", "types.Ok"]:
        r"""Closes the TDLib instance, destroying all local data without a proper logout\. The current user session will remain in the list of all active sessions\. All local data will be destroyed\. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "destroy",
            }
        )

    async def confirmQrCodeAuthentication(
        self, link: str = ""
    ) -> Union["types.Error", "types.Session"]:
        r"""Confirms QR code authentication on another device\. Returns created session on success

        Parameters:
            link (:class:`str`):
                A link from a QR code\. The link must be scanned by the in\-app camera

        Returns:
            :class:`~pytdbot.types.Session`
        """

        return await self.invoke({"@type": "confirmQrCodeAuthentication", "link": link})

    async def getCurrentState(self) -> Union["types.Error", "types.Updates"]:
        r"""Returns all updates needed to restore current TDLib state, i\.e\. all actual updateAuthorizationState/updateUser/updateNewChat and others\. This is especially useful if TDLib is run in a separate process\. Can be called before initialization

        Returns:
            :class:`~pytdbot.types.Updates`
        """

        return await self.invoke(
            {
                "@type": "getCurrentState",
            }
        )

    async def setDatabaseEncryptionKey(
        self, new_encryption_key: bytes = b""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the database encryption key\. Usually the encryption key is never changed and is stored in some OS keychain

        Parameters:
            new_encryption_key (:class:`bytes`):
                New encryption key

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setDatabaseEncryptionKey",
                "new_encryption_key": new_encryption_key,
            }
        )

    async def getPasswordState(self) -> Union["types.Error", "types.PasswordState"]:
        r"""Returns the current state of 2\-step verification

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "getPasswordState",
            }
        )

    async def setPassword(
        self,
        old_password: str = "",
        new_password: str = "",
        new_hint: str = "",
        set_recovery_email_address: bool = False,
        new_recovery_email_address: str = "",
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Changes the 2\-step verification password for the current user\. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

        Parameters:
            old_password (:class:`str`):
                Previous 2\-step verification password of the user

            new_password (:class:`str`):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (:class:`str`):
                New password hint; may be empty

            set_recovery_email_address (:class:`bool`):
                Pass true to change also the recovery email address

            new_recovery_email_address (:class:`str`):
                New recovery email address; may be empty

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "setPassword",
                "old_password": old_password,
                "new_password": new_password,
                "new_hint": new_hint,
                "set_recovery_email_address": set_recovery_email_address,
                "new_recovery_email_address": new_recovery_email_address,
            }
        )

    async def setLoginEmailAddress(
        self, new_login_email_address: str = ""
    ) -> Union["types.Error", "types.EmailAddressAuthenticationCodeInfo"]:
        r"""Changes the login email address of the user\. The email address can be changed only if the current user already has login email and passwordState\.login\_email\_address\_pattern is non\-empty\. The change will not be applied until the new login email address is confirmed with checkLoginEmailAddressCode\. To use Apple ID/Google ID instead of an email address, call checkLoginEmailAddressCode directly

        Parameters:
            new_login_email_address (:class:`str`):
                New login email address

        Returns:
            :class:`~pytdbot.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "setLoginEmailAddress",
                "new_login_email_address": new_login_email_address,
            }
        )

    async def resendLoginEmailAddressCode(
        self,
    ) -> Union["types.Error", "types.EmailAddressAuthenticationCodeInfo"]:
        r"""Resends the login email address verification code

        Returns:
            :class:`~pytdbot.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "resendLoginEmailAddressCode",
            }
        )

    async def checkLoginEmailAddressCode(
        self, code: "types.EmailAddressAuthentication" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the login email address authentication

        Parameters:
            code (:class:`"types.EmailAddressAuthentication"`):
                Email address authentication to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "checkLoginEmailAddressCode", "code": code})

    async def getRecoveryEmailAddress(
        self, password: str = ""
    ) -> Union["types.Error", "types.RecoveryEmailAddress"]:
        r"""Returns a 2\-step verification recovery email address that was previously set up\. This method can be used to verify a password provided by the user

        Parameters:
            password (:class:`str`):
                The 2\-step verification password for the current user

        Returns:
            :class:`~pytdbot.types.RecoveryEmailAddress`
        """

        return await self.invoke(
            {"@type": "getRecoveryEmailAddress", "password": password}
        )

    async def setRecoveryEmailAddress(
        self, password: str = "", new_recovery_email_address: str = ""
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Changes the 2\-step verification recovery email address of the user\. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed\. If new\_recovery\_email\_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation

        Parameters:
            password (:class:`str`):
                The 2\-step verification password of the current user

            new_recovery_email_address (:class:`str`):
                New recovery email address

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "setRecoveryEmailAddress",
                "password": password,
                "new_recovery_email_address": new_recovery_email_address,
            }
        )

    async def checkRecoveryEmailAddressCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Checks the 2\-step verification recovery email address verification code

        Parameters:
            code (:class:`str`):
                Verification code to check

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {"@type": "checkRecoveryEmailAddressCode", "code": code}
        )

    async def resendRecoveryEmailAddressCode(
        self,
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Resends the 2\-step verification recovery email address verification code

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "resendRecoveryEmailAddressCode",
            }
        )

    async def cancelRecoveryEmailAddressVerification(
        self,
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Cancels verification of the 2\-step verification recovery email address

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "cancelRecoveryEmailAddressVerification",
            }
        )

    async def requestPasswordRecovery(
        self,
    ) -> Union["types.Error", "types.EmailAddressAuthenticationCodeInfo"]:
        r"""Requests to send a 2\-step verification password recovery code to an email address that was previously set up

        Returns:
            :class:`~pytdbot.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "requestPasswordRecovery",
            }
        )

    async def checkPasswordRecoveryCode(
        self, recovery_code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether a 2\-step verification password recovery code sent to an email address is valid

        Parameters:
            recovery_code (:class:`str`):
                Recovery code to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkPasswordRecoveryCode", "recovery_code": recovery_code}
        )

    async def recoverPassword(
        self, recovery_code: str = "", new_password: str = "", new_hint: str = ""
    ) -> Union["types.Error", "types.PasswordState"]:
        r"""Recovers the 2\-step verification password using a recovery code sent to an email address that was previously set up

        Parameters:
            recovery_code (:class:`str`):
                Recovery code to check

            new_password (:class:`str`):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (:class:`str`):
                New password hint; may be empty

        Returns:
            :class:`~pytdbot.types.PasswordState`
        """

        return await self.invoke(
            {
                "@type": "recoverPassword",
                "recovery_code": recovery_code,
                "new_password": new_password,
                "new_hint": new_hint,
            }
        )

    async def resetPassword(self) -> Union["types.Error", "types.ResetPasswordResult"]:
        r"""Removes 2\-step verification password without previous password and access to recovery email address\. The password can't be reset immediately and the request needs to be repeated after the specified time

        Returns:
            :class:`~pytdbot.types.ResetPasswordResult`
        """

        return await self.invoke(
            {
                "@type": "resetPassword",
            }
        )

    async def cancelPasswordReset(self) -> Union["types.Error", "types.Ok"]:
        r"""Cancels reset of 2\-step verification password\. The method can be called if passwordState\.pending\_reset\_date \> 0

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "cancelPasswordReset",
            }
        )

    async def createTemporaryPassword(
        self, password: str = "", valid_for: int = 0
    ) -> Union["types.Error", "types.TemporaryPasswordState"]:
        r"""Creates a new temporary password for processing payments

        Parameters:
            password (:class:`str`):
                The 2\-step verification password of the current user

            valid_for (:class:`int`):
                Time during which the temporary password will be valid, in seconds; must be between 60 and 86400

        Returns:
            :class:`~pytdbot.types.TemporaryPasswordState`
        """

        return await self.invoke(
            {
                "@type": "createTemporaryPassword",
                "password": password,
                "valid_for": valid_for,
            }
        )

    async def getTemporaryPasswordState(
        self,
    ) -> Union["types.Error", "types.TemporaryPasswordState"]:
        r"""Returns information about the current temporary password

        Returns:
            :class:`~pytdbot.types.TemporaryPasswordState`
        """

        return await self.invoke(
            {
                "@type": "getTemporaryPasswordState",
            }
        )

    async def getMe(self) -> Union["types.Error", "types.User"]:
        r"""Returns the current user

        Returns:
            :class:`~pytdbot.types.User`
        """

        return await self.invoke(
            {
                "@type": "getMe",
            }
        )

    async def getUser(self, user_id: int = 0) -> Union["types.Error", "types.User"]:
        r"""Returns information about a user by their identifier\. This is an offline method if the current user is not a bot

        Parameters:
            user_id (:class:`int`):
                User identifier

        Returns:
            :class:`~pytdbot.types.User`
        """

        return await self.invoke({"@type": "getUser", "user_id": user_id})

    async def getUserFullInfo(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.UserFullInfo"]:
        r"""Returns full information about a user by their identifier

        Parameters:
            user_id (:class:`int`):
                User identifier

        Returns:
            :class:`~pytdbot.types.UserFullInfo`
        """

        return await self.invoke({"@type": "getUserFullInfo", "user_id": user_id})

    async def getBasicGroup(
        self, basic_group_id: int = 0
    ) -> Union["types.Error", "types.BasicGroup"]:
        r"""Returns information about a basic group by its identifier\. This is an offline method if the current user is not a bot

        Parameters:
            basic_group_id (:class:`int`):
                Basic group identifier

        Returns:
            :class:`~pytdbot.types.BasicGroup`
        """

        return await self.invoke(
            {"@type": "getBasicGroup", "basic_group_id": basic_group_id}
        )

    async def getBasicGroupFullInfo(
        self, basic_group_id: int = 0
    ) -> Union["types.Error", "types.BasicGroupFullInfo"]:
        r"""Returns full information about a basic group by its identifier

        Parameters:
            basic_group_id (:class:`int`):
                Basic group identifier

        Returns:
            :class:`~pytdbot.types.BasicGroupFullInfo`
        """

        return await self.invoke(
            {"@type": "getBasicGroupFullInfo", "basic_group_id": basic_group_id}
        )

    async def getSupergroup(
        self, supergroup_id: int = 0
    ) -> Union["types.Error", "types.Supergroup"]:
        r"""Returns information about a supergroup or a channel by its identifier\. This is an offline method if the current user is not a bot

        Parameters:
            supergroup_id (:class:`int`):
                Supergroup or channel identifier

        Returns:
            :class:`~pytdbot.types.Supergroup`
        """

        return await self.invoke(
            {"@type": "getSupergroup", "supergroup_id": supergroup_id}
        )

    async def getSupergroupFullInfo(
        self, supergroup_id: int = 0
    ) -> Union["types.Error", "types.SupergroupFullInfo"]:
        r"""Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

        Parameters:
            supergroup_id (:class:`int`):
                Supergroup or channel identifier

        Returns:
            :class:`~pytdbot.types.SupergroupFullInfo`
        """

        return await self.invoke(
            {"@type": "getSupergroupFullInfo", "supergroup_id": supergroup_id}
        )

    async def getSecretChat(
        self, secret_chat_id: int = 0
    ) -> Union["types.Error", "types.SecretChat"]:
        r"""Returns information about a secret chat by its identifier\. This is an offline method

        Parameters:
            secret_chat_id (:class:`int`):
                Secret chat identifier

        Returns:
            :class:`~pytdbot.types.SecretChat`
        """

        return await self.invoke(
            {"@type": "getSecretChat", "secret_chat_id": secret_chat_id}
        )

    async def getChat(self, chat_id: int = 0) -> Union["types.Error", "types.Chat"]:
        r"""Returns information about a chat by its identifier\. This is an offline method if the current user is not a bot

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke({"@type": "getChat", "chat_id": chat_id})

    async def getMessage(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns information about a message\. Returns a 404 error if the message doesn't exist

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message to get

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {"@type": "getMessage", "chat_id": chat_id, "message_id": message_id}
        )

    async def getMessageLocally(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns information about a message, if it is available without sending network request\. Returns a 404 error if message isn't available locally\. This is an offline method

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message to get

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {"@type": "getMessageLocally", "chat_id": chat_id, "message_id": message_id}
        )

    async def getRepliedMessage(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns information about a non\-bundled message that is replied by a given message\. Also, returns the pinned message, the game message, the invoice message, the message with a previously set same background, the giveaway message, and the topic creation message for messages of the types messagePinMessage, messageGameScore, messagePaymentSuccessful, messageChatSetBackground, messageGiveawayCompleted and topic messages without non\-bundled replied message respectively\. Returns a 404 error if the message doesn't exist

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the message belongs to

            message_id (:class:`int`):
                Identifier of the reply message

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {"@type": "getRepliedMessage", "chat_id": chat_id, "message_id": message_id}
        )

    async def getChatPinnedMessage(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns information about a newest pinned message in the chat\. Returns a 404 error if the message doesn't exist

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the message belongs to

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke({"@type": "getChatPinnedMessage", "chat_id": chat_id})

    async def getCallbackQueryMessage(
        self, chat_id: int = 0, message_id: int = 0, callback_query_id: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns information about a message with the callback button that originated a callback query; for bots only

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the message belongs to

            message_id (:class:`int`):
                Message identifier

            callback_query_id (:class:`int`):
                Identifier of the callback query

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "getCallbackQueryMessage",
                "chat_id": chat_id,
                "message_id": message_id,
                "callback_query_id": callback_query_id,
            }
        )

    async def getMessages(
        self, chat_id: int = 0, message_ids: List[int] = None
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns information about messages\. If a message is not found, returns null on the corresponding position of the result

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat the messages belong to

            message_ids (:class:`List[int]`):
                Identifiers of the messages to get

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {"@type": "getMessages", "chat_id": chat_id, "message_ids": message_ids}
        )

    async def getMessageProperties(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.MessageProperties"]:
        r"""Returns properties of a message\. This is an offline method

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.MessageProperties`
        """

        return await self.invoke(
            {
                "@type": "getMessageProperties",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def getMessageThread(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.MessageThreadInfo"]:
        r"""Returns information about a message thread\. Can be used only if messageProperties\.can\_get\_message\_thread \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.MessageThreadInfo`
        """

        return await self.invoke(
            {"@type": "getMessageThread", "chat_id": chat_id, "message_id": message_id}
        )

    async def getMessageReadDate(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.MessageReadDate"]:
        r"""Returns read date of a recent outgoing message in a private chat\. The method can be called if messageProperties\.can\_get\_read\_date \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.MessageReadDate`
        """

        return await self.invoke(
            {
                "@type": "getMessageReadDate",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def getMessageViewers(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.MessageViewers"]:
        r"""Returns viewers of a recent outgoing message in a basic group or a supergroup chat\. For video notes and voice notes only users, opened content of the message, are returned\. The method can be called if messageProperties\.can\_get\_viewers \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.MessageViewers`
        """

        return await self.invoke(
            {"@type": "getMessageViewers", "chat_id": chat_id, "message_id": message_id}
        )

    async def getFile(self, file_id: int = 0) -> Union["types.Error", "types.File"]:
        r"""Returns information about a file\. This is an offline method

        Parameters:
            file_id (:class:`int`):
                Identifier of the file to get

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke({"@type": "getFile", "file_id": file_id})

    async def getRemoteFile(
        self, remote_file_id: str = "", file_type: "types.FileType" = None
    ) -> Union["types.Error", "types.File"]:
        r"""Returns information about a file by its remote identifier\. This is an offline method\. Can be used to register a URL as a file for further uploading, or sending as a message\. Even the request succeeds, the file can be used only if it is still accessible to the user\. For example, if the file is from a message, then the message must be not deleted and accessible to the user\. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

        Parameters:
            remote_file_id (:class:`str`):
                Remote identifier of the file to get

            file_type (:class:`"types.FileType"`):
                File type; pass null if unknown

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "getRemoteFile",
                "remote_file_id": remote_file_id,
                "file_type": file_type,
            }
        )

    async def loadChats(
        self, chat_list: "types.ChatList" = None, limit: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Loads more chats from a chat list\. The loaded chats and their positions in the chat list will be sent through updates\. Chats are sorted by the pair \(chat\.position\.order, chat\.id\) in descending order\. Returns a 404 error if all chats have been loaded

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                The chat list in which to load chats; pass null to load chats from the main chat list

            limit (:class:`int`):
                The maximum number of chats to be loaded\. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "loadChats", "chat_list": chat_list, "limit": limit}
        )

    async def getChats(
        self, chat_list: "types.ChatList" = None, limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns an ordered list of chats from the beginning of a chat list\. For informational purposes only\. Use loadChats and updates processing instead to maintain chat lists in a consistent state

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                The chat list in which to return chats; pass null to get chats from the main chat list

            limit (:class:`int`):
                The maximum number of chats to be returned

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "getChats", "chat_list": chat_list, "limit": limit}
        )

    async def searchPublicChat(
        self, username: str = ""
    ) -> Union["types.Error", "types.Chat"]:
        r"""Searches a public chat by its username\. Currently, only private chats, supergroups and channels can be public\. Returns the chat if found; otherwise, an error is returned

        Parameters:
            username (:class:`str`):
                Username to be resolved

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke({"@type": "searchPublicChat", "username": username})

    async def searchPublicChats(
        self, query: str = ""
    ) -> Union["types.Error", "types.Chats"]:
        r"""Searches public chats by looking for specified query in their username and title\. Currently, only private chats, supergroups and channels can be public\. Returns a meaningful number of results\. Excludes private chats with contacts and chats from the chat list from the results

        Parameters:
            query (:class:`str`):
                Query to search for

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke({"@type": "searchPublicChats", "query": query})

    async def searchChats(
        self, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Searches for the specified query in the title and username of already known chats\. This is an offline method\. Returns chats in the order seen in the main chat list

        Parameters:
            query (:class:`str`):
                Query to search for\. If the query is empty, returns up to 50 recently found chats

            limit (:class:`int`):
                The maximum number of chats to be returned

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "searchChats", "query": query, "limit": limit}
        )

    async def searchChatsOnServer(
        self, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Searches for the specified query in the title and username of already known chats via request to the server\. Returns chats in the order seen in the main chat list

        Parameters:
            query (:class:`str`):
                Query to search for

            limit (:class:`int`):
                The maximum number of chats to be returned

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "searchChatsOnServer", "query": query, "limit": limit}
        )

    async def getRecommendedChats(self) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of channel chats recommended to the current user

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getRecommendedChats",
            }
        )

    async def getChatSimilarChats(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of chats similar to the given chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the target chat; must be an identifier of a channel chat

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke({"@type": "getChatSimilarChats", "chat_id": chat_id})

    async def getChatSimilarChatCount(
        self, chat_id: int = 0, return_local: bool = False
    ) -> Union["types.Error", "types.Count"]:
        r"""Returns approximate number of chats similar to the given chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the target chat; must be an identifier of a channel chat

            return_local (:class:`bool`):
                Pass true to get the number of chats without sending network requests, or \-1 if the number of chats is unknown locally

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke(
            {
                "@type": "getChatSimilarChatCount",
                "chat_id": chat_id,
                "return_local": return_local,
            }
        )

    async def openChatSimilarChat(
        self, chat_id: int = 0, opened_chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that a chat was opened from the list of similar chats\. The method is independent of openChat and closeChat methods

        Parameters:
            chat_id (:class:`int`):
                Identifier of the original chat, which similar chats were requested

            opened_chat_id (:class:`int`):
                Identifier of the opened chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "openChatSimilarChat",
                "chat_id": chat_id,
                "opened_chat_id": opened_chat_id,
            }
        )

    async def getBotSimilarBots(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.Users"]:
        r"""Returns a list of bots similar to the given bot

        Parameters:
            bot_user_id (:class:`int`):
                User identifier of the target bot

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {"@type": "getBotSimilarBots", "bot_user_id": bot_user_id}
        )

    async def getBotSimilarBotCount(
        self, bot_user_id: int = 0, return_local: bool = False
    ) -> Union["types.Error", "types.Count"]:
        r"""Returns approximate number of bots similar to the given bot

        Parameters:
            bot_user_id (:class:`int`):
                User identifier of the target bot

            return_local (:class:`bool`):
                Pass true to get the number of bots without sending network requests, or \-1 if the number of bots is unknown locally

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke(
            {
                "@type": "getBotSimilarBotCount",
                "bot_user_id": bot_user_id,
                "return_local": return_local,
            }
        )

    async def openBotSimilarBot(
        self, bot_user_id: int = 0, opened_bot_user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that a bot was opened from the list of similar bots

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the original bot, which similar bots were requested

            opened_bot_user_id (:class:`int`):
                Identifier of the opened bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "openBotSimilarBot",
                "bot_user_id": bot_user_id,
                "opened_bot_user_id": opened_bot_user_id,
            }
        )

    async def getTopChats(
        self, category: "types.TopChatCategory" = None, limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of frequently used chats

        Parameters:
            category (:class:`"types.TopChatCategory"`):
                Category of chats to be returned

            limit (:class:`int`):
                The maximum number of chats to be returned; up to 30

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "getTopChats", "category": category, "limit": limit}
        )

    async def removeTopChat(
        self, category: "types.TopChatCategory" = None, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a chat from the list of frequently used chats\. Supported only if the chat info database is enabled

        Parameters:
            category (:class:`"types.TopChatCategory"`):
                Category of frequently used chats

            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "removeTopChat", "category": category, "chat_id": chat_id}
        )

    async def searchRecentlyFoundChats(
        self, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Searches for the specified query in the title and username of up to 50 recently found chats\. This is an offline method

        Parameters:
            query (:class:`str`):
                Query to search for

            limit (:class:`int`):
                The maximum number of chats to be returned

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "searchRecentlyFoundChats", "query": query, "limit": limit}
        )

    async def addRecentlyFoundChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a chat to the list of recently found chats\. The chat is added to the beginning of the list\. If the chat is already in the list, it will be removed from the list first

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to add

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "addRecentlyFoundChat", "chat_id": chat_id})

    async def removeRecentlyFoundChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a chat from the list of recently found chats

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to be removed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "removeRecentlyFoundChat", "chat_id": chat_id}
        )

    async def clearRecentlyFoundChats(self) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of recently found chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearRecentlyFoundChats",
            }
        )

    async def getRecentlyOpenedChats(
        self, limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns recently opened chats\. This is an offline method\. Returns chats in the order of last opening

        Parameters:
            limit (:class:`int`):
                The maximum number of chats to be returned

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke({"@type": "getRecentlyOpenedChats", "limit": limit})

    async def checkChatUsername(
        self, chat_id: int = 0, username: str = ""
    ) -> Union["types.Error", "types.CheckChatUsernameResult"]:
        r"""Checks whether a username can be set for a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created

            username (:class:`str`):
                Username to be checked

        Returns:
            :class:`~pytdbot.types.CheckChatUsernameResult`
        """

        return await self.invoke(
            {"@type": "checkChatUsername", "chat_id": chat_id, "username": username}
        )

    async def getCreatedPublicChats(
        self, type: "types.PublicChatType" = None
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of public chats of the specified type, owned by the user

        Parameters:
            type (:class:`"types.PublicChatType"`):
                Type of the public chats to return

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke({"@type": "getCreatedPublicChats", "type": type})

    async def checkCreatedPublicChatsLimit(
        self, type: "types.PublicChatType" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether the maximum number of owned public chats has been reached\. Returns corresponding error if the limit was reached\. The limit can be increased with Telegram Premium

        Parameters:
            type (:class:`"types.PublicChatType"`):
                Type of the public chats, for which to check the limit

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkCreatedPublicChatsLimit", "type": type}
        )

    async def getSuitableDiscussionChats(self) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel\. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group\. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getSuitableDiscussionChats",
            }
        )

    async def getInactiveSupergroupChats(self) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of recently inactive supergroups and channels\. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS\_TOO\_MUCH error\. Also, the limit can be increased with Telegram Premium

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getInactiveSupergroupChats",
            }
        )

    async def getSuitablePersonalChats(self) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of channel chats, which can be used as a personal chat

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getSuitablePersonalChats",
            }
        )

    async def loadSavedMessagesTopics(
        self, limit: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Loads more Saved Messages topics\. The loaded topics will be sent through updateSavedMessagesTopic\. Topics are sorted by their topic\.order in descending order\. Returns a 404 error if all topics have been loaded

        Parameters:
            limit (:class:`int`):
                The maximum number of topics to be loaded\. For optimal performance, the number of loaded topics is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "loadSavedMessagesTopics", "limit": limit})

    async def getSavedMessagesTopicHistory(
        self,
        saved_messages_topic_id: int = 0,
        from_message_id: int = 0,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns messages in a Saved Messages topic\. The messages are returned in reverse chronological order \(i\.e\., in order of decreasing message\_id\)

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic which messages will be fetched

            from_message_id (:class:`int`):
                Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message

            offset (:class:`int`):
                Specify 0 to get results from exactly the message from\_message\_id or a negative offset up to 99 to get additionally some newer messages

            limit (:class:`int`):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than or equal to \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "getSavedMessagesTopicHistory",
                "saved_messages_topic_id": saved_messages_topic_id,
                "from_message_id": from_message_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getSavedMessagesTopicMessageByDate(
        self, saved_messages_topic_id: int = 0, date: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns the last message sent in a Saved Messages topic no later than the specified date

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic which message will be returned

            date (:class:`int`):
                Point in time \(Unix timestamp\) relative to which to search for messages

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "getSavedMessagesTopicMessageByDate",
                "saved_messages_topic_id": saved_messages_topic_id,
                "date": date,
            }
        )

    async def deleteSavedMessagesTopicHistory(
        self, saved_messages_topic_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages in a Saved Messages topic

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic which messages will be deleted

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteSavedMessagesTopicHistory",
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def deleteSavedMessagesTopicMessagesByDate(
        self, saved_messages_topic_id: int = 0, min_date: int = 0, max_date: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages between the specified dates in a Saved Messages topic\. Messages sent in the last 30 seconds will not be deleted

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic which messages will be deleted

            min_date (:class:`int`):
                The minimum date of the messages to delete

            max_date (:class:`int`):
                The maximum date of the messages to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteSavedMessagesTopicMessagesByDate",
                "saved_messages_topic_id": saved_messages_topic_id,
                "min_date": min_date,
                "max_date": max_date,
            }
        )

    async def toggleSavedMessagesTopicIsPinned(
        self, saved_messages_topic_id: int = 0, is_pinned: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the pinned state of a Saved Messages topic\. There can be up to getOption\(\"pinned\_saved\_messages\_topic\_count\_max\"\) pinned topics\. The limit can be increased with Telegram Premium

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic to pin or unpin

            is_pinned (:class:`bool`):
                Pass true to pin the topic; pass false to unpin it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSavedMessagesTopicIsPinned",
                "saved_messages_topic_id": saved_messages_topic_id,
                "is_pinned": is_pinned,
            }
        )

    async def setPinnedSavedMessagesTopics(
        self, saved_messages_topic_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of pinned Saved Messages topics

        Parameters:
            saved_messages_topic_ids (:class:`List[int]`):
                Identifiers of the new pinned Saved Messages topics

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setPinnedSavedMessagesTopics",
                "saved_messages_topic_ids": saved_messages_topic_ids,
            }
        )

    async def getGroupsInCommon(
        self, user_id: int = 0, offset_chat_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns a list of common group chats with a given user\. Chats are sorted by their type and creation date

        Parameters:
            user_id (:class:`int`):
                User identifier

            offset_chat_id (:class:`int`):
                Chat identifier starting from which to return chats; use 0 for the first request

            limit (:class:`int`):
                The maximum number of chats to be returned; up to 100

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getGroupsInCommon",
                "user_id": user_id,
                "offset_chat_id": offset_chat_id,
                "limit": limit,
            }
        )

    async def getChatHistory(
        self,
        chat_id: int = 0,
        from_message_id: int = 0,
        offset: int = 0,
        limit: int = 0,
        only_local: bool = False,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns messages in a chat\. The messages are returned in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib\. This is an offline method if only\_local is true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            from_message_id (:class:`int`):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (:class:`int`):
                Specify 0 to get results from exactly the message from\_message\_id or a negative offset up to 99 to get additionally some newer messages

            limit (:class:`int`):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than or equal to \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_local (:class:`bool`):
                Pass true to get only messages that are available without sending network requests

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "getChatHistory",
                "chat_id": chat_id,
                "from_message_id": from_message_id,
                "offset": offset,
                "limit": limit,
                "only_local": only_local,
            }
        )

    async def getMessageThreadHistory(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        from_message_id: int = 0,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns messages in a message thread of a message\. Can be used only if messageProperties\.can\_get\_message\_thread \=\= true\. Message thread of a channel message is in the channel's linked supergroup\. The messages are returned in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Message identifier, which thread history needs to be returned

            from_message_id (:class:`int`):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (:class:`int`):
                Specify 0 to get results from exactly the message from\_message\_id or a negative offset up to 99 to get additionally some newer messages

            limit (:class:`int`):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than or equal to \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "getMessageThreadHistory",
                "chat_id": chat_id,
                "message_id": message_id,
                "from_message_id": from_message_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def deleteChatHistory(
        self,
        chat_id: int = 0,
        remove_from_chat_list: bool = False,
        revoke: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages in the chat\. Use chat\.can\_be\_deleted\_only\_for\_self and chat\.can\_be\_deleted\_for\_all\_users fields to find whether and how the method can be applied to the chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            remove_from_chat_list (:class:`bool`):
                Pass true to remove the chat from all chat lists

            revoke (:class:`bool`):
                Pass true to delete chat history for all users

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatHistory",
                "chat_id": chat_id,
                "remove_from_chat_list": remove_from_chat_list,
                "revoke": revoke,
            }
        )

    async def deleteChat(self, chat_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a chat along with all messages in the corresponding chat for all chat members\. For group chats this will release the usernames and remove all members\. Use the field chat\.can\_be\_deleted\_for\_all\_users to find whether the method can be applied to the chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deleteChat", "chat_id": chat_id})

    async def searchChatMessages(
        self,
        chat_id: int = 0,
        query: str = "",
        sender_id: "types.MessageSender" = None,
        from_message_id: int = 0,
        offset: int = 0,
        limit: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        message_thread_id: int = 0,
        saved_messages_topic_id: int = 0,
    ) -> Union["types.Error", "types.FoundChatMessages"]:
        r"""Searches for messages with given words in the chat\. Returns the results in reverse chronological order, i\.e\. in order of decreasing message\_id\. Cannot be used in secret chats with a non\-empty query \(searchSecretMessages must be used instead\), or without an enabled message database\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit\. A combination of query, sender\_id, filter and message\_thread\_id search criteria is expected to be supported, only if it is required for Telegram official application implementation

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to search messages

            query (:class:`str`):
                Query to search for

            sender_id (:class:`"types.MessageSender"`):
                Identifier of the sender of messages to search for; pass null to search for messages from any sender\. Not supported in secret chats

            from_message_id (:class:`int`):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (:class:`int`):
                Specify 0 to get results from exactly the message from\_message\_id or a negative offset to get the specified message and some newer messages

            limit (:class:`int`):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            filter (:class:`"types.SearchMessagesFilter"`):
                Additional filter for messages to search; pass null to search for all messages

            message_thread_id (:class:`int`):
                If not 0, only messages in the specified thread will be returned; supergroups only

            saved_messages_topic_id (:class:`int`):
                If not 0, only messages in the specified Saved Messages topic will be returned; pass 0 to return all messages, or for chats other than Saved Messages

        Returns:
            :class:`~pytdbot.types.FoundChatMessages`
        """

        return await self.invoke(
            {
                "@type": "searchChatMessages",
                "chat_id": chat_id,
                "query": query,
                "sender_id": sender_id,
                "from_message_id": from_message_id,
                "offset": offset,
                "limit": limit,
                "filter": filter,
                "message_thread_id": message_thread_id,
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def searchMessages(
        self,
        chat_list: "types.ChatList" = None,
        query: str = "",
        offset: str = "",
        limit: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        chat_type_filter: "types.SearchMessagesChatTypeFilter" = None,
        min_date: int = 0,
        max_date: int = 0,
    ) -> Union["types.Error", "types.FoundMessages"]:
        r"""Searches for messages in all chats except secret chats\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing \(date, chat\_id, message\_id\)\)\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                Chat list in which to search messages; pass null to search in all chats regardless of their chat list\. Only Main and Archive chat lists are supported

            query (:class:`str`):
                Query to search for

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            filter (:class:`"types.SearchMessagesFilter"`):
                Additional filter for messages to search; pass null to search for all messages\. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function

            chat_type_filter (:class:`"types.SearchMessagesChatTypeFilter"`):
                Additional filter for type of the chat of the searched messages; pass null to search for messages in all chats

            min_date (:class:`int`):
                If not 0, the minimum date of the messages to return

            max_date (:class:`int`):
                If not 0, the maximum date of the messages to return

        Returns:
            :class:`~pytdbot.types.FoundMessages`
        """

        return await self.invoke(
            {
                "@type": "searchMessages",
                "chat_list": chat_list,
                "query": query,
                "offset": offset,
                "limit": limit,
                "filter": filter,
                "chat_type_filter": chat_type_filter,
                "min_date": min_date,
                "max_date": max_date,
            }
        )

    async def searchSecretMessages(
        self,
        chat_id: int = 0,
        query: str = "",
        offset: str = "",
        limit: int = 0,
        filter: "types.SearchMessagesFilter" = None,
    ) -> Union["types.Error", "types.FoundMessages"]:
        r"""Searches for messages in secret chats\. Returns the results in reverse chronological order\. For optimal performance, the number of returned messages is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to search\. Specify 0 to search in all secret chats

            query (:class:`str`):
                Query to search for\. If empty, searchChatMessages must be used instead

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            filter (:class:`"types.SearchMessagesFilter"`):
                Additional filter for messages to search; pass null to search for all messages

        Returns:
            :class:`~pytdbot.types.FoundMessages`
        """

        return await self.invoke(
            {
                "@type": "searchSecretMessages",
                "chat_id": chat_id,
                "query": query,
                "offset": offset,
                "limit": limit,
                "filter": filter,
            }
        )

    async def searchSavedMessages(
        self,
        saved_messages_topic_id: int = 0,
        tag: "types.ReactionType" = None,
        query: str = "",
        from_message_id: int = 0,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundChatMessages"]:
        r"""Searches for messages tagged by the given reaction and with the given words in the Saved Messages chat; for Telegram Premium users only\. Returns the results in reverse chronological order, i\.e\. in order of decreasing message\_id\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            saved_messages_topic_id (:class:`int`):
                If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages

            tag (:class:`"types.ReactionType"`):
                Tag to search for; pass null to return all suitable messages

            query (:class:`str`):
                Query to search for

            from_message_id (:class:`int`):
                Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message

            offset (:class:`int`):
                Specify 0 to get results from exactly the message from\_message\_id or a negative offset to get the specified message and some newer messages

            limit (:class:`int`):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundChatMessages`
        """

        return await self.invoke(
            {
                "@type": "searchSavedMessages",
                "saved_messages_topic_id": saved_messages_topic_id,
                "tag": tag,
                "query": query,
                "from_message_id": from_message_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def searchCallMessages(
        self, offset: str = "", limit: int = 0, only_missed: bool = False
    ) -> Union["types.Error", "types.FoundMessages"]:
        r"""Searches for call messages\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib

        Parameters:
            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_missed (:class:`bool`):
                Pass true to search only for messages with missed/declined calls

        Returns:
            :class:`~pytdbot.types.FoundMessages`
        """

        return await self.invoke(
            {
                "@type": "searchCallMessages",
                "offset": offset,
                "limit": limit,
                "only_missed": only_missed,
            }
        )

    async def searchOutgoingDocumentMessages(
        self, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.FoundMessages"]:
        r"""Searches for outgoing messages with content of the type messageDocument in all chats except secret chats\. Returns the results in reverse chronological order

        Parameters:
            query (:class:`str`):
                Query to search for in document file name and message caption

            limit (:class:`int`):
                The maximum number of messages to be returned; up to 100

        Returns:
            :class:`~pytdbot.types.FoundMessages`
        """

        return await self.invoke(
            {"@type": "searchOutgoingDocumentMessages", "query": query, "limit": limit}
        )

    async def searchPublicMessagesByTag(
        self, tag: str = "", offset: str = "", limit: int = 0
    ) -> Union["types.Error", "types.FoundMessages"]:
        r"""Searches for public channel posts containing the given hashtag or cashtag\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            tag (:class:`str`):
                Hashtag or cashtag to search for

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundMessages`
        """

        return await self.invoke(
            {
                "@type": "searchPublicMessagesByTag",
                "tag": tag,
                "offset": offset,
                "limit": limit,
            }
        )

    async def searchPublicStoriesByTag(
        self,
        story_sender_chat_id: int = 0,
        tag: str = "",
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundStories"]:
        r"""Searches for public stories containing the given hashtag or cashtag\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the stories to search for; pass 0 to search stories in all chats

            tag (:class:`str`):
                Hashtag or cashtag to search for

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of stories to be returned; up to 100\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundStories`
        """

        return await self.invoke(
            {
                "@type": "searchPublicStoriesByTag",
                "story_sender_chat_id": story_sender_chat_id,
                "tag": tag,
                "offset": offset,
                "limit": limit,
            }
        )

    async def searchPublicStoriesByLocation(
        self, address: "types.LocationAddress" = None, offset: str = "", limit: int = 0
    ) -> Union["types.Error", "types.FoundStories"]:
        r"""Searches for public stories by the given address location\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            address (:class:`"types.LocationAddress"`):
                Address of the location

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of stories to be returned; up to 100\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundStories`
        """

        return await self.invoke(
            {
                "@type": "searchPublicStoriesByLocation",
                "address": address,
                "offset": offset,
                "limit": limit,
            }
        )

    async def searchPublicStoriesByVenue(
        self,
        venue_provider: str = "",
        venue_id: str = "",
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundStories"]:
        r"""Searches for public stories from the given venue\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Parameters:
            venue_provider (:class:`str`):
                Provider of the venue

            venue_id (:class:`str`):
                Identifier of the venue in the provider database

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of stories to be returned; up to 100\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundStories`
        """

        return await self.invoke(
            {
                "@type": "searchPublicStoriesByVenue",
                "venue_provider": venue_provider,
                "venue_id": venue_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getSearchedForTags(
        self, tag_prefix: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Hashtags"]:
        r"""Returns recently searched for hashtags or cashtags by their prefix

        Parameters:
            tag_prefix (:class:`str`):
                Prefix of hashtags or cashtags to return

            limit (:class:`int`):
                The maximum number of items to be returned

        Returns:
            :class:`~pytdbot.types.Hashtags`
        """

        return await self.invoke(
            {"@type": "getSearchedForTags", "tag_prefix": tag_prefix, "limit": limit}
        )

    async def removeSearchedForTag(
        self, tag: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a hashtag or a cashtag from the list of recently searched for hashtags or cashtags

        Parameters:
            tag (:class:`str`):
                Hashtag or cashtag to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeSearchedForTag", "tag": tag})

    async def clearSearchedForTags(
        self, clear_cashtags: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of recently searched for hashtags or cashtags

        Parameters:
            clear_cashtags (:class:`bool`):
                Pass true to clear the list of recently searched for cashtags; otherwise, the list of recently searched for hashtags will be cleared

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "clearSearchedForTags", "clear_cashtags": clear_cashtags}
        )

    async def deleteAllCallMessages(
        self, revoke: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all call messages

        Parameters:
            revoke (:class:`bool`):
                Pass true to delete the messages for all users

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deleteAllCallMessages", "revoke": revoke})

    async def searchChatRecentLocationMessages(
        self, chat_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns information about the recent locations of chat members that were sent to the chat\. Returns up to 1 location message per user

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            limit (:class:`int`):
                The maximum number of messages to be returned

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "searchChatRecentLocationMessages",
                "chat_id": chat_id,
                "limit": limit,
            }
        )

    async def getChatMessageByDate(
        self, chat_id: int = 0, date: int = 0
    ) -> Union["types.Error", "types.Message"]:
        r"""Returns the last message sent in a chat no later than the specified date\. Returns a 404 error if such message doesn't exist

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            date (:class:`int`):
                Point in time \(Unix timestamp\) relative to which to search for messages

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {"@type": "getChatMessageByDate", "chat_id": chat_id, "date": date}
        )

    async def getChatSparseMessagePositions(
        self,
        chat_id: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        from_message_id: int = 0,
        limit: int = 0,
        saved_messages_topic_id: int = 0,
    ) -> Union["types.Error", "types.MessagePositions"]:
        r"""Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to return information about message positions

            filter (:class:`"types.SearchMessagesFilter"`):
                Filter for message content\. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (:class:`int`):
                The message identifier from which to return information about message positions

            limit (:class:`int`):
                The expected number of message positions to be returned; 50\-2000\. A smaller number of positions can be returned, if there are not enough appropriate messages

            saved_messages_topic_id (:class:`int`):
                If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages

        Returns:
            :class:`~pytdbot.types.MessagePositions`
        """

        return await self.invoke(
            {
                "@type": "getChatSparseMessagePositions",
                "chat_id": chat_id,
                "filter": filter,
                "from_message_id": from_message_id,
                "limit": limit,
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def getChatMessageCalendar(
        self,
        chat_id: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        from_message_id: int = 0,
        saved_messages_topic_id: int = 0,
    ) -> Union["types.Error", "types.MessageCalendar"]:
        r"""Returns information about the next messages of the specified type in the chat split by days\. Returns the results in reverse chronological order\. Can return partial result for the last returned day\. Behavior of this method depends on the value of the option \"utc\_time\_offset\"

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to return information about messages

            filter (:class:`"types.SearchMessagesFilter"`):
                Filter for message content\. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (:class:`int`):
                The message identifier from which to return information about messages; use 0 to get results from the last message

            saved_messages_topic_id (:class:`int`):
                If not0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages, or for chats other than Saved Messages

        Returns:
            :class:`~pytdbot.types.MessageCalendar`
        """

        return await self.invoke(
            {
                "@type": "getChatMessageCalendar",
                "chat_id": chat_id,
                "filter": filter,
                "from_message_id": from_message_id,
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def getChatMessageCount(
        self,
        chat_id: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        saved_messages_topic_id: int = 0,
        return_local: bool = False,
    ) -> Union["types.Error", "types.Count"]:
        r"""Returns approximate number of messages of the specified type in the chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to count messages

            filter (:class:`"types.SearchMessagesFilter"`):
                Filter for message content; searchMessagesFilterEmpty is unsupported in this function

            saved_messages_topic_id (:class:`int`):
                If not 0, only messages in the specified Saved Messages topic will be counted; pass 0 to count all messages, or for chats other than Saved Messages

            return_local (:class:`bool`):
                Pass true to get the number of messages without sending network requests, or \-1 if the number of messages is unknown locally

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke(
            {
                "@type": "getChatMessageCount",
                "chat_id": chat_id,
                "filter": filter,
                "saved_messages_topic_id": saved_messages_topic_id,
                "return_local": return_local,
            }
        )

    async def getChatMessagePosition(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        filter: "types.SearchMessagesFilter" = None,
        message_thread_id: int = 0,
        saved_messages_topic_id: int = 0,
    ) -> Union["types.Error", "types.Count"]:
        r"""Returns approximate 1\-based position of a message among messages, which can be found by the specified filter in the chat\. Cannot be used in secret chats

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which to find message position

            message_id (:class:`int`):
                Message identifier

            filter (:class:`"types.SearchMessagesFilter"`):
                Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function

            message_thread_id (:class:`int`):
                If not 0, only messages in the specified thread will be considered; supergroups only

            saved_messages_topic_id (:class:`int`):
                If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all relevant messages, or for chats other than Saved Messages

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke(
            {
                "@type": "getChatMessagePosition",
                "chat_id": chat_id,
                "message_id": message_id,
                "filter": filter,
                "message_thread_id": message_thread_id,
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def getChatScheduledMessages(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Messages"]:
        r"""Returns all scheduled messages in a chat\. The messages are returned in reverse chronological order \(i\.e\., in order of decreasing message\_id\)

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {"@type": "getChatScheduledMessages", "chat_id": chat_id}
        )

    async def getChatSponsoredMessages(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.SponsoredMessages"]:
        r"""Returns sponsored messages to be shown in a chat; for channel chats and chats with bots only

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

        Returns:
            :class:`~pytdbot.types.SponsoredMessages`
        """

        return await self.invoke(
            {"@type": "getChatSponsoredMessages", "chat_id": chat_id}
        )

    async def clickChatSponsoredMessage(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        is_media_click: bool = False,
        from_fullscreen: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the user opened the sponsored chat via the button, the name, the chat photo, a mention in the sponsored message text, or the media in the sponsored message

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the sponsored message

            message_id (:class:`int`):
                Identifier of the sponsored message

            is_media_click (:class:`bool`):
                Pass true if the media was clicked in the sponsored message

            from_fullscreen (:class:`bool`):
                Pass true if the user expanded the video from the sponsored message fullscreen before the click

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clickChatSponsoredMessage",
                "chat_id": chat_id,
                "message_id": message_id,
                "is_media_click": is_media_click,
                "from_fullscreen": from_fullscreen,
            }
        )

    async def reportChatSponsoredMessage(
        self, chat_id: int = 0, message_id: int = 0, option_id: bytes = b""
    ) -> Union["types.Error", "types.ReportSponsoredResult"]:
        r"""Reports a sponsored message to Telegram moderators

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the sponsored message

            message_id (:class:`int`):
                Identifier of the sponsored message

            option_id (:class:`bytes`):
                Option identifier chosen by the user; leave empty for the initial request

        Returns:
            :class:`~pytdbot.types.ReportSponsoredResult`
        """

        return await self.invoke(
            {
                "@type": "reportChatSponsoredMessage",
                "chat_id": chat_id,
                "message_id": message_id,
                "option_id": option_id,
            }
        )

    async def getSearchSponsoredChats(
        self, query: str = ""
    ) -> Union["types.Error", "types.SponsoredChats"]:
        r"""Returns sponsored chats to be shown in the search results

        Parameters:
            query (:class:`str`):
                Query the user searches for

        Returns:
            :class:`~pytdbot.types.SponsoredChats`
        """

        return await self.invoke({"@type": "getSearchSponsoredChats", "query": query})

    async def viewSponsoredChat(
        self, sponsored_chat_unique_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the user fully viewed a sponsored chat

        Parameters:
            sponsored_chat_unique_id (:class:`int`):
                Unique identifier of the sponsored chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "viewSponsoredChat",
                "sponsored_chat_unique_id": sponsored_chat_unique_id,
            }
        )

    async def openSponsoredChat(
        self, sponsored_chat_unique_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the user opened a sponsored chat

        Parameters:
            sponsored_chat_unique_id (:class:`int`):
                Unique identifier of the sponsored chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "openSponsoredChat",
                "sponsored_chat_unique_id": sponsored_chat_unique_id,
            }
        )

    async def reportSponsoredChat(
        self, sponsored_chat_unique_id: int = 0, option_id: bytes = b""
    ) -> Union["types.Error", "types.ReportSponsoredResult"]:
        r"""Reports a sponsored chat to Telegram moderators

        Parameters:
            sponsored_chat_unique_id (:class:`int`):
                Unique identifier of the sponsored chat

            option_id (:class:`bytes`):
                Option identifier chosen by the user; leave empty for the initial request

        Returns:
            :class:`~pytdbot.types.ReportSponsoredResult`
        """

        return await self.invoke(
            {
                "@type": "reportSponsoredChat",
                "sponsored_chat_unique_id": sponsored_chat_unique_id,
                "option_id": option_id,
            }
        )

    async def removeNotification(
        self, notification_group_id: int = 0, notification_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes an active notification from notification list\. Needs to be called only if the notification is removed by the current user

        Parameters:
            notification_group_id (:class:`int`):
                Identifier of notification group to which the notification belongs

            notification_id (:class:`int`):
                Identifier of removed notification

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeNotification",
                "notification_group_id": notification_group_id,
                "notification_id": notification_id,
            }
        )

    async def removeNotificationGroup(
        self, notification_group_id: int = 0, max_notification_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a group of active notifications\. Needs to be called only if the notification group is removed by the current user

        Parameters:
            notification_group_id (:class:`int`):
                Notification group identifier

            max_notification_id (:class:`int`):
                The maximum identifier of removed notifications

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeNotificationGroup",
                "notification_group_id": notification_group_id,
                "max_notification_id": max_notification_id,
            }
        )

    async def getMessageLink(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        media_timestamp: int = 0,
        for_album: bool = False,
        in_message_thread: bool = False,
    ) -> Union["types.Error", "types.MessageLink"]:
        r"""Returns an HTTPS link to a message in a chat\. Available only if messageProperties\.can\_get\_link, or if messageProperties\.can\_get\_media\_timestamp\_links and a media timestamp link is generated\. This is an offline method

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            media_timestamp (:class:`int`):
                If not 0, timestamp from which the video/audio/video note/voice note/story playing must start, in seconds\. The media can be in the message content or in its link preview

            for_album (:class:`bool`):
                Pass true to create a link for the whole media album

            in_message_thread (:class:`bool`):
                Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic

        Returns:
            :class:`~pytdbot.types.MessageLink`
        """

        return await self.invoke(
            {
                "@type": "getMessageLink",
                "chat_id": chat_id,
                "message_id": message_id,
                "media_timestamp": media_timestamp,
                "for_album": for_album,
                "in_message_thread": in_message_thread,
            }
        )

    async def getMessageEmbeddingCode(
        self, chat_id: int = 0, message_id: int = 0, for_album: bool = False
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns an HTML code for embedding the message\. Available only if messageProperties\.can\_get\_embedding\_code

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            for_album (:class:`bool`):
                Pass true to return an HTML code for embedding of the whole media album

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getMessageEmbeddingCode",
                "chat_id": chat_id,
                "message_id": message_id,
                "for_album": for_album,
            }
        )

    async def getMessageLinkInfo(
        self, url: str = ""
    ) -> Union["types.Error", "types.MessageLinkInfo"]:
        r"""Returns information about a public or private message link\. Can be called for any internal link of the type internalLinkTypeMessage

        Parameters:
            url (:class:`str`):
                The message link

        Returns:
            :class:`~pytdbot.types.MessageLinkInfo`
        """

        return await self.invoke({"@type": "getMessageLinkInfo", "url": url})

    async def translateText(
        self, text: "types.FormattedText" = None, to_language_code: str = ""
    ) -> Union["types.Error", "types.FormattedText"]:
        r"""Translates a text to the given language\. If the current user is a Telegram Premium user, then text formatting is preserved

        Parameters:
            text (:class:`"types.FormattedText"`):
                Text to translate

            to_language_code (:class:`str`):
                Language code of the language to which the message is translated\. Must be one of \"af\", \"sq\", \"am\", \"ar\", \"hy\", \"az\", \"eu\", \"be\", \"bn\", \"bs\", \"bg\", \"ca\", \"ceb\", \"zh\-CN\", \"zh\", \"zh\-Hans\", \"zh\-TW\", \"zh\-Hant\", \"co\", \"hr\", \"cs\", \"da\", \"nl\", \"en\", \"eo\", \"et\", \"fi\", \"fr\", \"fy\", \"gl\", \"ka\", \"de\", \"el\", \"gu\", \"ht\", \"ha\", \"haw\", \"he\", \"iw\", \"hi\", \"hmn\", \"hu\", \"is\", \"ig\", \"id\", \"in\", \"ga\", \"it\", \"ja\", \"jv\", \"kn\", \"kk\", \"km\", \"rw\", \"ko\", \"ku\", \"ky\", \"lo\", \"la\", \"lv\", \"lt\", \"lb\", \"mk\", \"mg\", \"ms\", \"ml\", \"mt\", \"mi\", \"mr\", \"mn\", \"my\", \"ne\", \"no\", \"ny\", \"or\", \"ps\", \"fa\", \"pl\", \"pt\", \"pa\", \"ro\", \"ru\", \"sm\", \"gd\", \"sr\", \"st\", \"sn\", \"sd\", \"si\", \"sk\", \"sl\", \"so\", \"es\", \"su\", \"sw\", \"sv\", \"tl\", \"tg\", \"ta\", \"tt\", \"te\", \"th\", \"tr\", \"tk\", \"uk\", \"ur\", \"ug\", \"uz\", \"vi\", \"cy\", \"xh\", \"yi\", \"ji\", \"yo\", \"zu\"

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        return await self.invoke(
            {
                "@type": "translateText",
                "text": text,
                "to_language_code": to_language_code,
            }
        )

    async def translateMessageText(
        self, chat_id: int = 0, message_id: int = 0, to_language_code: str = ""
    ) -> Union["types.Error", "types.FormattedText"]:
        r"""Extracts text or caption of the given message and translates it to the given language\. If the current user is a Telegram Premium user, then text formatting is preserved

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            to_language_code (:class:`str`):
                Language code of the language to which the message is translated\. Must be one of \"af\", \"sq\", \"am\", \"ar\", \"hy\", \"az\", \"eu\", \"be\", \"bn\", \"bs\", \"bg\", \"ca\", \"ceb\", \"zh\-CN\", \"zh\", \"zh\-Hans\", \"zh\-TW\", \"zh\-Hant\", \"co\", \"hr\", \"cs\", \"da\", \"nl\", \"en\", \"eo\", \"et\", \"fi\", \"fr\", \"fy\", \"gl\", \"ka\", \"de\", \"el\", \"gu\", \"ht\", \"ha\", \"haw\", \"he\", \"iw\", \"hi\", \"hmn\", \"hu\", \"is\", \"ig\", \"id\", \"in\", \"ga\", \"it\", \"ja\", \"jv\", \"kn\", \"kk\", \"km\", \"rw\", \"ko\", \"ku\", \"ky\", \"lo\", \"la\", \"lv\", \"lt\", \"lb\", \"mk\", \"mg\", \"ms\", \"ml\", \"mt\", \"mi\", \"mr\", \"mn\", \"my\", \"ne\", \"no\", \"ny\", \"or\", \"ps\", \"fa\", \"pl\", \"pt\", \"pa\", \"ro\", \"ru\", \"sm\", \"gd\", \"sr\", \"st\", \"sn\", \"sd\", \"si\", \"sk\", \"sl\", \"so\", \"es\", \"su\", \"sw\", \"sv\", \"tl\", \"tg\", \"ta\", \"tt\", \"te\", \"th\", \"tr\", \"tk\", \"uk\", \"ur\", \"ug\", \"uz\", \"vi\", \"cy\", \"xh\", \"yi\", \"ji\", \"yo\", \"zu\"

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        return await self.invoke(
            {
                "@type": "translateMessageText",
                "chat_id": chat_id,
                "message_id": message_id,
                "to_language_code": to_language_code,
            }
        )

    async def recognizeSpeech(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Recognizes speech in a video note or a voice note message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_recognize\_speech to check whether the message is suitable

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "recognizeSpeech", "chat_id": chat_id, "message_id": message_id}
        )

    async def rateSpeechRecognition(
        self, chat_id: int = 0, message_id: int = 0, is_good: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Rates recognized speech in a video note or a voice note message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            is_good (:class:`bool`):
                Pass true if the speech recognition is good

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "rateSpeechRecognition",
                "chat_id": chat_id,
                "message_id": message_id,
                "is_good": is_good,
            }
        )

    async def getChatAvailableMessageSenders(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatMessageSenders"]:
        r"""Returns the list of message sender identifiers, which can be used to send messages in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatMessageSenders`
        """

        return await self.invoke(
            {"@type": "getChatAvailableMessageSenders", "chat_id": chat_id}
        )

    async def setChatMessageSender(
        self, chat_id: int = 0, message_sender_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Selects a message sender to send messages in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_sender_id (:class:`"types.MessageSender"`):
                New message sender for the chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatMessageSender",
                "chat_id": chat_id,
                "message_sender_id": message_sender_id,
            }
        )

    async def sendMessage(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        options: "types.MessageSendOptions" = None,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Message"]:
        r"""Sends a message\. Returns the sent message

        Parameters:
            chat_id (:class:`int`):
                Target chat

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the message will be sent

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message or story to be replied; pass null if none

            options (:class:`"types.MessageSendOptions"`):
                Options to be used to send the message; pass null to use default options

            reply_markup (:class:`"types.ReplyMarkup"`):
                Markup for replying to the message; pass null if none; for bots only

            input_message_content (:class:`"types.InputMessageContent"`):
                The content of the message to be sent

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "sendMessage",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "reply_to": reply_to,
                "options": options,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def sendMessageAlbum(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        options: "types.MessageSendOptions" = None,
        input_message_contents: List["types.InputMessageContent"] = None,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Sends 2\-10 messages grouped together into an album\. Currently, only audio, document, photo and video messages can be grouped into an album\. Documents and audio files can be only grouped in an album with messages of the same type\. Returns sent messages

        Parameters:
            chat_id (:class:`int`):
                Target chat

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the messages will be sent

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message or story to be replied; pass null if none

            options (:class:`"types.MessageSendOptions"`):
                Options to be used to send the messages; pass null to use default options

            input_message_contents (:class:`List["types.InputMessageContent"]`):
                Contents of messages to be sent\. At most 10 messages can be added to an album\. All messages must have the same value of show\_caption\_above\_media

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "sendMessageAlbum",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "reply_to": reply_to,
                "options": options,
                "input_message_contents": input_message_contents,
            }
        )

    async def sendBotStartMessage(
        self, bot_user_id: int = 0, chat_id: int = 0, parameter: str = ""
    ) -> Union["types.Error", "types.Message"]:
        r"""Invites a bot to a chat \(if it is not yet a member\) and sends it the /start command; requires can\_invite\_users member right\. Bots can't be invited to a private chat other than the chat with the bot\. Bots can't be invited to channels \(although they can be added as admins\) and secret chats\. Returns the sent message

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the bot

            chat_id (:class:`int`):
                Identifier of the target chat

            parameter (:class:`str`):
                A hidden parameter sent to the bot for deep linking purposes \(https://core\.telegram\.org/bots\#deep\-linking\)

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "sendBotStartMessage",
                "bot_user_id": bot_user_id,
                "chat_id": chat_id,
                "parameter": parameter,
            }
        )

    async def sendInlineQueryResultMessage(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        options: "types.MessageSendOptions" = None,
        query_id: int = 0,
        result_id: str = "",
        hide_via_bot: bool = False,
    ) -> Union["types.Error", "types.Message"]:
        r"""Sends the result of an inline query as a message\. Returns the sent message\. Always clears a chat draft message

        Parameters:
            chat_id (:class:`int`):
                Target chat

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the message will be sent

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message or story to be replied; pass null if none

            options (:class:`"types.MessageSendOptions"`):
                Options to be used to send the message; pass null to use default options

            query_id (:class:`int`):
                Identifier of the inline query

            result_id (:class:`str`):
                Identifier of the inline query result

            hide_via_bot (:class:`bool`):
                Pass true to hide the bot, via which the message is sent\. Can be used only for bots getOption\(\"animation\_search\_bot\_username\"\), getOption\(\"photo\_search\_bot\_username\"\), and getOption\(\"venue\_search\_bot\_username\"\)

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "sendInlineQueryResultMessage",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "reply_to": reply_to,
                "options": options,
                "query_id": query_id,
                "result_id": result_id,
                "hide_via_bot": hide_via_bot,
            }
        )

    async def forwardMessages(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        from_chat_id: int = 0,
        message_ids: List[int] = None,
        options: "types.MessageSendOptions" = None,
        send_copy: bool = False,
        remove_caption: bool = False,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Forwards previously sent messages\. Returns the forwarded messages in the same order as the message identifiers passed in message\_ids\. If a message can't be forwarded, null will be returned instead of the message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which to forward messages

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the message will be sent; for forum threads only

            from_chat_id (:class:`int`):
                Identifier of the chat from which to forward messages

            message_ids (:class:`List[int]`):
                Identifiers of the messages to forward\. Message identifiers must be in a strictly increasing order\. At most 100 messages can be forwarded simultaneously\. A message can be forwarded only if messageProperties\.can\_be\_forwarded

            options (:class:`"types.MessageSendOptions"`):
                Options to be used to send the messages; pass null to use default options

            send_copy (:class:`bool`):
                Pass true to copy content of the messages without reference to the original sender\. Always true if the messages are forwarded to a secret chat or are local\. Use messageProperties\.can\_be\_saved and messageProperties\.can\_be\_copied\_to\_secret\_chat to check whether the message is suitable

            remove_caption (:class:`bool`):
                Pass true to remove media captions of message copies\. Ignored if send\_copy is false

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "forwardMessages",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "from_chat_id": from_chat_id,
                "message_ids": message_ids,
                "options": options,
                "send_copy": send_copy,
                "remove_caption": remove_caption,
            }
        )

    async def sendQuickReplyShortcutMessages(
        self, chat_id: int = 0, shortcut_id: int = 0, sending_id: int = 0
    ) -> Union["types.Error", "types.Messages"]:
        r"""Sends messages from a quick reply shortcut\. Requires Telegram Business subscription\. Can't be used to send paid messages

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which to send messages\. The chat must be a private chat with a regular user

            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut

            sending_id (:class:`int`):
                Non\-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "sendQuickReplyShortcutMessages",
                "chat_id": chat_id,
                "shortcut_id": shortcut_id,
                "sending_id": sending_id,
            }
        )

    async def resendMessages(
        self,
        chat_id: int = 0,
        message_ids: List[int] = None,
        quote: "types.InputTextQuote" = None,
        paid_message_star_count: int = 0,
    ) -> Union["types.Error", "types.Messages"]:
        r"""Resends messages which failed to send\. Can be called only for messages for which messageSendingStateFailed\.can\_retry is true and after specified in messageSendingStateFailed\.retry\_after time passed\. If a message is re\-sent, the corresponding failed to send message is deleted\. Returns the sent messages in the same order as the message identifiers passed in message\_ids\. If a message can't be re\-sent, null will be returned instead of the message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to send messages

            message_ids (:class:`List[int]`):
                Identifiers of the messages to resend\. Message identifiers must be in a strictly increasing order

            quote (:class:`"types.InputTextQuote"`):
                New manually chosen quote from the message to be replied; pass null if none\. Ignored if more than one message is re\-sent, or if messageSendingStateFailed\.need\_another\_reply\_quote \=\= false

            paid_message_star_count (:class:`int`):
                The number of Telegram Stars the user agreed to pay to send the messages\. Ignored if messageSendingStateFailed\.required\_paid\_message\_star\_count \=\= 0

        Returns:
            :class:`~pytdbot.types.Messages`
        """

        return await self.invoke(
            {
                "@type": "resendMessages",
                "chat_id": chat_id,
                "message_ids": message_ids,
                "quote": quote,
                "paid_message_star_count": paid_message_star_count,
            }
        )

    async def addLocalMessage(
        self,
        chat_id: int = 0,
        sender_id: "types.MessageSender" = None,
        reply_to: "types.InputMessageReplyTo" = None,
        disable_notification: bool = False,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Message"]:
        r"""Adds a local message to a chat\. The message is persistent across application restarts only if the message database is used\. Returns the added message

        Parameters:
            chat_id (:class:`int`):
                Target chat

            sender_id (:class:`"types.MessageSender"`):
                Identifier of the sender of the message

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message or story to be replied; pass null if none

            disable_notification (:class:`bool`):
                Pass true to disable notification for the message

            input_message_content (:class:`"types.InputMessageContent"`):
                The content of the message to be added

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "addLocalMessage",
                "chat_id": chat_id,
                "sender_id": sender_id,
                "reply_to": reply_to,
                "disable_notification": disable_notification,
                "input_message_content": input_message_content,
            }
        )

    async def deleteMessages(
        self, chat_id: int = 0, message_ids: List[int] = None, revoke: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes messages

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_ids (:class:`List[int]`):
                Identifiers of the messages to be deleted\. Use messageProperties\.can\_be\_deleted\_only\_for\_self and messageProperties\.can\_be\_deleted\_for\_all\_users to get suitable messages

            revoke (:class:`bool`):
                Pass true to delete messages for all chat members\. Always true for supergroups, channels and secret chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteMessages",
                "chat_id": chat_id,
                "message_ids": message_ids,
                "revoke": revoke,
            }
        )

    async def deleteChatMessagesBySender(
        self, chat_id: int = 0, sender_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages sent by the specified message sender in a chat\. Supported only for supergroups; requires can\_delete\_messages administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            sender_id (:class:`"types.MessageSender"`):
                Identifier of the sender of messages to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatMessagesBySender",
                "chat_id": chat_id,
                "sender_id": sender_id,
            }
        )

    async def deleteChatMessagesByDate(
        self,
        chat_id: int = 0,
        min_date: int = 0,
        max_date: int = 0,
        revoke: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages between the specified dates in a chat\. Supported only for private chats and basic groups\. Messages sent in the last 30 seconds will not be deleted

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            min_date (:class:`int`):
                The minimum date of the messages to delete

            max_date (:class:`int`):
                The maximum date of the messages to delete

            revoke (:class:`bool`):
                Pass true to delete chat messages for all users; private chats only

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatMessagesByDate",
                "chat_id": chat_id,
                "min_date": min_date,
                "max_date": max_date,
                "revoke": revoke,
            }
        )

    async def editMessageText(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Message"]:
        r"""Edits the text of a message \(or a text of a game message\)\. Returns the edited message after the edit is completed on the server side

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_be\_edited to check whether the message can be edited

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            input_message_content (:class:`"types.InputMessageContent"`):
                New text content of the message\. Must be of type inputMessageText

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "editMessageText",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editMessageLiveLocation(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        location: "types.Location" = None,
        live_period: int = 0,
        heading: int = 0,
        proximity_alert_radius: int = 0,
    ) -> Union["types.Error", "types.Message"]:
        r"""Edits the message content of a live location\. Messages can be edited for a limited period of time specified in the live location\. Returns the edited message after the edit is completed on the server side

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_be\_edited to check whether the message can be edited

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            location (:class:`"types.Location"`):
                New location content of the message; pass null to stop sharing the live location

            live_period (:class:`int`):
                New time relative to the message send date, for which the location can be updated, in seconds\. If 0x7FFFFFFF specified, then the location can be updated forever\. Otherwise, must not exceed the current live\_period by more than a day, and the live location expiration date must remain in the next 90 days\. Pass 0 to keep the current live\_period

            heading (:class:`int`):
                The new direction in which the location moves, in degrees; 1\-360\. Pass 0 if unknown

            proximity_alert_radius (:class:`int`):
                The new maximum distance for proximity alerts, in meters \(0\-100000\)\. Pass 0 if the notification is disabled

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "editMessageLiveLocation",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "location": location,
                "live_period": live_period,
                "heading": heading,
                "proximity_alert_radius": proximity_alert_radius,
            }
        )

    async def editMessageMedia(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Message"]:
        r"""Edits the media content of a message, including message caption\. If only the caption needs to be edited, use editMessageCaption instead\. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa\. Returns the edited message after the edit is completed on the server side

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_edit\_media to check whether the message can be edited

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            input_message_content (:class:`"types.InputMessageContent"`):
                New content of the message\. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "editMessageMedia",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editMessageCaption(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        caption: "types.FormattedText" = None,
        show_caption_above_media: bool = False,
    ) -> Union["types.Error", "types.Message"]:
        r"""Edits the message content caption\. Returns the edited message after the edit is completed on the server side

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_be\_edited to check whether the message can be edited

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            caption (:class:`"types.FormattedText"`):
                New message content caption; 0\-getOption\(\"message\_caption\_length\_max\"\) characters; pass null to remove caption

            show_caption_above_media (:class:`bool`):
                Pass true to show the caption above the media; otherwise, the caption will be shown below the media\. May be true only for animation, photo, and video messages

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "editMessageCaption",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "caption": caption,
                "show_caption_above_media": show_caption_above_media,
            }
        )

    async def editMessageReplyMarkup(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
    ) -> Union["types.Error", "types.Message"]:
        r"""Edits the message reply markup; for bots only\. Returns the edited message after the edit is completed on the server side

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_be\_edited to check whether the message can be edited

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "editMessageReplyMarkup",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
            }
        )

    async def editInlineMessageText(
        self,
        inline_message_id: str = "",
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the text of an inline text or game message sent via a bot; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            input_message_content (:class:`"types.InputMessageContent"`):
                New text content of the message\. Must be of type inputMessageText

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editInlineMessageText",
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editInlineMessageLiveLocation(
        self,
        inline_message_id: str = "",
        reply_markup: "types.ReplyMarkup" = None,
        location: "types.Location" = None,
        live_period: int = 0,
        heading: int = 0,
        proximity_alert_radius: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the content of a live location in an inline message sent via a bot; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            location (:class:`"types.Location"`):
                New location content of the message; pass null to stop sharing the live location

            live_period (:class:`int`):
                New time relative to the message send date, for which the location can be updated, in seconds\. If 0x7FFFFFFF specified, then the location can be updated forever\. Otherwise, must not exceed the current live\_period by more than a day, and the live location expiration date must remain in the next 90 days\. Pass 0 to keep the current live\_period

            heading (:class:`int`):
                The new direction in which the location moves, in degrees; 1\-360\. Pass 0 if unknown

            proximity_alert_radius (:class:`int`):
                The new maximum distance for proximity alerts, in meters \(0\-100000\)\. Pass 0 if the notification is disabled

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editInlineMessageLiveLocation",
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
                "location": location,
                "live_period": live_period,
                "heading": heading,
                "proximity_alert_radius": proximity_alert_radius,
            }
        )

    async def editInlineMessageMedia(
        self,
        inline_message_id: str = "",
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the media content of a message with a text, an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            input_message_content (:class:`"types.InputMessageContent"`):
                New content of the message\. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editInlineMessageMedia",
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editInlineMessageCaption(
        self,
        inline_message_id: str = "",
        reply_markup: "types.ReplyMarkup" = None,
        caption: "types.FormattedText" = None,
        show_caption_above_media: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the caption of an inline message sent via a bot; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            caption (:class:`"types.FormattedText"`):
                New message content caption; pass null to remove caption; 0\-getOption\(\"message\_caption\_length\_max\"\) characters

            show_caption_above_media (:class:`bool`):
                Pass true to show the caption above the media; otherwise, the caption will be shown below the media\. May be true only for animation, photo, and video messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editInlineMessageCaption",
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
                "caption": caption,
                "show_caption_above_media": show_caption_above_media,
            }
        )

    async def editInlineMessageReplyMarkup(
        self, inline_message_id: str = "", reply_markup: "types.ReplyMarkup" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the reply markup of an inline message sent via a bot; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editInlineMessageReplyMarkup",
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup,
            }
        )

    async def editMessageSchedulingState(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        scheduling_state: "types.MessageSchedulingState" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits the time when a scheduled message will be sent\. Scheduling state of all messages in the same album or forwarded together with the message will be also changed

        Parameters:
            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message\. Use messageProperties\.can\_edit\_scheduling\_state to check whether the message is suitable

            scheduling_state (:class:`"types.MessageSchedulingState"`):
                The new message scheduling state; pass null to send the message immediately\. Must be null for messages in the state messageSchedulingStateSendWhenVideoProcessed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editMessageSchedulingState",
                "chat_id": chat_id,
                "message_id": message_id,
                "scheduling_state": scheduling_state,
            }
        )

    async def setMessageFactCheck(
        self, chat_id: int = 0, message_id: int = 0, text: "types.FormattedText" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the fact\-check of a message\. Can be only used if messageProperties\.can\_set\_fact\_check \=\= true

        Parameters:
            chat_id (:class:`int`):
                The channel chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            text (:class:`"types.FormattedText"`):
                New text of the fact\-check; 0\-getOption\(\"fact\_check\_length\_max\"\) characters; pass null to remove it\. Only Bold, Italic, and TextUrl entities with https://t\.me/ links are supported

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setMessageFactCheck",
                "chat_id": chat_id,
                "message_id": message_id,
                "text": text,
            }
        )

    async def sendBusinessMessage(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        effect_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Sends a message on behalf of a business account; for bots only\. Returns the message after it was sent

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request

            chat_id (:class:`int`):
                Target chat

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message to be replied; pass null if none

            disable_notification (:class:`bool`):
                Pass true to disable notification for the message

            protect_content (:class:`bool`):
                Pass true if the content of the message must be protected from forwarding and saving

            effect_id (:class:`int`):
                Identifier of the effect to apply to the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                Markup for replying to the message; pass null if none

            input_message_content (:class:`"types.InputMessageContent"`):
                The content of the message to be sent

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "sendBusinessMessage",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "reply_to": reply_to,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "effect_id": effect_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def sendBusinessMessageAlbum(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        disable_notification: bool = False,
        protect_content: bool = False,
        effect_id: int = 0,
        input_message_contents: List["types.InputMessageContent"] = None,
    ) -> Union["types.Error", "types.BusinessMessages"]:
        r"""Sends 2\-10 messages grouped together into an album on behalf of a business account; for bots only\. Currently, only audio, document, photo and video messages can be grouped into an album\. Documents and audio files can be only grouped in an album with messages of the same type\. Returns sent messages

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request

            chat_id (:class:`int`):
                Target chat

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message to be replied; pass null if none

            disable_notification (:class:`bool`):
                Pass true to disable notification for the message

            protect_content (:class:`bool`):
                Pass true if the content of the message must be protected from forwarding and saving

            effect_id (:class:`int`):
                Identifier of the effect to apply to the message

            input_message_contents (:class:`List["types.InputMessageContent"]`):
                Contents of messages to be sent\. At most 10 messages can be added to an album\. All messages must have the same value of show\_caption\_above\_media

        Returns:
            :class:`~pytdbot.types.BusinessMessages`
        """

        return await self.invoke(
            {
                "@type": "sendBusinessMessageAlbum",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "reply_to": reply_to,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "effect_id": effect_id,
                "input_message_contents": input_message_contents,
            }
        )

    async def editBusinessMessageText(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Edits the text of a text or game message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            input_message_content (:class:`"types.InputMessageContent"`):
                New text content of the message\. Must be of type inputMessageText

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "editBusinessMessageText",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editBusinessMessageLiveLocation(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        location: "types.Location" = None,
        live_period: int = 0,
        heading: int = 0,
        proximity_alert_radius: int = 0,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Edits the content of a live location in a message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            location (:class:`"types.Location"`):
                New location content of the message; pass null to stop sharing the live location

            live_period (:class:`int`):
                New time relative to the message send date, for which the location can be updated, in seconds\. If 0x7FFFFFFF specified, then the location can be updated forever\. Otherwise, must not exceed the current live\_period by more than a day, and the live location expiration date must remain in the next 90 days\. Pass 0 to keep the current live\_period

            heading (:class:`int`):
                The new direction in which the location moves, in degrees; 1\-360\. Pass 0 if unknown

            proximity_alert_radius (:class:`int`):
                The new maximum distance for proximity alerts, in meters \(0\-100000\)\. Pass 0 if the notification is disabled

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "editBusinessMessageLiveLocation",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "location": location,
                "live_period": live_period,
                "heading": heading,
                "proximity_alert_radius": proximity_alert_radius,
            }
        )

    async def editBusinessMessageMedia(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Edits the media content of a message with a text, an animation, an audio, a document, a photo or a video in a message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

            input_message_content (:class:`"types.InputMessageContent"`):
                New content of the message\. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "editBusinessMessageMedia",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "input_message_content": input_message_content,
            }
        )

    async def editBusinessMessageCaption(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
        caption: "types.FormattedText" = None,
        show_caption_above_media: bool = False,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Edits the caption of a message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

            caption (:class:`"types.FormattedText"`):
                New message content caption; pass null to remove caption; 0\-getOption\(\"message\_caption\_length\_max\"\) characters

            show_caption_above_media (:class:`bool`):
                Pass true to show the caption above the media; otherwise, the caption will be shown below the media\. May be true only for animation, photo, and video messages

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "editBusinessMessageCaption",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
                "caption": caption,
                "show_caption_above_media": show_caption_above_media,
            }
        )

    async def editBusinessMessageReplyMarkup(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Edits the reply markup of a message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "editBusinessMessageReplyMarkup",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
            }
        )

    async def stopBusinessPoll(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
    ) -> Union["types.Error", "types.BusinessMessage"]:
        r"""Stops a poll sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message with the poll was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message containing the poll

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none

        Returns:
            :class:`~pytdbot.types.BusinessMessage`
        """

        return await self.invoke(
            {
                "@type": "stopBusinessPoll",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
            }
        )

    async def setBusinessMessageIsPinned(
        self,
        business_connection_id: str = "",
        chat_id: int = 0,
        message_id: int = 0,
        is_pinned: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Pins or unpins a message sent on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which the message was sent

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

            is_pinned (:class:`bool`):
                Pass true to pin the message, pass false to unpin it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessMessageIsPinned",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "is_pinned": is_pinned,
            }
        )

    async def readBusinessMessage(
        self, business_connection_id: str = "", chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reads a message on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection through which the message was received

            chat_id (:class:`int`):
                The chat the message belongs to

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "readBusinessMessage",
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def deleteBusinessMessages(
        self, business_connection_id: str = "", message_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes messages on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection through which the messages were received

            message_ids (:class:`List[int]`):
                Identifier of the messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteBusinessMessages",
                "business_connection_id": business_connection_id,
                "message_ids": message_ids,
            }
        )

    async def editBusinessStory(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        content: "types.InputStoryContent" = None,
        areas: "types.InputStoryAreas" = None,
        caption: "types.FormattedText" = None,
        privacy_settings: "types.StoryPrivacySettings" = None,
    ) -> Union["types.Error", "types.Story"]:
        r"""Changes a story sent by the bot on behalf of a business account; for bots only

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Identifier of the story to edit

            content (:class:`"types.InputStoryContent"`):
                New content of the story

            areas (:class:`"types.InputStoryAreas"`):
                New clickable rectangle areas to be shown on the story media

            caption (:class:`"types.FormattedText"`):
                New story caption

            privacy_settings (:class:`"types.StoryPrivacySettings"`):
                The new privacy settings for the story

        Returns:
            :class:`~pytdbot.types.Story`
        """

        return await self.invoke(
            {
                "@type": "editBusinessStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "content": content,
                "areas": areas,
                "caption": caption,
                "privacy_settings": privacy_settings,
            }
        )

    async def deleteBusinessStory(
        self, business_connection_id: str = "", story_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a story sent by the bot on behalf of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            story_id (:class:`int`):
                Identifier of the story to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteBusinessStory",
                "business_connection_id": business_connection_id,
                "story_id": story_id,
            }
        )

    async def setBusinessAccountName(
        self,
        business_connection_id: str = "",
        first_name: str = "",
        last_name: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the first and last name of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            first_name (:class:`str`):
                The new value of the first name for the business account; 1\-64 characters

            last_name (:class:`str`):
                The new value of the optional last name for the business account; 0\-64 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAccountName",
                "business_connection_id": business_connection_id,
                "first_name": first_name,
                "last_name": last_name,
            }
        )

    async def setBusinessAccountBio(
        self, business_connection_id: str = "", bio: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the bio of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            bio (:class:`str`):
                The new value of the bio; 0\-getOption\(\"bio\_length\_max\"\) characters without line feeds

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAccountBio",
                "business_connection_id": business_connection_id,
                "bio": bio,
            }
        )

    async def setBusinessAccountProfilePhoto(
        self,
        business_connection_id: str = "",
        photo: "types.InputChatPhoto" = None,
        is_public: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes a profile photo of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            photo (:class:`"types.InputChatPhoto"`):
                Profile photo to set; pass null to remove the photo

            is_public (:class:`bool`):
                Pass true to set the public photo, which will be visible even the main photo is hidden by privacy settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAccountProfilePhoto",
                "business_connection_id": business_connection_id,
                "photo": photo,
                "is_public": is_public,
            }
        )

    async def setBusinessAccountUsername(
        self, business_connection_id: str = "", username: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the editable username of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            username (:class:`str`):
                The new value of the username

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAccountUsername",
                "business_connection_id": business_connection_id,
                "username": username,
            }
        )

    async def setBusinessAccountGiftSettings(
        self, business_connection_id: str = "", settings: "types.GiftSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes settings for gift receiving of a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            settings (:class:`"types.GiftSettings"`):
                The new settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAccountGiftSettings",
                "business_connection_id": business_connection_id,
                "settings": settings,
            }
        )

    async def getBusinessAccountStarAmount(
        self, business_connection_id: str = ""
    ) -> Union["types.Error", "types.StarAmount"]:
        r"""Returns the amount of Telegram Stars owned by a business account; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

        Returns:
            :class:`~pytdbot.types.StarAmount`
        """

        return await self.invoke(
            {
                "@type": "getBusinessAccountStarAmount",
                "business_connection_id": business_connection_id,
            }
        )

    async def transferBusinessAccountStars(
        self, business_connection_id: str = "", star_count: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Transfer Telegram Stars from the business account to the business bot; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection

            star_count (:class:`int`):
                Number of Telegram Stars to transfer

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "transferBusinessAccountStars",
                "business_connection_id": business_connection_id,
                "star_count": star_count,
            }
        )

    async def checkQuickReplyShortcutName(
        self, name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks validness of a name for a quick reply shortcut\. Can be called synchronously

        Parameters:
            name (:class:`str`):
                The name of the shortcut; 1\-32 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "checkQuickReplyShortcutName", "name": name})

    async def loadQuickReplyShortcuts(self) -> Union["types.Error", "types.Ok"]:
        r"""Loads quick reply shortcuts created by the current user\. The loaded data will be sent through updateQuickReplyShortcut and updateQuickReplyShortcuts

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "loadQuickReplyShortcuts",
            }
        )

    async def setQuickReplyShortcutName(
        self, shortcut_id: int = 0, name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes name of a quick reply shortcut

        Parameters:
            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut

            name (:class:`str`):
                New name for the shortcut\. Use checkQuickReplyShortcutName to check its validness

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setQuickReplyShortcutName",
                "shortcut_id": shortcut_id,
                "name": name,
            }
        )

    async def deleteQuickReplyShortcut(
        self, shortcut_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a quick reply shortcut

        Parameters:
            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteQuickReplyShortcut", "shortcut_id": shortcut_id}
        )

    async def reorderQuickReplyShortcuts(
        self, shortcut_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of quick reply shortcuts

        Parameters:
            shortcut_ids (:class:`List[int]`):
                The new order of quick reply shortcuts

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "reorderQuickReplyShortcuts", "shortcut_ids": shortcut_ids}
        )

    async def loadQuickReplyShortcutMessages(
        self, shortcut_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Loads quick reply messages that can be sent by a given quick reply shortcut\. The loaded messages will be sent through updateQuickReplyShortcutMessages

        Parameters:
            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "loadQuickReplyShortcutMessages", "shortcut_id": shortcut_id}
        )

    async def deleteQuickReplyShortcutMessages(
        self, shortcut_id: int = 0, message_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes specified quick reply messages

        Parameters:
            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut to which the messages belong

            message_ids (:class:`List[int]`):
                Unique identifiers of the messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteQuickReplyShortcutMessages",
                "shortcut_id": shortcut_id,
                "message_ids": message_ids,
            }
        )

    async def addQuickReplyShortcutMessage(
        self,
        shortcut_name: str = "",
        reply_to_message_id: int = 0,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.QuickReplyMessage"]:
        r"""Adds a message to a quick reply shortcut\. If shortcut doesn't exist and there are less than getOption\(\"quick\_reply\_shortcut\_count\_max\"\) shortcuts, then a new shortcut is created\. The shortcut must not contain more than getOption\(\"quick\_reply\_shortcut\_message\_count\_max\"\) messages after adding the new message\. Returns the added message

        Parameters:
            shortcut_name (:class:`str`):
                Name of the target shortcut

            reply_to_message_id (:class:`int`):
                Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none

            input_message_content (:class:`"types.InputMessageContent"`):
                The content of the message to be added; inputMessagePoll, inputMessageForwarded and inputMessageLocation with live\_period aren't supported

        Returns:
            :class:`~pytdbot.types.QuickReplyMessage`
        """

        return await self.invoke(
            {
                "@type": "addQuickReplyShortcutMessage",
                "shortcut_name": shortcut_name,
                "reply_to_message_id": reply_to_message_id,
                "input_message_content": input_message_content,
            }
        )

    async def addQuickReplyShortcutInlineQueryResultMessage(
        self,
        shortcut_name: str = "",
        reply_to_message_id: int = 0,
        query_id: int = 0,
        result_id: str = "",
        hide_via_bot: bool = False,
    ) -> Union["types.Error", "types.QuickReplyMessage"]:
        r"""Adds a message to a quick reply shortcut via inline bot\. If shortcut doesn't exist and there are less than getOption\(\"quick\_reply\_shortcut\_count\_max\"\) shortcuts, then a new shortcut is created\. The shortcut must not contain more than getOption\(\"quick\_reply\_shortcut\_message\_count\_max\"\) messages after adding the new message\. Returns the added message

        Parameters:
            shortcut_name (:class:`str`):
                Name of the target shortcut

            reply_to_message_id (:class:`int`):
                Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none

            query_id (:class:`int`):
                Identifier of the inline query

            result_id (:class:`str`):
                Identifier of the inline query result

            hide_via_bot (:class:`bool`):
                Pass true to hide the bot, via which the message is sent\. Can be used only for bots getOption\(\"animation\_search\_bot\_username\"\), getOption\(\"photo\_search\_bot\_username\"\), and getOption\(\"venue\_search\_bot\_username\"\)

        Returns:
            :class:`~pytdbot.types.QuickReplyMessage`
        """

        return await self.invoke(
            {
                "@type": "addQuickReplyShortcutInlineQueryResultMessage",
                "shortcut_name": shortcut_name,
                "reply_to_message_id": reply_to_message_id,
                "query_id": query_id,
                "result_id": result_id,
                "hide_via_bot": hide_via_bot,
            }
        )

    async def addQuickReplyShortcutMessageAlbum(
        self,
        shortcut_name: str = "",
        reply_to_message_id: int = 0,
        input_message_contents: List["types.InputMessageContent"] = None,
    ) -> Union["types.Error", "types.QuickReplyMessages"]:
        r"""Adds 2\-10 messages grouped together into an album to a quick reply shortcut\. Currently, only audio, document, photo and video messages can be grouped into an album\. Documents and audio files can be only grouped in an album with messages of the same type\. Returns sent messages

        Parameters:
            shortcut_name (:class:`str`):
                Name of the target shortcut

            reply_to_message_id (:class:`int`):
                Identifier of a quick reply message in the same shortcut to be replied; pass 0 if none

            input_message_contents (:class:`List["types.InputMessageContent"]`):
                Contents of messages to be sent\. At most 10 messages can be added to an album\. All messages must have the same value of show\_caption\_above\_media

        Returns:
            :class:`~pytdbot.types.QuickReplyMessages`
        """

        return await self.invoke(
            {
                "@type": "addQuickReplyShortcutMessageAlbum",
                "shortcut_name": shortcut_name,
                "reply_to_message_id": reply_to_message_id,
                "input_message_contents": input_message_contents,
            }
        )

    async def readdQuickReplyShortcutMessages(
        self, shortcut_name: str = "", message_ids: List[int] = None
    ) -> Union["types.Error", "types.QuickReplyMessages"]:
        r"""Readds quick reply messages which failed to add\. Can be called only for messages for which messageSendingStateFailed\.can\_retry is true and after specified in messageSendingStateFailed\.retry\_after time passed\. If a message is readded, the corresponding failed to send message is deleted\. Returns the sent messages in the same order as the message identifiers passed in message\_ids\. If a message can't be readded, null will be returned instead of the message

        Parameters:
            shortcut_name (:class:`str`):
                Name of the target shortcut

            message_ids (:class:`List[int]`):
                Identifiers of the quick reply messages to readd\. Message identifiers must be in a strictly increasing order

        Returns:
            :class:`~pytdbot.types.QuickReplyMessages`
        """

        return await self.invoke(
            {
                "@type": "readdQuickReplyShortcutMessages",
                "shortcut_name": shortcut_name,
                "message_ids": message_ids,
            }
        )

    async def editQuickReplyMessage(
        self,
        shortcut_id: int = 0,
        message_id: int = 0,
        input_message_content: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Asynchronously edits the text, media or caption of a quick reply message\. Use quickReplyMessage\.can\_be\_edited to check whether a message can be edited\. Media message can be edited only to a media message\. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa

        Parameters:
            shortcut_id (:class:`int`):
                Unique identifier of the quick reply shortcut with the message

            message_id (:class:`int`):
                Identifier of the message

            input_message_content (:class:`"types.InputMessageContent"`):
                New content of the message\. Must be one of the following types: inputMessageText, inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editQuickReplyMessage",
                "shortcut_id": shortcut_id,
                "message_id": message_id,
                "input_message_content": input_message_content,
            }
        )

    async def getForumTopicDefaultIcons(self) -> Union["types.Error", "types.Stickers"]:
        r"""Returns the list of custom emoji, which can be used as forum topic icon by all users

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getForumTopicDefaultIcons",
            }
        )

    async def createForumTopic(
        self, chat_id: int = 0, name: str = "", icon: "types.ForumTopicIcon" = None
    ) -> Union["types.Error", "types.ForumTopicInfo"]:
        r"""Creates a topic in a forum supergroup chat; requires can\_manage\_topics administrator or can\_create\_topics member right in the supergroup

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            name (:class:`str`):
                Name of the topic; 1\-128 characters

            icon (:class:`"types.ForumTopicIcon"`):
                Icon of the topic\. Icon color must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F\. Telegram Premium users can use any custom emoji as topic icon, other users can use only a custom emoji returned by getForumTopicDefaultIcons

        Returns:
            :class:`~pytdbot.types.ForumTopicInfo`
        """

        return await self.invoke(
            {
                "@type": "createForumTopic",
                "chat_id": chat_id,
                "name": name,
                "icon": icon,
            }
        )

    async def editForumTopic(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        name: str = "",
        edit_icon_custom_emoji: bool = False,
        icon_custom_emoji_id: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits title and icon of a topic in a forum supergroup chat; requires can\_manage\_topics right in the supergroup unless the user is creator of the topic

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

            name (:class:`str`):
                New name of the topic; 0\-128 characters\. If empty, the previous topic name is kept

            edit_icon_custom_emoji (:class:`bool`):
                Pass true to edit the icon of the topic\. Icon of the General topic can't be edited

            icon_custom_emoji_id (:class:`int`):
                Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji\. Ignored if edit\_icon\_custom\_emoji is false\. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editForumTopic",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "name": name,
                "edit_icon_custom_emoji": edit_icon_custom_emoji,
                "icon_custom_emoji_id": icon_custom_emoji_id,
            }
        )

    async def getForumTopic(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.ForumTopic"]:
        r"""Returns information about a forum topic

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

        Returns:
            :class:`~pytdbot.types.ForumTopic`
        """

        return await self.invoke(
            {
                "@type": "getForumTopic",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def getForumTopicLink(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.MessageLink"]:
        r"""Returns an HTTPS link to a topic in a forum chat\. This is an offline method

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

        Returns:
            :class:`~pytdbot.types.MessageLink`
        """

        return await self.invoke(
            {
                "@type": "getForumTopicLink",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def getForumTopics(
        self,
        chat_id: int = 0,
        query: str = "",
        offset_date: int = 0,
        offset_message_id: int = 0,
        offset_message_thread_id: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.ForumTopics"]:
        r"""Returns found forum topics in a forum chat\. This is a temporary method for getting information about topic list from the server

        Parameters:
            chat_id (:class:`int`):
                Identifier of the forum chat

            query (:class:`str`):
                Query to search for in the forum topic's name

            offset_date (:class:`int`):
                The date starting from which the results need to be fetched\. Use 0 or any date in the future to get results from the last topic

            offset_message_id (:class:`int`):
                The message identifier of the last message in the last found topic, or 0 for the first request

            offset_message_thread_id (:class:`int`):
                The message thread identifier of the last found topic, or 0 for the first request

            limit (:class:`int`):
                The maximum number of forum topics to be returned; up to 100\. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.ForumTopics`
        """

        return await self.invoke(
            {
                "@type": "getForumTopics",
                "chat_id": chat_id,
                "query": query,
                "offset_date": offset_date,
                "offset_message_id": offset_message_id,
                "offset_message_thread_id": offset_message_thread_id,
                "limit": limit,
            }
        )

    async def setForumTopicNotificationSettings(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        notification_settings: "types.ChatNotificationSettings" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the notification settings of a forum topic

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

            notification_settings (:class:`"types.ChatNotificationSettings"`):
                New notification settings for the forum topic\. If the topic is muted for more than 366 days, it is considered to be muted forever

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setForumTopicNotificationSettings",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "notification_settings": notification_settings,
            }
        )

    async def toggleForumTopicIsClosed(
        self, chat_id: int = 0, message_thread_id: int = 0, is_closed: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a topic is closed in a forum supergroup chat; requires can\_manage\_topics right in the supergroup unless the user is creator of the topic

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

            is_closed (:class:`bool`):
                Pass true to close the topic; pass false to reopen it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleForumTopicIsClosed",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "is_closed": is_closed,
            }
        )

    async def toggleGeneralForumTopicIsHidden(
        self, chat_id: int = 0, is_hidden: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a General topic is hidden in a forum supergroup chat; requires can\_manage\_topics right in the supergroup

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            is_hidden (:class:`bool`):
                Pass true to hide and close the General topic; pass false to unhide it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGeneralForumTopicIsHidden",
                "chat_id": chat_id,
                "is_hidden": is_hidden,
            }
        )

    async def toggleForumTopicIsPinned(
        self, chat_id: int = 0, message_thread_id: int = 0, is_pinned: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the pinned state of a forum topic; requires can\_manage\_topics right in the supergroup\. There can be up to getOption\(\"pinned\_forum\_topic\_count\_max\"\) pinned forum topics

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

            is_pinned (:class:`bool`):
                Pass true to pin the topic; pass false to unpin it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleForumTopicIsPinned",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "is_pinned": is_pinned,
            }
        )

    async def setPinnedForumTopics(
        self, chat_id: int = 0, message_thread_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of pinned forum topics; requires can\_manage\_topics right in the supergroup

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_ids (:class:`List[int]`):
                The new list of pinned forum topics

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setPinnedForumTopics",
                "chat_id": chat_id,
                "message_thread_ids": message_thread_ids,
            }
        )

    async def deleteForumTopic(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all messages in a forum topic; requires can\_delete\_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier of the forum topic

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteForumTopic",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def getEmojiReaction(
        self, emoji: str = ""
    ) -> Union["types.Error", "types.EmojiReaction"]:
        r"""Returns information about an emoji reaction\. Returns a 404 error if the reaction is not found

        Parameters:
            emoji (:class:`str`):
                Text representation of the reaction

        Returns:
            :class:`~pytdbot.types.EmojiReaction`
        """

        return await self.invoke({"@type": "getEmojiReaction", "emoji": emoji})

    async def getCustomEmojiReactionAnimations(
        self,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns TGS stickers with generic animations for custom emoji reactions

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getCustomEmojiReactionAnimations",
            }
        )

    async def getMessageAvailableReactions(
        self, chat_id: int = 0, message_id: int = 0, row_size: int = 0
    ) -> Union["types.Error", "types.AvailableReactions"]:
        r"""Returns reactions, which can be added to a message\. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            row_size (:class:`int`):
                Number of reaction per row, 5\-25

        Returns:
            :class:`~pytdbot.types.AvailableReactions`
        """

        return await self.invoke(
            {
                "@type": "getMessageAvailableReactions",
                "chat_id": chat_id,
                "message_id": message_id,
                "row_size": row_size,
            }
        )

    async def clearRecentReactions(self) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of recently used reactions

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearRecentReactions",
            }
        )

    async def addMessageReaction(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reaction_type: "types.ReactionType" = None,
        is_big: bool = False,
        update_recent_reactions: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a reaction or a tag to a message\. Use getMessageAvailableReactions to receive the list of available reactions for the message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            reaction_type (:class:`"types.ReactionType"`):
                Type of the reaction to add\. Use addPendingPaidMessageReaction instead to add the paid reaction

            is_big (:class:`bool`):
                Pass true if the reaction is added with a big animation

            update_recent_reactions (:class:`bool`):
                Pass true if the reaction needs to be added to recent reactions; tags are never added to the list of recent reactions

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addMessageReaction",
                "chat_id": chat_id,
                "message_id": message_id,
                "reaction_type": reaction_type,
                "is_big": is_big,
                "update_recent_reactions": update_recent_reactions,
            }
        )

    async def removeMessageReaction(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reaction_type: "types.ReactionType" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a reaction from a message\. A chosen reaction can always be removed

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            reaction_type (:class:`"types.ReactionType"`):
                Type of the reaction to remove\. The paid reaction can't be removed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeMessageReaction",
                "chat_id": chat_id,
                "message_id": message_id,
                "reaction_type": reaction_type,
            }
        )

    async def getChatAvailablePaidMessageReactionSenders(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.MessageSenders"]:
        r"""Returns the list of message sender identifiers, which can be used to send a paid reaction in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.MessageSenders`
        """

        return await self.invoke(
            {"@type": "getChatAvailablePaidMessageReactionSenders", "chat_id": chat_id}
        )

    async def addPendingPaidMessageReaction(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        star_count: int = 0,
        type: "types.PaidReactionType" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds the paid message reaction to a message\. Use getMessageAvailableReactions to check whether the reaction is available for the message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            star_count (:class:`int`):
                Number of Telegram Stars to be used for the reaction\. The total number of pending paid reactions must not exceed getOption\(\"paid\_reaction\_star\_count\_max\"\)

            type (:class:`"types.PaidReactionType"`):
                Type of the paid reaction; pass null if the user didn't choose reaction type explicitly, for example, the reaction is set from the message bubble

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addPendingPaidMessageReaction",
                "chat_id": chat_id,
                "message_id": message_id,
                "star_count": star_count,
                "type": type,
            }
        )

    async def commitPendingPaidMessageReactions(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Applies all pending paid reactions on a message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "commitPendingPaidMessageReactions",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def removePendingPaidMessageReactions(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes all pending paid reactions on a message

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removePendingPaidMessageReactions",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def setPaidMessageReactionType(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        type: "types.PaidReactionType" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes type of paid message reaction of the current user on a message\. The message must have paid reaction added by the current user

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            type (:class:`"types.PaidReactionType"`):
                New type of the paid reaction

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setPaidMessageReactionType",
                "chat_id": chat_id,
                "message_id": message_id,
                "type": type,
            }
        )

    async def setMessageReactions(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reaction_types: List["types.ReactionType"] = None,
        is_big: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets reactions on a message; for bots only

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message

            reaction_types (:class:`List["types.ReactionType"]`):
                Types of the reaction to set; pass an empty list to remove the reactions

            is_big (:class:`bool`):
                Pass true if the reactions are added with a big animation

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setMessageReactions",
                "chat_id": chat_id,
                "message_id": message_id,
                "reaction_types": reaction_types,
                "is_big": is_big,
            }
        )

    async def getMessageAddedReactions(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reaction_type: "types.ReactionType" = None,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.AddedReactions"]:
        r"""Returns reactions added for a message, along with their sender

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the message belongs

            message_id (:class:`int`):
                Identifier of the message\. Use message\.interaction\_info\.reactions\.can\_get\_added\_reactions to check whether added reactions can be received for the message

            reaction_type (:class:`"types.ReactionType"`):
                Type of the reactions to return; pass null to return all added reactions; reactionTypePaid isn't supported

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of reactions to be returned; must be positive and can't be greater than 100

        Returns:
            :class:`~pytdbot.types.AddedReactions`
        """

        return await self.invoke(
            {
                "@type": "getMessageAddedReactions",
                "chat_id": chat_id,
                "message_id": message_id,
                "reaction_type": reaction_type,
                "offset": offset,
                "limit": limit,
            }
        )

    async def setDefaultReactionType(
        self, reaction_type: "types.ReactionType" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes type of default reaction for the current user

        Parameters:
            reaction_type (:class:`"types.ReactionType"`):
                New type of the default reaction\. The paid reaction can't be set as default

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setDefaultReactionType", "reaction_type": reaction_type}
        )

    async def getSavedMessagesTags(
        self, saved_messages_topic_id: int = 0
    ) -> Union["types.Error", "types.SavedMessagesTags"]:
        r"""Returns tags used in Saved Messages or a Saved Messages topic

        Parameters:
            saved_messages_topic_id (:class:`int`):
                Identifier of Saved Messages topic which tags will be returned; pass 0 to get all Saved Messages tags

        Returns:
            :class:`~pytdbot.types.SavedMessagesTags`
        """

        return await self.invoke(
            {
                "@type": "getSavedMessagesTags",
                "saved_messages_topic_id": saved_messages_topic_id,
            }
        )

    async def setSavedMessagesTagLabel(
        self, tag: "types.ReactionType" = None, label: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes label of a Saved Messages tag; for Telegram Premium users only

        Parameters:
            tag (:class:`"types.ReactionType"`):
                The tag which label will be changed

            label (:class:`str`):
                New label for the tag; 0\-12 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setSavedMessagesTagLabel", "tag": tag, "label": label}
        )

    async def getMessageEffect(
        self, effect_id: int = 0
    ) -> Union["types.Error", "types.MessageEffect"]:
        r"""Returns information about a message effect\. Returns a 404 error if the effect is not found

        Parameters:
            effect_id (:class:`int`):
                Unique identifier of the effect

        Returns:
            :class:`~pytdbot.types.MessageEffect`
        """

        return await self.invoke({"@type": "getMessageEffect", "effect_id": effect_id})

    async def searchQuote(
        self,
        text: "types.FormattedText" = None,
        quote: "types.FormattedText" = None,
        quote_position: int = 0,
    ) -> Union["types.Error", "types.FoundPosition"]:
        r"""Searches for a given quote in a text\. Returns found quote start position in UTF\-16 code units\. Returns a 404 error if the quote is not found\. Can be called synchronously

        Parameters:
            text (:class:`"types.FormattedText"`):
                Text in which to search for the quote

            quote (:class:`"types.FormattedText"`):
                Quote to search for

            quote_position (:class:`int`):
                Approximate quote position in UTF\-16 code units

        Returns:
            :class:`~pytdbot.types.FoundPosition`
        """

        return await self.invoke(
            {
                "@type": "searchQuote",
                "text": text,
                "quote": quote,
                "quote_position": quote_position,
            }
        )

    async def getTextEntities(
        self, text: str = ""
    ) -> Union["types.Error", "types.TextEntities"]:
        r"""Returns all entities \(mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses\) found in the text\. Can be called synchronously

        Parameters:
            text (:class:`str`):
                The text in which to look for entities

        Returns:
            :class:`~pytdbot.types.TextEntities`
        """

        return await self.invoke({"@type": "getTextEntities", "text": text})

    async def parseTextEntities(
        self, text: str = "", parse_mode: "types.TextParseMode" = None
    ) -> Union["types.Error", "types.FormattedText"]:
        r"""Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, ExpandableBlockQuote, Code, Pre, PreCode, TextUrl and MentionName entities from a marked\-up text\. Can be called synchronously

        Parameters:
            text (:class:`str`):
                The text to parse

            parse_mode (:class:`"types.TextParseMode"`):
                Text parse mode

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        return await self.invoke(
            {"@type": "parseTextEntities", "text": text, "parse_mode": parse_mode}
        )

    async def parseMarkdown(
        self, text: "types.FormattedText" = None
    ) -> Union["types.Error", "types.FormattedText"]:
        r"""Parses Markdown entities in a human\-friendly format, ignoring markup errors\. Can be called synchronously

        Parameters:
            text (:class:`"types.FormattedText"`):
                The text to parse\. For example, \"\_\_italic\_\_ \~\~strikethrough\~\~ \|\|spoiler\|\| \*\*bold\*\* \`code\` \`\`\`pre\`\`\` \_\_\[italic\_\_ text\_url\]\(telegram\.org\) \_\_italic\*\*bold italic\_\_bold\*\*\"

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        return await self.invoke({"@type": "parseMarkdown", "text": text})

    async def getMarkdownText(
        self, text: "types.FormattedText" = None
    ) -> Union["types.Error", "types.FormattedText"]:
        r"""Replaces text entities with Markdown formatting in a human\-friendly format\. Entities that can't be represented in Markdown unambiguously are kept as is\. Can be called synchronously

        Parameters:
            text (:class:`"types.FormattedText"`):
                The text

        Returns:
            :class:`~pytdbot.types.FormattedText`
        """

        return await self.invoke({"@type": "getMarkdownText", "text": text})

    async def getCountryFlagEmoji(
        self, country_code: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns an emoji for the given country\. Returns an empty string on failure\. Can be called synchronously

        Parameters:
            country_code (:class:`str`):
                A two\-letter ISO 3166\-1 alpha\-2 country code as received from getCountries

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {"@type": "getCountryFlagEmoji", "country_code": country_code}
        )

    async def getFileMimeType(
        self, file_name: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns the MIME type of a file, guessed by its extension\. Returns an empty string on failure\. Can be called synchronously

        Parameters:
            file_name (:class:`str`):
                The name of the file or path to the file

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke({"@type": "getFileMimeType", "file_name": file_name})

    async def getFileExtension(
        self, mime_type: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns the extension of a file, guessed by its MIME type\. Returns an empty string on failure\. Can be called synchronously

        Parameters:
            mime_type (:class:`str`):
                The MIME type of the file

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke({"@type": "getFileExtension", "mime_type": mime_type})

    async def cleanFileName(
        self, file_name: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Removes potentially dangerous characters from the name of a file\. Returns an empty string on failure\. Can be called synchronously

        Parameters:
            file_name (:class:`str`):
                File name or path to the file

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke({"@type": "cleanFileName", "file_name": file_name})

    async def getLanguagePackString(
        self,
        language_pack_database_path: str = "",
        localization_target: str = "",
        language_pack_id: str = "",
        key: str = "",
    ) -> Union["types.Error", "types.LanguagePackStringValue"]:
        r"""Returns a string stored in the local database from the specified localization target and language pack by its key\. Returns a 404 error if the string is not found\. Can be called synchronously

        Parameters:
            language_pack_database_path (:class:`str`):
                Path to the language pack database in which strings are stored

            localization_target (:class:`str`):
                Localization target to which the language pack belongs

            language_pack_id (:class:`str`):
                Language pack identifier

            key (:class:`str`):
                Language pack key of the string to be returned

        Returns:
            :class:`~pytdbot.types.LanguagePackStringValue`
        """

        return await self.invoke(
            {
                "@type": "getLanguagePackString",
                "language_pack_database_path": language_pack_database_path,
                "localization_target": localization_target,
                "language_pack_id": language_pack_id,
                "key": key,
            }
        )

    async def getJsonValue(
        self, json: str = ""
    ) -> Union["types.Error", "types.JsonValue"]:
        r"""Converts a JSON\-serialized string to corresponding JsonValue object\. Can be called synchronously

        Parameters:
            json (:class:`str`):
                The JSON\-serialized string

        Returns:
            :class:`~pytdbot.types.JsonValue`
        """

        return await self.invoke({"@type": "getJsonValue", "json": json})

    async def getJsonString(
        self, json_value: "types.JsonValue" = None
    ) -> Union["types.Error", "types.Text"]:
        r"""Converts a JsonValue object to corresponding JSON\-serialized string\. Can be called synchronously

        Parameters:
            json_value (:class:`"types.JsonValue"`):
                The JsonValue object

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke({"@type": "getJsonString", "json_value": json_value})

    async def getThemeParametersJsonString(
        self, theme: "types.ThemeParameters" = None
    ) -> Union["types.Error", "types.Text"]:
        r"""Converts a themeParameters object to corresponding JSON\-serialized string\. Can be called synchronously

        Parameters:
            theme (:class:`"types.ThemeParameters"`):
                Theme parameters to convert to JSON

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {"@type": "getThemeParametersJsonString", "theme": theme}
        )

    async def setPollAnswer(
        self, chat_id: int = 0, message_id: int = 0, option_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the user answer to a poll\. A poll in quiz mode can be answered only once

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the poll belongs

            message_id (:class:`int`):
                Identifier of the message containing the poll

            option_ids (:class:`List[int]`):
                0\-based identifiers of answer options, chosen by the user\. User can choose more than 1 answer option only is the poll allows multiple answers

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setPollAnswer",
                "chat_id": chat_id,
                "message_id": message_id,
                "option_ids": option_ids,
            }
        )

    async def getPollVoters(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        option_id: int = 0,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.MessageSenders"]:
        r"""Returns message senders voted for the specified option in a non\-anonymous polls\. For optimal performance, the number of returned users is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the poll belongs

            message_id (:class:`int`):
                Identifier of the message containing the poll

            option_id (:class:`int`):
                0\-based identifier of the answer option

            offset (:class:`int`):
                Number of voters to skip in the result; must be non\-negative

            limit (:class:`int`):
                The maximum number of voters to be returned; must be positive and can't be greater than 50\. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached

        Returns:
            :class:`~pytdbot.types.MessageSenders`
        """

        return await self.invoke(
            {
                "@type": "getPollVoters",
                "chat_id": chat_id,
                "message_id": message_id,
                "option_id": option_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def stopPoll(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        reply_markup: "types.ReplyMarkup" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Stops a poll

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to which the poll belongs

            message_id (:class:`int`):
                Identifier of the message containing the poll\. Use messageProperties\.can\_be\_edited to check whether the poll can be stopped

            reply_markup (:class:`"types.ReplyMarkup"`):
                The new message reply markup; pass null if none; for bots only

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "stopPoll",
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": reply_markup,
            }
        )

    async def hideSuggestedAction(
        self, action: "types.SuggestedAction" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Hides a suggested action

        Parameters:
            action (:class:`"types.SuggestedAction"`):
                Suggested action to hide

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "hideSuggestedAction", "action": action})

    async def hideContactCloseBirthdays(self) -> Union["types.Error", "types.Ok"]:
        r"""Hides the list of contacts that have close birthdays for 24 hours

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "hideContactCloseBirthdays",
            }
        )

    async def getBusinessConnection(
        self, connection_id: str = ""
    ) -> Union["types.Error", "types.BusinessConnection"]:
        r"""Returns information about a business connection by its identifier; for bots only

        Parameters:
            connection_id (:class:`str`):
                Identifier of the business connection to return

        Returns:
            :class:`~pytdbot.types.BusinessConnection`
        """

        return await self.invoke(
            {"@type": "getBusinessConnection", "connection_id": connection_id}
        )

    async def getLoginUrlInfo(
        self, chat_id: int = 0, message_id: int = 0, button_id: int = 0
    ) -> Union["types.Error", "types.LoginUrlInfo"]:
        r"""Returns information about a button of type inlineKeyboardButtonTypeLoginUrl\. The method needs to be called when the user presses the button

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the message with the button

            message_id (:class:`int`):
                Message identifier of the message with the button\. The message must not be scheduled

            button_id (:class:`int`):
                Button identifier

        Returns:
            :class:`~pytdbot.types.LoginUrlInfo`
        """

        return await self.invoke(
            {
                "@type": "getLoginUrlInfo",
                "chat_id": chat_id,
                "message_id": message_id,
                "button_id": button_id,
            }
        )

    async def getLoginUrl(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        button_id: int = 0,
        allow_write_access: bool = False,
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl\. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed\. If an error is returned, then the button must be handled as an ordinary URL button

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the message with the button

            message_id (:class:`int`):
                Message identifier of the message with the button

            button_id (:class:`int`):
                Button identifier

            allow_write_access (:class:`bool`):
                Pass true to allow the bot to send messages to the current user

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getLoginUrl",
                "chat_id": chat_id,
                "message_id": message_id,
                "button_id": button_id,
                "allow_write_access": allow_write_access,
            }
        )

    async def shareUsersWithBot(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        button_id: int = 0,
        shared_user_ids: List[int] = None,
        only_check: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Shares users after pressing a keyboardButtonTypeRequestUsers button with the bot

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat with the bot

            message_id (:class:`int`):
                Identifier of the message with the button

            button_id (:class:`int`):
                Identifier of the button

            shared_user_ids (:class:`List[int]`):
                Identifiers of the shared users

            only_check (:class:`bool`):
                Pass true to check that the users can be shared by the button instead of actually sharing them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "shareUsersWithBot",
                "chat_id": chat_id,
                "message_id": message_id,
                "button_id": button_id,
                "shared_user_ids": shared_user_ids,
                "only_check": only_check,
            }
        )

    async def shareChatWithBot(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        button_id: int = 0,
        shared_chat_id: int = 0,
        only_check: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat with the bot

            message_id (:class:`int`):
                Identifier of the message with the button

            button_id (:class:`int`):
                Identifier of the button

            shared_chat_id (:class:`int`):
                Identifier of the shared chat

            only_check (:class:`bool`):
                Pass true to check that the chat can be shared by the button instead of actually sharing it\. Doesn't check bot\_is\_member and bot\_administrator\_rights restrictions\. If the bot must be a member, then all chats from getGroupsInCommon and all chats, where the user can add the bot, are suitable\. In the latter case the bot will be automatically added to the chat\. If the bot must be an administrator, then all chats, where the bot already has requested rights or can be added to administrators by the user, are suitable\. In the latter case the bot will be automatically granted requested rights

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "shareChatWithBot",
                "chat_id": chat_id,
                "message_id": message_id,
                "button_id": button_id,
                "shared_chat_id": shared_chat_id,
                "only_check": only_check,
            }
        )

    async def getInlineQueryResults(
        self,
        bot_user_id: int = 0,
        chat_id: int = 0,
        user_location: "types.Location" = None,
        query: str = "",
        offset: str = "",
    ) -> Union["types.Error", "types.InlineQueryResults"]:
        r"""Sends an inline query to a bot and returns its results\. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            chat_id (:class:`int`):
                Identifier of the chat where the query was sent

            user_location (:class:`"types.Location"`):
                Location of the user; pass null if unknown or the bot doesn't need user's location

            query (:class:`str`):
                Text of the query

            offset (:class:`str`):
                Offset of the first entry to return; use empty string to get the first chunk of results

        Returns:
            :class:`~pytdbot.types.InlineQueryResults`
        """

        return await self.invoke(
            {
                "@type": "getInlineQueryResults",
                "bot_user_id": bot_user_id,
                "chat_id": chat_id,
                "user_location": user_location,
                "query": query,
                "offset": offset,
            }
        )

    async def answerInlineQuery(
        self,
        inline_query_id: int = 0,
        is_personal: bool = False,
        button: "types.InlineQueryResultsButton" = None,
        results: List["types.InputInlineQueryResult"] = None,
        cache_time: int = 0,
        next_offset: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the result of an inline query; for bots only

        Parameters:
            inline_query_id (:class:`int`):
                Identifier of the inline query

            is_personal (:class:`bool`):
                Pass true if results may be cached and returned only for the user that sent the query\. By default, results may be returned to any user who sends the same query

            button (:class:`"types.InlineQueryResultsButton"`):
                Button to be shown above inline query results; pass null if none

            results (:class:`List["types.InputInlineQueryResult"]`):
                The results of the query

            cache_time (:class:`int`):
                Allowed time to cache the results of the query, in seconds

            next_offset (:class:`str`):
                Offset for the next inline query; pass an empty string if there are no more results

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "answerInlineQuery",
                "inline_query_id": inline_query_id,
                "is_personal": is_personal,
                "button": button,
                "results": results,
                "cache_time": cache_time,
                "next_offset": next_offset,
            }
        )

    async def savePreparedInlineMessage(
        self,
        user_id: int = 0,
        result: "types.InputInlineQueryResult" = None,
        chat_types: "types.TargetChatTypes" = None,
    ) -> Union["types.Error", "types.PreparedInlineMessageId"]:
        r"""Saves an inline message to be sent by the given user; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user

            result (:class:`"types.InputInlineQueryResult"`):
                The description of the message

            chat_types (:class:`"types.TargetChatTypes"`):
                Types of the chats to which the message can be sent

        Returns:
            :class:`~pytdbot.types.PreparedInlineMessageId`
        """

        return await self.invoke(
            {
                "@type": "savePreparedInlineMessage",
                "user_id": user_id,
                "result": result,
                "chat_types": chat_types,
            }
        )

    async def getPreparedInlineMessage(
        self, bot_user_id: int = 0, prepared_message_id: str = ""
    ) -> Union["types.Error", "types.PreparedInlineMessage"]:
        r"""Saves an inline message to be sent by the given user

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the bot that created the message

            prepared_message_id (:class:`str`):
                Identifier of the prepared message

        Returns:
            :class:`~pytdbot.types.PreparedInlineMessage`
        """

        return await self.invoke(
            {
                "@type": "getPreparedInlineMessage",
                "bot_user_id": bot_user_id,
                "prepared_message_id": prepared_message_id,
            }
        )

    async def getGrossingWebAppBots(
        self, offset: str = "", limit: int = 0
    ) -> Union["types.Error", "types.FoundUsers"]:
        r"""Returns the most grossing Web App bots

        Parameters:
            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of bots to be returned; up to 100

        Returns:
            :class:`~pytdbot.types.FoundUsers`
        """

        return await self.invoke(
            {"@type": "getGrossingWebAppBots", "offset": offset, "limit": limit}
        )

    async def searchWebApp(
        self, bot_user_id: int = 0, web_app_short_name: str = ""
    ) -> Union["types.Error", "types.FoundWebApp"]:
        r"""Returns information about a Web App by its short name\. Returns a 404 error if the Web App is not found

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            web_app_short_name (:class:`str`):
                Short name of the Web App

        Returns:
            :class:`~pytdbot.types.FoundWebApp`
        """

        return await self.invoke(
            {
                "@type": "searchWebApp",
                "bot_user_id": bot_user_id,
                "web_app_short_name": web_app_short_name,
            }
        )

    async def getWebAppPlaceholder(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.Outline"]:
        r"""Returns a default placeholder for Web Apps of a bot\. This is an offline method\. Returns a 404 error if the placeholder isn't known

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

        Returns:
            :class:`~pytdbot.types.Outline`
        """

        return await self.invoke(
            {"@type": "getWebAppPlaceholder", "bot_user_id": bot_user_id}
        )

    async def getWebAppLinkUrl(
        self,
        chat_id: int = 0,
        bot_user_id: int = 0,
        web_app_short_name: str = "",
        start_parameter: str = "",
        allow_write_access: bool = False,
        parameters: "types.WebAppOpenParameters" = None,
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which the link was clicked; pass 0 if none

            bot_user_id (:class:`int`):
                Identifier of the target bot

            web_app_short_name (:class:`str`):
                Short name of the Web App

            start_parameter (:class:`str`):
                Start parameter from internalLinkTypeWebApp

            allow_write_access (:class:`bool`):
                Pass true if the current user allowed the bot to send them messages

            parameters (:class:`"types.WebAppOpenParameters"`):
                Parameters to use to open the Web App

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getWebAppLinkUrl",
                "chat_id": chat_id,
                "bot_user_id": bot_user_id,
                "web_app_short_name": web_app_short_name,
                "start_parameter": start_parameter,
                "allow_write_access": allow_write_access,
                "parameters": parameters,
            }
        )

    async def getMainWebApp(
        self,
        chat_id: int = 0,
        bot_user_id: int = 0,
        start_parameter: str = "",
        parameters: "types.WebAppOpenParameters" = None,
    ) -> Union["types.Error", "types.MainWebApp"]:
        r"""Returns information needed to open the main Web App of a bot

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which the Web App is opened; pass 0 if none

            bot_user_id (:class:`int`):
                Identifier of the target bot\. If the bot is restricted for the current user, then show an error instead of calling the method

            start_parameter (:class:`str`):
                Start parameter from internalLinkTypeMainWebApp

            parameters (:class:`"types.WebAppOpenParameters"`):
                Parameters to use to open the Web App

        Returns:
            :class:`~pytdbot.types.MainWebApp`
        """

        return await self.invoke(
            {
                "@type": "getMainWebApp",
                "chat_id": chat_id,
                "bot_user_id": bot_user_id,
                "start_parameter": start_parameter,
                "parameters": parameters,
            }
        )

    async def getWebAppUrl(
        self,
        bot_user_id: int = 0,
        url: str = "",
        parameters: "types.WebAppOpenParameters" = None,
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, or an inlineQueryResultsButtonTypeWebApp button

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. If the bot is restricted for the current user, then show an error instead of calling the method

            url (:class:`str`):
                The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, or an empty string when the bot is opened from the side menu

            parameters (:class:`"types.WebAppOpenParameters"`):
                Parameters to use to open the Web App

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getWebAppUrl",
                "bot_user_id": bot_user_id,
                "url": url,
                "parameters": parameters,
            }
        )

    async def sendWebAppData(
        self, bot_user_id: int = 0, button_text: str = "", data: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends data received from a keyboardButtonTypeWebApp Web App to a bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            button_text (:class:`str`):
                Text of the keyboardButtonTypeWebApp button, which opened the Web App

            data (:class:`str`):
                The data

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendWebAppData",
                "bot_user_id": bot_user_id,
                "button_text": button_text,
                "data": data,
            }
        )

    async def openWebApp(
        self,
        chat_id: int = 0,
        bot_user_id: int = 0,
        url: str = "",
        message_thread_id: int = 0,
        reply_to: "types.InputMessageReplyTo" = None,
        parameters: "types.WebAppOpenParameters" = None,
    ) -> Union["types.Error", "types.WebAppInfo"]:
        r"""Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button\. For each bot, a confirmation alert about data sent to the bot must be shown once

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat in which the Web App is opened\. The Web App can't be opened in secret chats

            bot_user_id (:class:`int`):
                Identifier of the bot, providing the Web App\. If the bot is restricted for the current user, then show an error instead of calling the method

            url (:class:`str`):
                The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the message will be sent

            reply_to (:class:`"types.InputMessageReplyTo"`):
                Information about the message or story to be replied in the message sent by the Web App; pass null if none

            parameters (:class:`"types.WebAppOpenParameters"`):
                Parameters to use to open the Web App

        Returns:
            :class:`~pytdbot.types.WebAppInfo`
        """

        return await self.invoke(
            {
                "@type": "openWebApp",
                "chat_id": chat_id,
                "bot_user_id": bot_user_id,
                "url": url,
                "message_thread_id": message_thread_id,
                "reply_to": reply_to,
                "parameters": parameters,
            }
        )

    async def closeWebApp(
        self, web_app_launch_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that a previously opened Web App was closed

        Parameters:
            web_app_launch_id (:class:`int`):
                Identifier of Web App launch, received from openWebApp

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "closeWebApp", "web_app_launch_id": web_app_launch_id}
        )

    async def answerWebAppQuery(
        self, web_app_query_id: str = "", result: "types.InputInlineQueryResult" = None
    ) -> Union["types.Error", "types.SentWebAppMessage"]:
        r"""Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

        Parameters:
            web_app_query_id (:class:`str`):
                Identifier of the Web App query

            result (:class:`"types.InputInlineQueryResult"`):
                The result of the query

        Returns:
            :class:`~pytdbot.types.SentWebAppMessage`
        """

        return await self.invoke(
            {
                "@type": "answerWebAppQuery",
                "web_app_query_id": web_app_query_id,
                "result": result,
            }
        )

    async def checkWebAppFileDownload(
        self, bot_user_id: int = 0, file_name: str = "", url: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether a file can be downloaded and saved locally by Web App request

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the bot, providing the Web App

            file_name (:class:`str`):
                Name of the file

            url (:class:`str`):
                URL of the file

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "checkWebAppFileDownload",
                "bot_user_id": bot_user_id,
                "file_name": file_name,
                "url": url,
            }
        )

    async def getCallbackQueryAnswer(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        payload: "types.CallbackQueryPayload" = None,
    ) -> Union["types.Error", "types.CallbackQueryAnswer"]:
        r"""Sends a callback query to a bot and returns an answer\. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat with the message

            message_id (:class:`int`):
                Identifier of the message from which the query originated\. The message must not be scheduled

            payload (:class:`"types.CallbackQueryPayload"`):
                Query payload

        Returns:
            :class:`~pytdbot.types.CallbackQueryAnswer`
        """

        return await self.invoke(
            {
                "@type": "getCallbackQueryAnswer",
                "chat_id": chat_id,
                "message_id": message_id,
                "payload": payload,
            }
        )

    async def answerCallbackQuery(
        self,
        callback_query_id: int = 0,
        text: str = "",
        show_alert: bool = False,
        url: str = "",
        cache_time: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the result of a callback query; for bots only

        Parameters:
            callback_query_id (:class:`int`):
                Identifier of the callback query

            text (:class:`str`):
                Text of the answer

            show_alert (:class:`bool`):
                Pass true to show an alert to the user instead of a toast notification

            url (:class:`str`):
                URL to be opened

            cache_time (:class:`int`):
                Time during which the result of the query can be cached, in seconds

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "answerCallbackQuery",
                "callback_query_id": callback_query_id,
                "text": text,
                "show_alert": show_alert,
                "url": url,
                "cache_time": cache_time,
            }
        )

    async def answerShippingQuery(
        self,
        shipping_query_id: int = 0,
        shipping_options: List["types.ShippingOption"] = None,
        error_message: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the result of a shipping query; for bots only

        Parameters:
            shipping_query_id (:class:`int`):
                Identifier of the shipping query

            shipping_options (:class:`List["types.ShippingOption"]`):
                Available shipping options

            error_message (:class:`str`):
                An error message, empty on success

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "answerShippingQuery",
                "shipping_query_id": shipping_query_id,
                "shipping_options": shipping_options,
                "error_message": error_message,
            }
        )

    async def answerPreCheckoutQuery(
        self, pre_checkout_query_id: int = 0, error_message: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the result of a pre\-checkout query; for bots only

        Parameters:
            pre_checkout_query_id (:class:`int`):
                Identifier of the pre\-checkout query

            error_message (:class:`str`):
                An error message, empty on success

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "answerPreCheckoutQuery",
                "pre_checkout_query_id": pre_checkout_query_id,
                "error_message": error_message,
            }
        )

    async def setGameScore(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        edit_message: bool = False,
        user_id: int = 0,
        score: int = 0,
        force: bool = False,
    ) -> Union["types.Error", "types.Message"]:
        r"""Updates the game score of the specified user in the game; for bots only

        Parameters:
            chat_id (:class:`int`):
                The chat to which the message with the game belongs

            message_id (:class:`int`):
                Identifier of the message

            edit_message (:class:`bool`):
                Pass true to edit the game message to include the current scoreboard

            user_id (:class:`int`):
                User identifier

            score (:class:`int`):
                The new score

            force (:class:`bool`):
                Pass true to update the score even if it decreases\. If the score is 0, the user will be deleted from the high score table

        Returns:
            :class:`~pytdbot.types.Message`
        """

        return await self.invoke(
            {
                "@type": "setGameScore",
                "chat_id": chat_id,
                "message_id": message_id,
                "edit_message": edit_message,
                "user_id": user_id,
                "score": score,
                "force": force,
            }
        )

    async def setInlineGameScore(
        self,
        inline_message_id: str = "",
        edit_message: bool = False,
        user_id: int = 0,
        score: int = 0,
        force: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Updates the game score of the specified user in a game; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            edit_message (:class:`bool`):
                Pass true to edit the game message to include the current scoreboard

            user_id (:class:`int`):
                User identifier

            score (:class:`int`):
                The new score

            force (:class:`bool`):
                Pass true to update the score even if it decreases\. If the score is 0, the user will be deleted from the high score table

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setInlineGameScore",
                "inline_message_id": inline_message_id,
                "edit_message": edit_message,
                "user_id": user_id,
                "score": score,
                "force": force,
            }
        )

    async def getGameHighScores(
        self, chat_id: int = 0, message_id: int = 0, user_id: int = 0
    ) -> Union["types.Error", "types.GameHighScores"]:
        r"""Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only

        Parameters:
            chat_id (:class:`int`):
                The chat that contains the message with the game

            message_id (:class:`int`):
                Identifier of the message

            user_id (:class:`int`):
                User identifier

        Returns:
            :class:`~pytdbot.types.GameHighScores`
        """

        return await self.invoke(
            {
                "@type": "getGameHighScores",
                "chat_id": chat_id,
                "message_id": message_id,
                "user_id": user_id,
            }
        )

    async def getInlineGameHighScores(
        self, inline_message_id: str = "", user_id: int = 0
    ) -> Union["types.Error", "types.GameHighScores"]:
        r"""Returns game high scores and some part of the high score table in the range of the specified user; for bots only

        Parameters:
            inline_message_id (:class:`str`):
                Inline message identifier

            user_id (:class:`int`):
                User identifier

        Returns:
            :class:`~pytdbot.types.GameHighScores`
        """

        return await self.invoke(
            {
                "@type": "getInlineGameHighScores",
                "inline_message_id": inline_message_id,
                "user_id": user_id,
            }
        )

    async def deleteChatReplyMarkup(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes the default reply markup from a chat\. Must be called after a one\-time keyboard or a replyMarkupForceReply reply markup has been used\. An updateChatReplyMarkup update will be sent if the reply markup is changed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                The message identifier of the used keyboard

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatReplyMarkup",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def sendChatAction(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        business_connection_id: str = "",
        action: "types.ChatAction" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends a notification about user activity in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the action was performed

            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request; for bots only

            action (:class:`"types.ChatAction"`):
                The action description; pass null to cancel the currently active action

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendChatAction",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "business_connection_id": business_connection_id,
                "action": action,
            }
        )

    async def openChat(self, chat_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the chat is opened by the user\. Many useful activities depend on the chat being opened or closed \(e\.g\., in supergroups and channels all updates are received only for opened chats\)

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "openChat", "chat_id": chat_id})

    async def closeChat(self, chat_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the chat is closed by the user\. Many useful activities depend on the chat being opened or closed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "closeChat", "chat_id": chat_id})

    async def viewMessages(
        self,
        chat_id: int = 0,
        message_ids: List[int] = None,
        source: "types.MessageSource" = None,
        force_read: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that messages are being viewed by the user\. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen \(excluding the button\)\. Many useful activities depend on whether the messages are currently being viewed or not \(e\.g\., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels\)

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_ids (:class:`List[int]`):
                The identifiers of the messages being viewed

            source (:class:`"types.MessageSource"`):
                Source of the message view; pass null to guess the source based on chat open state

            force_read (:class:`bool`):
                Pass true to mark as read the specified messages even the chat is closed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "viewMessages",
                "chat_id": chat_id,
                "message_ids": message_ids,
                "source": source,
                "force_read": force_read,
            }
        )

    async def openMessageContent(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the message content has been opened \(e\.g\., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message\)\. An updateMessageContentOpened update will be generated if something has changed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the message

            message_id (:class:`int`):
                Identifier of the message with the opened content

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "openMessageContent",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def clickAnimatedEmojiMessage(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Sticker"]:
        r"""Informs TDLib that a message with an animated emoji was clicked by the user\. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the message

            message_id (:class:`int`):
                Identifier of the clicked message

        Returns:
            :class:`~pytdbot.types.Sticker`
        """

        return await self.invoke(
            {
                "@type": "clickAnimatedEmojiMessage",
                "chat_id": chat_id,
                "message_id": message_id,
            }
        )

    async def getInternalLink(
        self, type: "types.InternalLinkType" = None, is_http: bool = False
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTPS or a tg: link with the given type\. Can be called before authorization

        Parameters:
            type (:class:`"types.InternalLinkType"`):
                Expected type of the link

            is_http (:class:`bool`):
                Pass true to create an HTTPS link \(only available for some link types\); pass false to create a tg: link

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {"@type": "getInternalLink", "type": type, "is_http": is_http}
        )

    async def getInternalLinkType(
        self, link: str = ""
    ) -> Union["types.Error", "types.InternalLinkType"]:
        r"""Returns information about the type of internal link\. Returns a 404 error if the link is not internal\. Can be called before authorization

        Parameters:
            link (:class:`str`):
                The link

        Returns:
            :class:`~pytdbot.types.InternalLinkType`
        """

        return await self.invoke({"@type": "getInternalLinkType", "link": link})

    async def getExternalLinkInfo(
        self, link: str = ""
    ) -> Union["types.Error", "types.LoginUrlInfo"]:
        r"""Returns information about an action to be done when the current user clicks an external link\. Don't use this method for links from secret chats if link preview is disabled in secret chats

        Parameters:
            link (:class:`str`):
                The link

        Returns:
            :class:`~pytdbot.types.LoginUrlInfo`
        """

        return await self.invoke({"@type": "getExternalLinkInfo", "link": link})

    async def getExternalLink(
        self, link: str = "", allow_write_access: bool = False
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link\. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

        Parameters:
            link (:class:`str`):
                The HTTP link

            allow_write_access (:class:`bool`):
                Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getExternalLink",
                "link": link,
                "allow_write_access": allow_write_access,
            }
        )

    async def readAllChatMentions(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Marks all mentions in a chat as read

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "readAllChatMentions", "chat_id": chat_id})

    async def readAllMessageThreadMentions(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Marks all mentions in a forum topic as read

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                Message thread identifier in which mentions are marked as read

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "readAllMessageThreadMentions",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def readAllChatReactions(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Marks all reactions in a chat or a forum topic as read

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "readAllChatReactions", "chat_id": chat_id})

    async def readAllMessageThreadReactions(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Marks all reactions in a forum topic as read

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                Message thread identifier in which reactions are marked as read

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "readAllMessageThreadReactions",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def createPrivateChat(
        self, user_id: int = 0, force: bool = False
    ) -> Union["types.Error", "types.Chat"]:
        r"""Returns an existing chat corresponding to a given user

        Parameters:
            user_id (:class:`int`):
                User identifier

            force (:class:`bool`):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {"@type": "createPrivateChat", "user_id": user_id, "force": force}
        )

    async def createBasicGroupChat(
        self, basic_group_id: int = 0, force: bool = False
    ) -> Union["types.Error", "types.Chat"]:
        r"""Returns an existing chat corresponding to a known basic group

        Parameters:
            basic_group_id (:class:`int`):
                Basic group identifier

            force (:class:`bool`):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {
                "@type": "createBasicGroupChat",
                "basic_group_id": basic_group_id,
                "force": force,
            }
        )

    async def createSupergroupChat(
        self, supergroup_id: int = 0, force: bool = False
    ) -> Union["types.Error", "types.Chat"]:
        r"""Returns an existing chat corresponding to a known supergroup or channel

        Parameters:
            supergroup_id (:class:`int`):
                Supergroup or channel identifier

            force (:class:`bool`):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {
                "@type": "createSupergroupChat",
                "supergroup_id": supergroup_id,
                "force": force,
            }
        )

    async def createSecretChat(
        self, secret_chat_id: int = 0
    ) -> Union["types.Error", "types.Chat"]:
        r"""Returns an existing chat corresponding to a known secret chat

        Parameters:
            secret_chat_id (:class:`int`):
                Secret chat identifier

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {"@type": "createSecretChat", "secret_chat_id": secret_chat_id}
        )

    async def createNewBasicGroupChat(
        self,
        user_ids: List[int] = None,
        title: str = "",
        message_auto_delete_time: int = 0,
    ) -> Union["types.Error", "types.CreatedBasicGroupChat"]:
        r"""Creates a new basic group and sends a corresponding messageBasicGroupChatCreate\. Returns information about the newly created chat

        Parameters:
            user_ids (:class:`List[int]`):
                Identifiers of users to be added to the basic group; may be empty to create a basic group without other members

            title (:class:`str`):
                Title of the new basic group; 1\-128 characters

            message_auto_delete_time (:class:`int`):
                Message auto\-delete time value, in seconds; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

        Returns:
            :class:`~pytdbot.types.CreatedBasicGroupChat`
        """

        return await self.invoke(
            {
                "@type": "createNewBasicGroupChat",
                "user_ids": user_ids,
                "title": title,
                "message_auto_delete_time": message_auto_delete_time,
            }
        )

    async def createNewSupergroupChat(
        self,
        title: str = "",
        is_forum: bool = False,
        is_channel: bool = False,
        description: str = "",
        location: "types.ChatLocation" = None,
        message_auto_delete_time: int = 0,
        for_import: bool = False,
    ) -> Union["types.Error", "types.Chat"]:
        r"""Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate\. Returns the newly created chat

        Parameters:
            title (:class:`str`):
                Title of the new chat; 1\-128 characters

            is_forum (:class:`bool`):
                Pass true to create a forum supergroup chat

            is_channel (:class:`bool`):
                Pass true to create a channel chat; ignored if a forum is created

            description (:class:`str`):
                Chat description; 0\-255 characters

            location (:class:`"types.ChatLocation"`):
                Chat location if a location\-based supergroup is being created; pass null to create an ordinary supergroup chat

            message_auto_delete_time (:class:`int`):
                Message auto\-delete time value, in seconds; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

            for_import (:class:`bool`):
                Pass true to create a supergroup for importing messages using importMessages

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {
                "@type": "createNewSupergroupChat",
                "title": title,
                "is_forum": is_forum,
                "is_channel": is_channel,
                "description": description,
                "location": location,
                "message_auto_delete_time": message_auto_delete_time,
                "for_import": for_import,
            }
        )

    async def createNewSecretChat(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.Chat"]:
        r"""Creates a new secret chat\. Returns the newly created chat

        Parameters:
            user_id (:class:`int`):
                Identifier of the target user

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke({"@type": "createNewSecretChat", "user_id": user_id})

    async def upgradeBasicGroupChatToSupergroupChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Chat"]:
        r"""Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires owner privileges\. Deactivates the original basic group

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat to upgrade

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {"@type": "upgradeBasicGroupChatToSupergroupChat", "chat_id": chat_id}
        )

    async def getChatListsToAddChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatLists"]:
        r"""Returns chat lists to which the chat can be added\. This is an offline method

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatLists`
        """

        return await self.invoke({"@type": "getChatListsToAddChat", "chat_id": chat_id})

    async def addChatToList(
        self, chat_id: int = 0, chat_list: "types.ChatList" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a chat to a chat list\. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            chat_list (:class:`"types.ChatList"`):
                The chat list\. Use getChatListsToAddChat to get suitable chat lists

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "addChatToList", "chat_id": chat_id, "chat_list": chat_list}
        )

    async def getChatFolder(
        self, chat_folder_id: int = 0
    ) -> Union["types.Error", "types.ChatFolder"]:
        r"""Returns information about a chat folder by its identifier

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

        Returns:
            :class:`~pytdbot.types.ChatFolder`
        """

        return await self.invoke(
            {"@type": "getChatFolder", "chat_folder_id": chat_folder_id}
        )

    async def createChatFolder(
        self, folder: "types.ChatFolder" = None
    ) -> Union["types.Error", "types.ChatFolderInfo"]:
        r"""Creates new chat folder\. Returns information about the created chat folder\. There can be up to getOption\(\"chat\_folder\_count\_max\"\) chat folders, but the limit can be increased with Telegram Premium

        Parameters:
            folder (:class:`"types.ChatFolder"`):
                The new chat folder

        Returns:
            :class:`~pytdbot.types.ChatFolderInfo`
        """

        return await self.invoke({"@type": "createChatFolder", "folder": folder})

    async def editChatFolder(
        self, chat_folder_id: int = 0, folder: "types.ChatFolder" = None
    ) -> Union["types.Error", "types.ChatFolderInfo"]:
        r"""Edits existing chat folder\. Returns information about the edited chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            folder (:class:`"types.ChatFolder"`):
                The edited chat folder

        Returns:
            :class:`~pytdbot.types.ChatFolderInfo`
        """

        return await self.invoke(
            {
                "@type": "editChatFolder",
                "chat_folder_id": chat_folder_id,
                "folder": folder,
            }
        )

    async def deleteChatFolder(
        self, chat_folder_id: int = 0, leave_chat_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes existing chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            leave_chat_ids (:class:`List[int]`):
                Identifiers of the chats to leave\. The chats must be pinned or always included in the folder

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatFolder",
                "chat_folder_id": chat_folder_id,
                "leave_chat_ids": leave_chat_ids,
            }
        )

    async def getChatFolderChatsToLeave(
        self, chat_folder_id: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "getChatFolderChatsToLeave", "chat_folder_id": chat_folder_id}
        )

    async def getChatFolderChatCount(
        self, folder: "types.ChatFolder" = None
    ) -> Union["types.Error", "types.Count"]:
        r"""Returns approximate number of chats in a being created chat folder\. Main and archive chat lists must be fully preloaded for this function to work correctly

        Parameters:
            folder (:class:`"types.ChatFolder"`):
                The new chat folder

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke({"@type": "getChatFolderChatCount", "folder": folder})

    async def reorderChatFolders(
        self, chat_folder_ids: List[int] = None, main_chat_list_position: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of chat folders

        Parameters:
            chat_folder_ids (:class:`List[int]`):
                Identifiers of chat folders in the new correct order

            main_chat_list_position (:class:`int`):
                Position of the main chat list among chat folders, 0\-based\. Can be non\-zero only for Premium users

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reorderChatFolders",
                "chat_folder_ids": chat_folder_ids,
                "main_chat_list_position": main_chat_list_position,
            }
        )

    async def toggleChatFolderTags(
        self, are_tags_enabled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether chat folder tags are enabled

        Parameters:
            are_tags_enabled (:class:`bool`):
                Pass true to enable folder tags; pass false to disable them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "toggleChatFolderTags", "are_tags_enabled": are_tags_enabled}
        )

    async def getRecommendedChatFolders(
        self,
    ) -> Union["types.Error", "types.RecommendedChatFolders"]:
        r"""Returns recommended chat folders for the current user

        Returns:
            :class:`~pytdbot.types.RecommendedChatFolders`
        """

        return await self.invoke(
            {
                "@type": "getRecommendedChatFolders",
            }
        )

    async def getChatFolderDefaultIconName(
        self, folder: "types.ChatFolder" = None
    ) -> Union["types.Error", "types.ChatFolderIcon"]:
        r"""Returns default icon name for a folder\. Can be called synchronously

        Parameters:
            folder (:class:`"types.ChatFolder"`):
                Chat folder

        Returns:
            :class:`~pytdbot.types.ChatFolderIcon`
        """

        return await self.invoke(
            {"@type": "getChatFolderDefaultIconName", "folder": folder}
        )

    async def getChatsForChatFolderInviteLink(
        self, chat_folder_id: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getChatsForChatFolderInviteLink",
                "chat_folder_id": chat_folder_id,
            }
        )

    async def createChatFolderInviteLink(
        self, chat_folder_id: int = 0, name: str = "", chat_ids: List[int] = None
    ) -> Union["types.Error", "types.ChatFolderInviteLink"]:
        r"""Creates a new invite link for a chat folder\. A link can be created for a chat folder if it has only pinned and included chats

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            name (:class:`str`):
                Name of the link; 0\-32 characters

            chat_ids (:class:`List[int]`):
                Identifiers of chats to be accessible by the invite link\. Use getChatsForChatFolderInviteLink to get suitable chats\. Basic groups will be automatically converted to supergroups before link creation

        Returns:
            :class:`~pytdbot.types.ChatFolderInviteLink`
        """

        return await self.invoke(
            {
                "@type": "createChatFolderInviteLink",
                "chat_folder_id": chat_folder_id,
                "name": name,
                "chat_ids": chat_ids,
            }
        )

    async def getChatFolderInviteLinks(
        self, chat_folder_id: int = 0
    ) -> Union["types.Error", "types.ChatFolderInviteLinks"]:
        r"""Returns invite links created by the current user for a shareable chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

        Returns:
            :class:`~pytdbot.types.ChatFolderInviteLinks`
        """

        return await self.invoke(
            {"@type": "getChatFolderInviteLinks", "chat_folder_id": chat_folder_id}
        )

    async def editChatFolderInviteLink(
        self,
        chat_folder_id: int = 0,
        invite_link: str = "",
        name: str = "",
        chat_ids: List[int] = None,
    ) -> Union["types.Error", "types.ChatFolderInviteLink"]:
        r"""Edits an invite link for a chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            invite_link (:class:`str`):
                Invite link to be edited

            name (:class:`str`):
                New name of the link; 0\-32 characters

            chat_ids (:class:`List[int]`):
                New identifiers of chats to be accessible by the invite link\. Use getChatsForChatFolderInviteLink to get suitable chats\. Basic groups will be automatically converted to supergroups before link editing

        Returns:
            :class:`~pytdbot.types.ChatFolderInviteLink`
        """

        return await self.invoke(
            {
                "@type": "editChatFolderInviteLink",
                "chat_folder_id": chat_folder_id,
                "invite_link": invite_link,
                "name": name,
                "chat_ids": chat_ids,
            }
        )

    async def deleteChatFolderInviteLink(
        self, chat_folder_id: int = 0, invite_link: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes an invite link for a chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            invite_link (:class:`str`):
                Invite link to be deleted

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatFolderInviteLink",
                "chat_folder_id": chat_folder_id,
                "invite_link": invite_link,
            }
        )

    async def checkChatFolderInviteLink(
        self, invite_link: str = ""
    ) -> Union["types.Error", "types.ChatFolderInviteLinkInfo"]:
        r"""Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder

        Parameters:
            invite_link (:class:`str`):
                Invite link to be checked

        Returns:
            :class:`~pytdbot.types.ChatFolderInviteLinkInfo`
        """

        return await self.invoke(
            {"@type": "checkChatFolderInviteLink", "invite_link": invite_link}
        )

    async def addChatFolderByInviteLink(
        self, invite_link: str = "", chat_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a chat folder by an invite link

        Parameters:
            invite_link (:class:`str`):
                Invite link for the chat folder

            chat_ids (:class:`List[int]`):
                Identifiers of the chats added to the chat folder\. The chats are automatically joined if they aren't joined yet

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addChatFolderByInviteLink",
                "invite_link": invite_link,
                "chat_ids": chat_ids,
            }
        )

    async def getChatFolderNewChats(
        self, chat_folder_id: int = 0
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns new chats added to a shareable chat folder by its owner\. The method must be called at most once in getOption\(\"chat\_folder\_new\_chats\_update\_period\"\) for the given chat folder

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {"@type": "getChatFolderNewChats", "chat_folder_id": chat_folder_id}
        )

    async def processChatFolderNewChats(
        self, chat_folder_id: int = 0, added_chat_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Process new chats added to a shareable chat folder by its owner

        Parameters:
            chat_folder_id (:class:`int`):
                Chat folder identifier

            added_chat_ids (:class:`List[int]`):
                Identifiers of the new chats, which are added to the chat folder\. The chats are automatically joined if they aren't joined yet

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "processChatFolderNewChats",
                "chat_folder_id": chat_folder_id,
                "added_chat_ids": added_chat_ids,
            }
        )

    async def getArchiveChatListSettings(
        self,
    ) -> Union["types.Error", "types.ArchiveChatListSettings"]:
        r"""Returns settings for automatic moving of chats to and from the Archive chat lists

        Returns:
            :class:`~pytdbot.types.ArchiveChatListSettings`
        """

        return await self.invoke(
            {
                "@type": "getArchiveChatListSettings",
            }
        )

    async def setArchiveChatListSettings(
        self, settings: "types.ArchiveChatListSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes settings for automatic moving of chats to and from the Archive chat lists

        Parameters:
            settings (:class:`"types.ArchiveChatListSettings"`):
                New settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setArchiveChatListSettings", "settings": settings}
        )

    async def setChatTitle(
        self, chat_id: int = 0, title: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the chat title\. Supported only for basic groups, supergroups and channels\. Requires can\_change\_info member right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            title (:class:`str`):
                New title of the chat; 1\-128 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setChatTitle", "chat_id": chat_id, "title": title}
        )

    async def setChatPhoto(
        self, chat_id: int = 0, photo: "types.InputChatPhoto" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the photo of a chat\. Supported only for basic groups, supergroups and channels\. Requires can\_change\_info member right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            photo (:class:`"types.InputChatPhoto"`):
                New chat photo; pass null to delete the chat photo

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setChatPhoto", "chat_id": chat_id, "photo": photo}
        )

    async def setChatAccentColor(
        self,
        chat_id: int = 0,
        accent_color_id: int = 0,
        background_custom_emoji_id: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes accent color and background custom emoji of a channel chat\. Requires can\_change\_info administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            accent_color_id (:class:`int`):
                Identifier of the accent color to use\. The chat must have at least accentColor\.min\_channel\_chat\_boost\_level boost level to pass the corresponding color

            background_custom_emoji_id (:class:`int`):
                Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none\. Use chatBoostLevelFeatures\.can\_set\_background\_custom\_emoji to check whether a custom emoji can be set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatAccentColor",
                "chat_id": chat_id,
                "accent_color_id": accent_color_id,
                "background_custom_emoji_id": background_custom_emoji_id,
            }
        )

    async def setChatProfileAccentColor(
        self,
        chat_id: int = 0,
        profile_accent_color_id: int = 0,
        profile_background_custom_emoji_id: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes accent color and background custom emoji for profile of a supergroup or channel chat\. Requires can\_change\_info administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            profile_accent_color_id (:class:`int`):
                Identifier of the accent color to use for profile; pass \-1 if none\. The chat must have at least profileAccentColor\.min\_supergroup\_chat\_boost\_level for supergroups or profileAccentColor\.min\_channel\_chat\_boost\_level for channels boost level to pass the corresponding color

            profile_background_custom_emoji_id (:class:`int`):
                Identifier of a custom emoji to be shown on the chat's profile photo background; 0 if none\. Use chatBoostLevelFeatures\.can\_set\_profile\_background\_custom\_emoji to check whether a custom emoji can be set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatProfileAccentColor",
                "chat_id": chat_id,
                "profile_accent_color_id": profile_accent_color_id,
                "profile_background_custom_emoji_id": profile_background_custom_emoji_id,
            }
        )

    async def setChatMessageAutoDeleteTime(
        self, chat_id: int = 0, message_auto_delete_time: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the message auto\-delete or self\-destruct \(for secret chats\) time in a chat\. Requires change\_info administrator right in basic groups, supergroups and channels\. Message auto\-delete time can't be changed in a chat with the current user \(Saved Messages\) and the chat 777000 \(Telegram\)\.

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_auto_delete_time (:class:`int`):
                New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatMessageAutoDeleteTime",
                "chat_id": chat_id,
                "message_auto_delete_time": message_auto_delete_time,
            }
        )

    async def setChatEmojiStatus(
        self, chat_id: int = 0, emoji_status: "types.EmojiStatus" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the emoji status of a chat\. Use chatBoostLevelFeatures\.can\_set\_emoji\_status to check whether an emoji status can be set\. Requires can\_change\_info administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            emoji_status (:class:`"types.EmojiStatus"`):
                New emoji status; pass null to remove emoji status

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatEmojiStatus",
                "chat_id": chat_id,
                "emoji_status": emoji_status,
            }
        )

    async def setChatPermissions(
        self, chat_id: int = 0, permissions: "types.ChatPermissions" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the chat members permissions\. Supported only for basic groups and supergroups\. Requires can\_restrict\_members administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            permissions (:class:`"types.ChatPermissions"`):
                New non\-administrator members permissions in the chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatPermissions",
                "chat_id": chat_id,
                "permissions": permissions,
            }
        )

    async def setChatBackground(
        self,
        chat_id: int = 0,
        background: "types.InputBackground" = None,
        type: "types.BackgroundType" = None,
        dark_theme_dimming: int = 0,
        only_for_self: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the background in a specific chat\. Supported only in private and secret chats with non\-deleted users, and in chats with sufficient boost level and can\_change\_info administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            background (:class:`"types.InputBackground"`):
                The input background to use; pass null to create a new filled or chat theme background

            type (:class:`"types.BackgroundType"`):
                Background type; pass null to use default background type for the chosen background; backgroundTypeChatTheme isn't supported for private and secret chats\. Use chatBoostLevelFeatures\.chat\_theme\_background\_count and chatBoostLevelFeatures\.can\_set\_custom\_background to check whether the background type can be set in the boosted chat

            dark_theme_dimming (:class:`int`):
                Dimming of the background in dark themes, as a percentage; 0\-100\. Applied only to Wallpaper and Fill types of background

            only_for_self (:class:`bool`):
                Pass true to set background only for self; pass false to set background for all chat users\. Always false for backgrounds set in boosted chats\. Background can be set for both users only by Telegram Premium users and if set background isn't of the type inputBackgroundPrevious

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatBackground",
                "chat_id": chat_id,
                "background": background,
                "type": type,
                "dark_theme_dimming": dark_theme_dimming,
                "only_for_self": only_for_self,
            }
        )

    async def deleteChatBackground(
        self, chat_id: int = 0, restore_previous: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes background in a specific chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            restore_previous (:class:`bool`):
                Pass true to restore previously set background\. Can be used only in private and secret chats with non\-deleted users if userFullInfo\.set\_chat\_background \=\= true\. Supposed to be used from messageChatSetBackground messages with the currently set background that was set for both sides by the other user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteChatBackground",
                "chat_id": chat_id,
                "restore_previous": restore_previous,
            }
        )

    async def setChatTheme(
        self, chat_id: int = 0, theme_name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the chat theme\. Supported only in private and secret chats

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            theme_name (:class:`str`):
                Name of the new chat theme; pass an empty string to return the default theme

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setChatTheme", "chat_id": chat_id, "theme_name": theme_name}
        )

    async def setChatDraftMessage(
        self,
        chat_id: int = 0,
        message_thread_id: int = 0,
        draft_message: "types.DraftMessage" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the draft message in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_thread_id (:class:`int`):
                If not 0, the message thread identifier in which the draft was changed

            draft_message (:class:`"types.DraftMessage"`):
                New draft message; pass null to remove the draft\. All files in draft message content must be of the type inputFileLocal\. Media thumbnails and captions are ignored

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatDraftMessage",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
                "draft_message": draft_message,
            }
        )

    async def setChatNotificationSettings(
        self,
        chat_id: int = 0,
        notification_settings: "types.ChatNotificationSettings" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the notification settings of a chat\. Notification settings of a chat with the current user \(Saved Messages\) can't be changed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            notification_settings (:class:`"types.ChatNotificationSettings"`):
                New notification settings for the chat\. If the chat is muted for more than 366 days, it is considered to be muted forever

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatNotificationSettings",
                "chat_id": chat_id,
                "notification_settings": notification_settings,
            }
        )

    async def toggleChatHasProtectedContent(
        self, chat_id: int = 0, has_protected_content: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the ability of users to save, forward, or copy chat content\. Supported only for basic groups, supergroups and channels\. Requires owner privileges

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            has_protected_content (:class:`bool`):
                New value of has\_protected\_content

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatHasProtectedContent",
                "chat_id": chat_id,
                "has_protected_content": has_protected_content,
            }
        )

    async def toggleChatViewAsTopics(
        self, chat_id: int = 0, view_as_topics: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the view\_as\_topics setting of a forum chat or Saved Messages

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            view_as_topics (:class:`bool`):
                New value of view\_as\_topics

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatViewAsTopics",
                "chat_id": chat_id,
                "view_as_topics": view_as_topics,
            }
        )

    async def toggleChatIsTranslatable(
        self, chat_id: int = 0, is_translatable: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the translatable state of a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            is_translatable (:class:`bool`):
                New value of is\_translatable

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatIsTranslatable",
                "chat_id": chat_id,
                "is_translatable": is_translatable,
            }
        )

    async def toggleChatIsMarkedAsUnread(
        self, chat_id: int = 0, is_marked_as_unread: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the marked as unread state of a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            is_marked_as_unread (:class:`bool`):
                New value of is\_marked\_as\_unread

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatIsMarkedAsUnread",
                "chat_id": chat_id,
                "is_marked_as_unread": is_marked_as_unread,
            }
        )

    async def toggleChatDefaultDisableNotification(
        self, chat_id: int = 0, default_disable_notification: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the value of the default disable\_notification parameter, used when a message is sent to a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            default_disable_notification (:class:`bool`):
                New value of default\_disable\_notification

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatDefaultDisableNotification",
                "chat_id": chat_id,
                "default_disable_notification": default_disable_notification,
            }
        )

    async def setChatAvailableReactions(
        self,
        chat_id: int = 0,
        available_reactions: "types.ChatAvailableReactions" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes reactions, available in a chat\. Available for basic groups, supergroups, and channels\. Requires can\_change\_info member right

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            available_reactions (:class:`"types.ChatAvailableReactions"`):
                Reactions available in the chat\. All explicitly specified emoji reactions must be active\. In channel chats up to the chat's boost level custom emoji reactions can be explicitly specified

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatAvailableReactions",
                "chat_id": chat_id,
                "available_reactions": available_reactions,
            }
        )

    async def setChatClientData(
        self, chat_id: int = 0, client_data: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes application\-specific data associated with a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            client_data (:class:`str`):
                New value of client\_data

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatClientData",
                "chat_id": chat_id,
                "client_data": client_data,
            }
        )

    async def setChatDescription(
        self, chat_id: int = 0, description: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes information about a chat\. Available for basic groups, supergroups, and channels\. Requires can\_change\_info member right

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            description (:class:`str`):
                New chat description; 0\-255 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatDescription",
                "chat_id": chat_id,
                "description": description,
            }
        )

    async def setChatDiscussionGroup(
        self, chat_id: int = 0, discussion_chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the discussion group of a channel chat; requires can\_change\_info administrator right in the channel if it is specified

        Parameters:
            chat_id (:class:`int`):
                Identifier of the channel chat\. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat \(requires can\_pin\_messages member right in the supergroup\)

            discussion_chat_id (:class:`int`):
                Identifier of a new channel's discussion group\. Use 0 to remove the discussion group\. Use the method getSuitableDiscussionChats to find all suitable groups\. Basic group chats must be first upgraded to supergroup chats\. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatDiscussionGroup",
                "chat_id": chat_id,
                "discussion_chat_id": discussion_chat_id,
            }
        )

    async def setChatLocation(
        self, chat_id: int = 0, location: "types.ChatLocation" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the location of a chat\. Available only for some location\-based supergroups, use supergroupFullInfo\.can\_set\_location to check whether the method is allowed to use

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            location (:class:`"types.ChatLocation"`):
                New location for the chat; must be valid and not null

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setChatLocation", "chat_id": chat_id, "location": location}
        )

    async def setChatSlowModeDelay(
        self, chat_id: int = 0, slow_mode_delay: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the slow mode delay of a chat\. Available only for supergroups; requires can\_restrict\_members right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            slow_mode_delay (:class:`int`):
                New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatSlowModeDelay",
                "chat_id": chat_id,
                "slow_mode_delay": slow_mode_delay,
            }
        )

    async def pinChatMessage(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        disable_notification: bool = False,
        only_for_self: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Pins a message in a chat\. A message can be pinned only if messageProperties\.can\_be\_pinned

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_id (:class:`int`):
                Identifier of the new pinned message

            disable_notification (:class:`bool`):
                Pass true to disable notification about the pinned message\. Notifications are always disabled in channels and private chats

            only_for_self (:class:`bool`):
                Pass true to pin the message only for self; private chats only

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "pinChatMessage",
                "chat_id": chat_id,
                "message_id": message_id,
                "disable_notification": disable_notification,
                "only_for_self": only_for_self,
            }
        )

    async def unpinChatMessage(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a pinned message from a chat; requires can\_pin\_messages member right if the chat is a basic group or supergroup, or can\_edit\_messages administrator right if the chat is a channel

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_id (:class:`int`):
                Identifier of the removed pinned message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "unpinChatMessage", "chat_id": chat_id, "message_id": message_id}
        )

    async def unpinAllChatMessages(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes all pinned messages from a chat; requires can\_pin\_messages member right if the chat is a basic group or supergroup, or can\_edit\_messages administrator right if the chat is a channel

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "unpinAllChatMessages", "chat_id": chat_id})

    async def unpinAllMessageThreadMessages(
        self, chat_id: int = 0, message_thread_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes all pinned messages from a forum topic; requires can\_pin\_messages member right in the supergroup

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            message_thread_id (:class:`int`):
                Message thread identifier in which messages will be unpinned

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "unpinAllMessageThreadMessages",
                "chat_id": chat_id,
                "message_thread_id": message_thread_id,
            }
        )

    async def joinChat(self, chat_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Adds the current user as a new member to a chat\. Private and secret chats can't be joined using this method\. May return an error with a message \"INVITE\_REQUEST\_SENT\" if only a join request was created

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "joinChat", "chat_id": chat_id})

    async def leaveChat(self, chat_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Removes the current user from chat members\. Private and secret chats can't be left using this method

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "leaveChat", "chat_id": chat_id})

    async def addChatMember(
        self, chat_id: int = 0, user_id: int = 0, forward_limit: int = 0
    ) -> Union["types.Error", "types.FailedToAddMembers"]:
        r"""Adds a new member to a chat; requires can\_invite\_users member right\. Members can't be added to private or secret chats\. Returns information about members that weren't added

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            user_id (:class:`int`):
                Identifier of the user

            forward_limit (:class:`int`):
                The number of earlier messages from the chat to be forwarded to the new member; up to 100\. Ignored for supergroups and channels, or if the added user is a bot

        Returns:
            :class:`~pytdbot.types.FailedToAddMembers`
        """

        return await self.invoke(
            {
                "@type": "addChatMember",
                "chat_id": chat_id,
                "user_id": user_id,
                "forward_limit": forward_limit,
            }
        )

    async def addChatMembers(
        self, chat_id: int = 0, user_ids: List[int] = None
    ) -> Union["types.Error", "types.FailedToAddMembers"]:
        r"""Adds multiple new members to a chat; requires can\_invite\_users member right\. Currently, this method is only available for supergroups and channels\. This method can't be used to join a chat\. Members can't be added to a channel if it has more than 200 members\. Returns information about members that weren't added

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            user_ids (:class:`List[int]`):
                Identifiers of the users to be added to the chat\. The maximum number of added users is 20 for supergroups and 100 for channels

        Returns:
            :class:`~pytdbot.types.FailedToAddMembers`
        """

        return await self.invoke(
            {"@type": "addChatMembers", "chat_id": chat_id, "user_ids": user_ids}
        )

    async def setChatMemberStatus(
        self,
        chat_id: int = 0,
        member_id: "types.MessageSender" = None,
        status: "types.ChatMemberStatus" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the status of a chat member; requires can\_invite\_users member right to add a chat member, can\_promote\_members administrator right to change administrator rights of the member, and can\_restrict\_members administrator right to change restrictions of a user\. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead\. Use addChatMember or banChatMember if some additional parameters needs to be passed

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            member_id (:class:`"types.MessageSender"`):
                Member identifier\. Chats can be only banned and unbanned in supergroups and channels

            status (:class:`"types.ChatMemberStatus"`):
                The new status of the member in the chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatMemberStatus",
                "chat_id": chat_id,
                "member_id": member_id,
                "status": status,
            }
        )

    async def banChatMember(
        self,
        chat_id: int = 0,
        member_id: "types.MessageSender" = None,
        banned_until_date: int = 0,
        revoke_messages: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Bans a member in a chat; requires can\_restrict\_members administrator right\. Members can't be banned in private or secret chats\. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc\., unless unbanned first

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            member_id (:class:`"types.MessageSender"`):
                Member identifier

            banned_until_date (:class:`int`):
                Point in time \(Unix timestamp\) when the user will be unbanned; 0 if never\. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever\. Ignored in basic groups and if a chat is banned

            revoke_messages (:class:`bool`):
                Pass true to delete all messages in the chat for the user that is being removed\. Always true for supergroups and channels

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "banChatMember",
                "chat_id": chat_id,
                "member_id": member_id,
                "banned_until_date": banned_until_date,
                "revoke_messages": revoke_messages,
            }
        )

    async def canTransferOwnership(
        self,
    ) -> Union["types.Error", "types.CanTransferOwnershipResult"]:
        r"""Checks whether the current session can be used to transfer a chat ownership to another user

        Returns:
            :class:`~pytdbot.types.CanTransferOwnershipResult`
        """

        return await self.invoke(
            {
                "@type": "canTransferOwnership",
            }
        )

    async def transferChatOwnership(
        self, chat_id: int = 0, user_id: int = 0, password: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the owner of a chat; requires owner privileges in the chat\. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session\. Available only for supergroups and channel chats

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            user_id (:class:`int`):
                Identifier of the user to which transfer the ownership\. The ownership can't be transferred to a bot or to a deleted user

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "transferChatOwnership",
                "chat_id": chat_id,
                "user_id": user_id,
                "password": password,
            }
        )

    async def getChatMember(
        self, chat_id: int = 0, member_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.ChatMember"]:
        r"""Returns information about a single member of a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            member_id (:class:`"types.MessageSender"`):
                Member identifier

        Returns:
            :class:`~pytdbot.types.ChatMember`
        """

        return await self.invoke(
            {"@type": "getChatMember", "chat_id": chat_id, "member_id": member_id}
        )

    async def searchChatMembers(
        self,
        chat_id: int = 0,
        query: str = "",
        limit: int = 0,
        filter: "types.ChatMembersFilter" = None,
    ) -> Union["types.Error", "types.ChatMembers"]:
        r"""Searches for a specified query in the first name, last name and usernames of the members of a specified chat\. Requires administrator rights if the chat is a channel

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            query (:class:`str`):
                Query to search for

            limit (:class:`int`):
                The maximum number of users to be returned; up to 200

            filter (:class:`"types.ChatMembersFilter"`):
                The type of users to search for; pass null to search among all chat members

        Returns:
            :class:`~pytdbot.types.ChatMembers`
        """

        return await self.invoke(
            {
                "@type": "searchChatMembers",
                "chat_id": chat_id,
                "query": query,
                "limit": limit,
                "filter": filter,
            }
        )

    async def getChatAdministrators(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatAdministrators"]:
        r"""Returns a list of administrators of the chat with their custom titles

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatAdministrators`
        """

        return await self.invoke({"@type": "getChatAdministrators", "chat_id": chat_id})

    async def clearAllDraftMessages(
        self, exclude_secret_chats: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Clears message drafts in all chats

        Parameters:
            exclude_secret_chats (:class:`bool`):
                Pass true to keep local message drafts in secret chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearAllDraftMessages",
                "exclude_secret_chats": exclude_secret_chats,
            }
        )

    async def getSavedNotificationSound(
        self, notification_sound_id: int = 0
    ) -> Union["types.Error", "types.NotificationSounds"]:
        r"""Returns saved notification sound by its identifier\. Returns a 404 error if there is no saved notification sound with the specified identifier

        Parameters:
            notification_sound_id (:class:`int`):
                Identifier of the notification sound

        Returns:
            :class:`~pytdbot.types.NotificationSounds`
        """

        return await self.invoke(
            {
                "@type": "getSavedNotificationSound",
                "notification_sound_id": notification_sound_id,
            }
        )

    async def getSavedNotificationSounds(
        self,
    ) -> Union["types.Error", "types.NotificationSounds"]:
        r"""Returns the list of saved notification sounds\. If a sound isn't in the list, then default sound needs to be used

        Returns:
            :class:`~pytdbot.types.NotificationSounds`
        """

        return await self.invoke(
            {
                "@type": "getSavedNotificationSounds",
            }
        )

    async def addSavedNotificationSound(
        self, sound: "types.InputFile" = None
    ) -> Union["types.Error", "types.NotificationSound"]:
        r"""Adds a new notification sound to the list of saved notification sounds\. The new notification sound is added to the top of the list\. If it is already in the list, its position isn't changed

        Parameters:
            sound (:class:`"types.InputFile"`):
                Notification sound file to add

        Returns:
            :class:`~pytdbot.types.NotificationSound`
        """

        return await self.invoke({"@type": "addSavedNotificationSound", "sound": sound})

    async def removeSavedNotificationSound(
        self, notification_sound_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a notification sound from the list of saved notification sounds

        Parameters:
            notification_sound_id (:class:`int`):
                Identifier of the notification sound

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeSavedNotificationSound",
                "notification_sound_id": notification_sound_id,
            }
        )

    async def getChatNotificationSettingsExceptions(
        self,
        scope: "types.NotificationSettingsScope" = None,
        compare_sound: bool = False,
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns the list of chats with non\-default notification settings for new messages

        Parameters:
            scope (:class:`"types.NotificationSettingsScope"`):
                If specified, only chats from the scope will be returned; pass null to return chats from all scopes

            compare_sound (:class:`bool`):
                Pass true to include in the response chats with only non\-default sound

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getChatNotificationSettingsExceptions",
                "scope": scope,
                "compare_sound": compare_sound,
            }
        )

    async def getScopeNotificationSettings(
        self, scope: "types.NotificationSettingsScope" = None
    ) -> Union["types.Error", "types.ScopeNotificationSettings"]:
        r"""Returns the notification settings for chats of a given type

        Parameters:
            scope (:class:`"types.NotificationSettingsScope"`):
                Types of chats for which to return the notification settings information

        Returns:
            :class:`~pytdbot.types.ScopeNotificationSettings`
        """

        return await self.invoke(
            {"@type": "getScopeNotificationSettings", "scope": scope}
        )

    async def setScopeNotificationSettings(
        self,
        scope: "types.NotificationSettingsScope" = None,
        notification_settings: "types.ScopeNotificationSettings" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes notification settings for chats of a given type

        Parameters:
            scope (:class:`"types.NotificationSettingsScope"`):
                Types of chats for which to change the notification settings

            notification_settings (:class:`"types.ScopeNotificationSettings"`):
                The new notification settings for the given scope

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setScopeNotificationSettings",
                "scope": scope,
                "notification_settings": notification_settings,
            }
        )

    async def setReactionNotificationSettings(
        self, notification_settings: "types.ReactionNotificationSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes notification settings for reactions

        Parameters:
            notification_settings (:class:`"types.ReactionNotificationSettings"`):
                The new notification settings for reactions

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setReactionNotificationSettings",
                "notification_settings": notification_settings,
            }
        )

    async def resetAllNotificationSettings(self) -> Union["types.Error", "types.Ok"]:
        r"""Resets all chat and scope notification settings to their default values\. By default, all chats are unmuted and message previews are shown

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "resetAllNotificationSettings",
            }
        )

    async def toggleChatIsPinned(
        self,
        chat_list: "types.ChatList" = None,
        chat_id: int = 0,
        is_pinned: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the pinned state of a chat\. There can be up to getOption\(\"pinned\_chat\_count\_max\"\)/getOption\(\"pinned\_archived\_chat\_count\_max\"\) pinned non\-secret chats and the same number of secret chats in the main/archive chat list\. The limit can be increased with Telegram Premium

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                Chat list in which to change the pinned state of the chat

            chat_id (:class:`int`):
                Chat identifier

            is_pinned (:class:`bool`):
                Pass true to pin the chat; pass false to unpin it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatIsPinned",
                "chat_list": chat_list,
                "chat_id": chat_id,
                "is_pinned": is_pinned,
            }
        )

    async def setPinnedChats(
        self, chat_list: "types.ChatList" = None, chat_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of pinned chats

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                Chat list in which to change the order of pinned chats

            chat_ids (:class:`List[int]`):
                The new list of pinned chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setPinnedChats", "chat_list": chat_list, "chat_ids": chat_ids}
        )

    async def readChatList(
        self, chat_list: "types.ChatList" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Traverse all chats in a chat list and marks all messages in the chats as read

        Parameters:
            chat_list (:class:`"types.ChatList"`):
                Chat list in which to mark all chats as read

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "readChatList", "chat_list": chat_list})

    async def getCurrentWeather(
        self, location: "types.Location" = None
    ) -> Union["types.Error", "types.CurrentWeather"]:
        r"""Returns the current weather in the given location

        Parameters:
            location (:class:`"types.Location"`):
                The location

        Returns:
            :class:`~pytdbot.types.CurrentWeather`
        """

        return await self.invoke({"@type": "getCurrentWeather", "location": location})

    async def getStory(
        self, story_sender_chat_id: int = 0, story_id: int = 0, only_local: bool = False
    ) -> Union["types.Error", "types.Story"]:
        r"""Returns a story

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Story identifier

            only_local (:class:`bool`):
                Pass true to get only locally available information without sending network requests

        Returns:
            :class:`~pytdbot.types.Story`
        """

        return await self.invoke(
            {
                "@type": "getStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "only_local": only_local,
            }
        )

    async def getChatsToSendStories(self) -> Union["types.Error", "types.Chats"]:
        r"""Returns supergroup and channel chats in which the current user has the right to post stories\. The chats must be rechecked with canSendStory before actually trying to post a story there

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getChatsToSendStories",
            }
        )

    async def canSendStory(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.CanSendStoryResult"]:
        r"""Checks whether the current user can send a story on behalf of a chat; requires can\_post\_stories right for supergroup and channel chats

        Parameters:
            chat_id (:class:`int`):
                Chat identifier\. Pass Saved Messages chat identifier when posting a story on behalf of the current user

        Returns:
            :class:`~pytdbot.types.CanSendStoryResult`
        """

        return await self.invoke({"@type": "canSendStory", "chat_id": chat_id})

    async def sendStory(
        self,
        chat_id: int = 0,
        content: "types.InputStoryContent" = None,
        areas: "types.InputStoryAreas" = None,
        caption: "types.FormattedText" = None,
        privacy_settings: "types.StoryPrivacySettings" = None,
        active_period: int = 0,
        from_story_full_id: "types.StoryFullId" = None,
        is_posted_to_chat_page: bool = False,
        protect_content: bool = False,
    ) -> Union["types.Error", "types.Story"]:
        r"""Sends a new story to a chat; requires can\_post\_stories right for supergroup and channel chats\. Returns a temporary story

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat that will post the story\. Pass Saved Messages chat identifier when posting a story on behalf of the current user

            content (:class:`"types.InputStoryContent"`):
                Content of the story

            areas (:class:`"types.InputStoryAreas"`):
                Clickable rectangle areas to be shown on the story media; pass null if none

            caption (:class:`"types.FormattedText"`):
                Story caption; pass null to use an empty caption; 0\-getOption\(\"story\_caption\_length\_max\"\) characters; can have entities only if getOption\(\"can\_use\_text\_entities\_in\_story\_caption\"\)

            privacy_settings (:class:`"types.StoryPrivacySettings"`):
                The privacy settings for the story; ignored for stories sent to supergroup and channel chats

            active_period (:class:`int`):
                Period after which the story is moved to archive, in seconds; must be one of 6 \* 3600, 12 \* 3600, 86400, or 2 \* 86400 for Telegram Premium users, and 86400 otherwise

            from_story_full_id (:class:`"types.StoryFullId"`):
                Full identifier of the original story, which content was used to create the story; pass null if the story isn't repost of another story

            is_posted_to_chat_page (:class:`bool`):
                Pass true to keep the story accessible after expiration

            protect_content (:class:`bool`):
                Pass true if the content of the story must be protected from forwarding and screenshotting

        Returns:
            :class:`~pytdbot.types.Story`
        """

        return await self.invoke(
            {
                "@type": "sendStory",
                "chat_id": chat_id,
                "content": content,
                "areas": areas,
                "caption": caption,
                "privacy_settings": privacy_settings,
                "active_period": active_period,
                "from_story_full_id": from_story_full_id,
                "is_posted_to_chat_page": is_posted_to_chat_page,
                "protect_content": protect_content,
            }
        )

    async def editStory(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        content: "types.InputStoryContent" = None,
        areas: "types.InputStoryAreas" = None,
        caption: "types.FormattedText" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes content and caption of a story\. Can be called only if story\.can\_be\_edited \=\= true

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Identifier of the story to edit

            content (:class:`"types.InputStoryContent"`):
                New content of the story; pass null to keep the current content

            areas (:class:`"types.InputStoryAreas"`):
                New clickable rectangle areas to be shown on the story media; pass null to keep the current areas\. Areas can't be edited if story content isn't changed

            caption (:class:`"types.FormattedText"`):
                New story caption; pass null to keep the current caption

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "content": content,
                "areas": areas,
                "caption": caption,
            }
        )

    async def editStoryCover(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        cover_frame_timestamp: float = 0.0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes cover of a video story\. Can be called only if story\.can\_be\_edited \=\= true and the story isn't being edited now

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Identifier of the story to edit

            cover_frame_timestamp (:class:`float`):
                New timestamp of the frame, which will be used as video thumbnail

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editStoryCover",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "cover_frame_timestamp": cover_frame_timestamp,
            }
        )

    async def setStoryPrivacySettings(
        self, story_id: int = 0, privacy_settings: "types.StoryPrivacySettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes privacy settings of a story\. The method can be called only for stories posted on behalf of the current user and if story\.can\_be\_edited \=\= true

        Parameters:
            story_id (:class:`int`):
                Identifier of the story

            privacy_settings (:class:`"types.StoryPrivacySettings"`):
                The new privacy settings for the story

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setStoryPrivacySettings",
                "story_id": story_id,
                "privacy_settings": privacy_settings,
            }
        )

    async def toggleStoryIsPostedToChatPage(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        is_posted_to_chat_page: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a story is accessible after expiration\. Can be called only if story\.can\_toggle\_is\_posted\_to\_chat\_page \=\= true

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Identifier of the story

            is_posted_to_chat_page (:class:`bool`):
                Pass true to make the story accessible after expiration; pass false to make it private

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleStoryIsPostedToChatPage",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "is_posted_to_chat_page": is_posted_to_chat_page,
            }
        )

    async def deleteStory(
        self, story_sender_chat_id: int = 0, story_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a previously sent story\. Can be called only if story\.can\_be\_deleted \=\= true

        Parameters:
            story_sender_chat_id (:class:`int`):
                Identifier of the chat that posted the story

            story_id (:class:`int`):
                Identifier of the story to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
            }
        )

    async def getStoryNotificationSettingsExceptions(
        self,
    ) -> Union["types.Error", "types.Chats"]:
        r"""Returns the list of chats with non\-default notification settings for stories

        Returns:
            :class:`~pytdbot.types.Chats`
        """

        return await self.invoke(
            {
                "@type": "getStoryNotificationSettingsExceptions",
            }
        )

    async def loadActiveStories(
        self, story_list: "types.StoryList" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Loads more active stories from a story list\. The loaded stories will be sent through updates\. Active stories are sorted by the pair \(active\_stories\.order, active\_stories\.story\_sender\_chat\_id\) in descending order\. Returns a 404 error if all active stories have been loaded

        Parameters:
            story_list (:class:`"types.StoryList"`):
                The story list in which to load active stories

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "loadActiveStories", "story_list": story_list}
        )

    async def setChatActiveStoriesList(
        self, chat_id: int = 0, story_list: "types.StoryList" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes story list in which stories from the chat are shown

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat that posted stories

            story_list (:class:`"types.StoryList"`):
                New list for active stories posted by the chat

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatActiveStoriesList",
                "chat_id": chat_id,
                "story_list": story_list,
            }
        )

    async def getChatActiveStories(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatActiveStories"]:
        r"""Returns the list of active stories posted by the given chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatActiveStories`
        """

        return await self.invoke({"@type": "getChatActiveStories", "chat_id": chat_id})

    async def getChatPostedToChatPageStories(
        self, chat_id: int = 0, from_story_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.Stories"]:
        r"""Returns the list of stories that posted by the given chat to its chat page\. If from\_story\_id \=\= 0, then pinned stories are returned first\. Then, stories are returned in reverse chronological order \(i\.e\., in order of decreasing story\_id\)\. For optimal performance, the number of returned stories is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            from_story_id (:class:`int`):
                Identifier of the story starting from which stories must be returned; use 0 to get results from pinned and the newest story

            limit (:class:`int`):
                The maximum number of stories to be returned\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.Stories`
        """

        return await self.invoke(
            {
                "@type": "getChatPostedToChatPageStories",
                "chat_id": chat_id,
                "from_story_id": from_story_id,
                "limit": limit,
            }
        )

    async def getChatArchivedStories(
        self, chat_id: int = 0, from_story_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.Stories"]:
        r"""Returns the list of all stories posted by the given chat; requires can\_edit\_stories right in the chat\. The stories are returned in reverse chronological order \(i\.e\., in order of decreasing story\_id\)\. For optimal performance, the number of returned stories is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            from_story_id (:class:`int`):
                Identifier of the story starting from which stories must be returned; use 0 to get results from the last story

            limit (:class:`int`):
                The maximum number of stories to be returned\. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.Stories`
        """

        return await self.invoke(
            {
                "@type": "getChatArchivedStories",
                "chat_id": chat_id,
                "from_story_id": from_story_id,
                "limit": limit,
            }
        )

    async def setChatPinnedStories(
        self, chat_id: int = 0, story_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the list of pinned stories on a chat page; requires can\_edit\_stories right in the chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat that posted the stories

            story_ids (:class:`List[int]`):
                New list of pinned stories\. All stories must be posted to the chat page first\. There can be up to getOption\(\"pinned\_story\_count\_max\"\) pinned stories on a chat page

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatPinnedStories",
                "chat_id": chat_id,
                "story_ids": story_ids,
            }
        )

    async def openStory(
        self, story_sender_chat_id: int = 0, story_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that a story is opened and is being viewed by the user

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the opened story

            story_id (:class:`int`):
                The identifier of the story

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "openStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
            }
        )

    async def closeStory(
        self, story_sender_chat_id: int = 0, story_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that a story is closed by the user

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the story to close

            story_id (:class:`int`):
                The identifier of the story

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "closeStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
            }
        )

    async def getStoryAvailableReactions(
        self, row_size: int = 0
    ) -> Union["types.Error", "types.AvailableReactions"]:
        r"""Returns reactions, which can be chosen for a story

        Parameters:
            row_size (:class:`int`):
                Number of reaction per row, 5\-25

        Returns:
            :class:`~pytdbot.types.AvailableReactions`
        """

        return await self.invoke(
            {"@type": "getStoryAvailableReactions", "row_size": row_size}
        )

    async def setStoryReaction(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        reaction_type: "types.ReactionType" = None,
        update_recent_reactions: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes chosen reaction on a story that has already been sent

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the story

            story_id (:class:`int`):
                The identifier of the story

            reaction_type (:class:`"types.ReactionType"`):
                Type of the reaction to set; pass null to remove the reaction\. Custom emoji reactions can be used only by Telegram Premium users\. Paid reactions can't be set

            update_recent_reactions (:class:`bool`):
                Pass true if the reaction needs to be added to recent reactions

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setStoryReaction",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "reaction_type": reaction_type,
                "update_recent_reactions": update_recent_reactions,
            }
        )

    async def getStoryInteractions(
        self,
        story_id: int = 0,
        query: str = "",
        only_contacts: bool = False,
        prefer_forwards: bool = False,
        prefer_with_reaction: bool = False,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.StoryInteractions"]:
        r"""Returns interactions with a story\. The method can be called only for stories posted on behalf of the current user

        Parameters:
            story_id (:class:`int`):
                Story identifier

            query (:class:`str`):
                Query to search for in names, usernames and titles; may be empty to get all relevant interactions

            only_contacts (:class:`bool`):
                Pass true to get only interactions by contacts; pass false to get all relevant interactions

            prefer_forwards (:class:`bool`):
                Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date

            prefer_with_reaction (:class:`bool`):
                Pass true to get interactions with reaction first; pass false to get interactions sorted just by interaction date\. Ignored if prefer\_forwards \=\= true

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of story interactions to return

        Returns:
            :class:`~pytdbot.types.StoryInteractions`
        """

        return await self.invoke(
            {
                "@type": "getStoryInteractions",
                "story_id": story_id,
                "query": query,
                "only_contacts": only_contacts,
                "prefer_forwards": prefer_forwards,
                "prefer_with_reaction": prefer_with_reaction,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getChatStoryInteractions(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        reaction_type: "types.ReactionType" = None,
        prefer_forwards: bool = False,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.StoryInteractions"]:
        r"""Returns interactions with a story posted in a chat\. Can be used only if story is posted on behalf of a chat and the user is an administrator in the chat

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the story

            story_id (:class:`int`):
                Story identifier

            reaction_type (:class:`"types.ReactionType"`):
                Pass the default heart reaction or a suggested reaction type to receive only interactions with the specified reaction type; pass null to receive all interactions; reactionTypePaid isn't supported

            prefer_forwards (:class:`bool`):
                Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of story interactions to return

        Returns:
            :class:`~pytdbot.types.StoryInteractions`
        """

        return await self.invoke(
            {
                "@type": "getChatStoryInteractions",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "reaction_type": reaction_type,
                "prefer_forwards": prefer_forwards,
                "offset": offset,
                "limit": limit,
            }
        )

    async def reportStory(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        option_id: bytes = b"",
        text: str = "",
    ) -> Union["types.Error", "types.ReportStoryResult"]:
        r"""Reports a story to the Telegram moderators

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the story to report

            story_id (:class:`int`):
                The identifier of the story to report

            option_id (:class:`bytes`):
                Option identifier chosen by the user; leave empty for the initial request

            text (:class:`str`):
                Additional report details; 0\-1024 characters; leave empty for the initial request

        Returns:
            :class:`~pytdbot.types.ReportStoryResult`
        """

        return await self.invoke(
            {
                "@type": "reportStory",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "option_id": option_id,
                "text": text,
            }
        )

    async def activateStoryStealthMode(self) -> Union["types.Error", "types.Ok"]:
        r"""Activates stealth mode for stories, which hides all views of stories from the current user in the last \"story\_stealth\_mode\_past\_period\" seconds and for the next \"story\_stealth\_mode\_future\_period\" seconds; for Telegram Premium users only

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "activateStoryStealthMode",
            }
        )

    async def getStoryPublicForwards(
        self,
        story_sender_chat_id: int = 0,
        story_id: int = 0,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.PublicForwards"]:
        r"""Returns forwards of a story as a message to public chats and reposts by public channels\. Can be used only if the story is posted on behalf of the current user or story\.can\_get\_statistics \=\= true\. For optimal performance, the number of returned messages and stories is chosen by TDLib

        Parameters:
            story_sender_chat_id (:class:`int`):
                The identifier of the sender of the story

            story_id (:class:`int`):
                The identifier of the story

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages and stories to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.PublicForwards`
        """

        return await self.invoke(
            {
                "@type": "getStoryPublicForwards",
                "story_sender_chat_id": story_sender_chat_id,
                "story_id": story_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getChatBoostLevelFeatures(
        self, is_channel: bool = False, level: int = 0
    ) -> Union["types.Error", "types.ChatBoostLevelFeatures"]:
        r"""Returns the list of features available on the specific chat boost level\. This is an offline method

        Parameters:
            is_channel (:class:`bool`):
                Pass true to get the list of features for channels; pass false to get the list of features for supergroups

            level (:class:`int`):
                Chat boost level

        Returns:
            :class:`~pytdbot.types.ChatBoostLevelFeatures`
        """

        return await self.invoke(
            {
                "@type": "getChatBoostLevelFeatures",
                "is_channel": is_channel,
                "level": level,
            }
        )

    async def getChatBoostFeatures(
        self, is_channel: bool = False
    ) -> Union["types.Error", "types.ChatBoostFeatures"]:
        r"""Returns the list of features available for different chat boost levels\. This is an offline method

        Parameters:
            is_channel (:class:`bool`):
                Pass true to get the list of features for channels; pass false to get the list of features for supergroups

        Returns:
            :class:`~pytdbot.types.ChatBoostFeatures`
        """

        return await self.invoke(
            {"@type": "getChatBoostFeatures", "is_channel": is_channel}
        )

    async def getAvailableChatBoostSlots(
        self,
    ) -> Union["types.Error", "types.ChatBoostSlots"]:
        r"""Returns the list of available chat boost slots for the current user

        Returns:
            :class:`~pytdbot.types.ChatBoostSlots`
        """

        return await self.invoke(
            {
                "@type": "getAvailableChatBoostSlots",
            }
        )

    async def getChatBoostStatus(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatBoostStatus"]:
        r"""Returns the current boost status for a supergroup or a channel chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

        Returns:
            :class:`~pytdbot.types.ChatBoostStatus`
        """

        return await self.invoke({"@type": "getChatBoostStatus", "chat_id": chat_id})

    async def boostChat(
        self, chat_id: int = 0, slot_ids: List[int] = None
    ) -> Union["types.Error", "types.ChatBoostSlots"]:
        r"""Boosts a chat and returns the list of available chat boost slots for the current user after the boost

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            slot_ids (:class:`List[int]`):
                Identifiers of boost slots of the current user from which to apply boosts to the chat

        Returns:
            :class:`~pytdbot.types.ChatBoostSlots`
        """

        return await self.invoke(
            {"@type": "boostChat", "chat_id": chat_id, "slot_ids": slot_ids}
        )

    async def getChatBoostLink(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatBoostLink"]:
        r"""Returns an HTTPS link to boost the specified supergroup or channel chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

        Returns:
            :class:`~pytdbot.types.ChatBoostLink`
        """

        return await self.invoke({"@type": "getChatBoostLink", "chat_id": chat_id})

    async def getChatBoostLinkInfo(
        self, url: str = ""
    ) -> Union["types.Error", "types.ChatBoostLinkInfo"]:
        r"""Returns information about a link to boost a chat\. Can be called for any internal link of the type internalLinkTypeChatBoost

        Parameters:
            url (:class:`str`):
                The link to boost a chat

        Returns:
            :class:`~pytdbot.types.ChatBoostLinkInfo`
        """

        return await self.invoke({"@type": "getChatBoostLinkInfo", "url": url})

    async def getChatBoosts(
        self,
        chat_id: int = 0,
        only_gift_codes: bool = False,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundChatBoosts"]:
        r"""Returns the list of boosts applied to a chat; requires administrator rights in the chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            only_gift_codes (:class:`bool`):
                Pass true to receive only boosts received from gift codes and giveaways created by the chat

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of boosts to be returned; up to 100\. For optimal performance, the number of returned boosts can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.FoundChatBoosts`
        """

        return await self.invoke(
            {
                "@type": "getChatBoosts",
                "chat_id": chat_id,
                "only_gift_codes": only_gift_codes,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getUserChatBoosts(
        self, chat_id: int = 0, user_id: int = 0
    ) -> Union["types.Error", "types.FoundChatBoosts"]:
        r"""Returns the list of boosts applied to a chat by a given user; requires administrator rights in the chat; for bots only

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat

            user_id (:class:`int`):
                Identifier of the user

        Returns:
            :class:`~pytdbot.types.FoundChatBoosts`
        """

        return await self.invoke(
            {"@type": "getUserChatBoosts", "chat_id": chat_id, "user_id": user_id}
        )

    async def getAttachmentMenuBot(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.AttachmentMenuBot"]:
        r"""Returns information about a bot that can be added to attachment or side menu

        Parameters:
            bot_user_id (:class:`int`):
                Bot's user identifier

        Returns:
            :class:`~pytdbot.types.AttachmentMenuBot`
        """

        return await self.invoke(
            {"@type": "getAttachmentMenuBot", "bot_user_id": bot_user_id}
        )

    async def toggleBotIsAddedToAttachmentMenu(
        self,
        bot_user_id: int = 0,
        is_added: bool = False,
        allow_write_access: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds or removes a bot to attachment and side menu\. Bot can be added to the menu, only if userTypeBot\.can\_be\_added\_to\_attachment\_menu \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Bot's user identifier

            is_added (:class:`bool`):
                Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu

            allow_write_access (:class:`bool`):
                Pass true if the current user allowed the bot to send them messages\. Ignored if is\_added is false

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleBotIsAddedToAttachmentMenu",
                "bot_user_id": bot_user_id,
                "is_added": is_added,
                "allow_write_access": allow_write_access,
            }
        )

    async def getThemedEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatusCustomEmojis"]:
        r"""Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list for self status

        Returns:
            :class:`~pytdbot.types.EmojiStatusCustomEmojis`
        """

        return await self.invoke(
            {
                "@type": "getThemedEmojiStatuses",
            }
        )

    async def getRecentEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatuses"]:
        r"""Returns recent emoji statuses for self status

        Returns:
            :class:`~pytdbot.types.EmojiStatuses`
        """

        return await self.invoke(
            {
                "@type": "getRecentEmojiStatuses",
            }
        )

    async def getUpgradedGiftEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatuses"]:
        r"""Returns available upgraded gift emoji statuses for self status

        Returns:
            :class:`~pytdbot.types.EmojiStatuses`
        """

        return await self.invoke(
            {
                "@type": "getUpgradedGiftEmojiStatuses",
            }
        )

    async def getDefaultEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatusCustomEmojis"]:
        r"""Returns default emoji statuses for self status

        Returns:
            :class:`~pytdbot.types.EmojiStatusCustomEmojis`
        """

        return await self.invoke(
            {
                "@type": "getDefaultEmojiStatuses",
            }
        )

    async def clearRecentEmojiStatuses(self) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of recently used emoji statuses for self status

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearRecentEmojiStatuses",
            }
        )

    async def getThemedChatEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatusCustomEmojis"]:
        r"""Returns up to 8 emoji statuses, which must be shown in the emoji status list for chats

        Returns:
            :class:`~pytdbot.types.EmojiStatusCustomEmojis`
        """

        return await self.invoke(
            {
                "@type": "getThemedChatEmojiStatuses",
            }
        )

    async def getDefaultChatEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatusCustomEmojis"]:
        r"""Returns default emoji statuses for chats

        Returns:
            :class:`~pytdbot.types.EmojiStatusCustomEmojis`
        """

        return await self.invoke(
            {
                "@type": "getDefaultChatEmojiStatuses",
            }
        )

    async def getDisallowedChatEmojiStatuses(
        self,
    ) -> Union["types.Error", "types.EmojiStatusCustomEmojis"]:
        r"""Returns the list of emoji statuses, which can't be used as chat emoji status, even they are from a sticker set with is\_allowed\_as\_chat\_emoji\_status \=\= true

        Returns:
            :class:`~pytdbot.types.EmojiStatusCustomEmojis`
        """

        return await self.invoke(
            {
                "@type": "getDisallowedChatEmojiStatuses",
            }
        )

    async def downloadFile(
        self,
        file_id: int = 0,
        priority: int = 0,
        offset: int = 0,
        limit: int = 0,
        synchronous: bool = False,
    ) -> Union["types.Error", "types.File"]:
        r"""Downloads a file from the cloud\. Download progress and completion of the download will be notified through updateFile updates

        Parameters:
            file_id (:class:`int`):
                Identifier of the file to download

            priority (:class:`int`):
                Priority of the download \(1\-32\)\. The higher the priority, the earlier the file will be downloaded\. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first

            offset (:class:`int`):
                The starting position from which the file needs to be downloaded

            limit (:class:`int`):
                Number of bytes which need to be downloaded starting from the \"offset\" position before the download will automatically be canceled; use 0 to download without a limit

            synchronous (:class:`bool`):
                Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "downloadFile",
                "file_id": file_id,
                "priority": priority,
                "offset": offset,
                "limit": limit,
                "synchronous": synchronous,
            }
        )

    async def getFileDownloadedPrefixSize(
        self, file_id: int = 0, offset: int = 0
    ) -> Union["types.Error", "types.FileDownloadedPrefixSize"]:
        r"""Returns file downloaded prefix size from a given offset, in bytes

        Parameters:
            file_id (:class:`int`):
                Identifier of the file

            offset (:class:`int`):
                Offset from which downloaded prefix size needs to be calculated

        Returns:
            :class:`~pytdbot.types.FileDownloadedPrefixSize`
        """

        return await self.invoke(
            {
                "@type": "getFileDownloadedPrefixSize",
                "file_id": file_id,
                "offset": offset,
            }
        )

    async def cancelDownloadFile(
        self, file_id: int = 0, only_if_pending: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Stops the downloading of a file\. If a file has already been downloaded, does nothing

        Parameters:
            file_id (:class:`int`):
                Identifier of a file to stop downloading

            only_if_pending (:class:`bool`):
                Pass true to stop downloading only if it hasn't been started, i\.e\. request hasn't been sent to server

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "cancelDownloadFile",
                "file_id": file_id,
                "only_if_pending": only_if_pending,
            }
        )

    async def getSuggestedFileName(
        self, file_id: int = 0, directory: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns suggested name for saving a file in a given directory

        Parameters:
            file_id (:class:`int`):
                Identifier of the file

            directory (:class:`str`):
                Directory in which the file is expected to be saved

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getSuggestedFileName",
                "file_id": file_id,
                "directory": directory,
            }
        )

    async def preliminaryUploadFile(
        self,
        file: "types.InputFile" = None,
        file_type: "types.FileType" = None,
        priority: int = 0,
    ) -> Union["types.Error", "types.File"]:
        r"""Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes\. In all other cases there is no need to preliminary upload a file\. Updates updateFile will be used to notify about upload progress\. The upload will not be completed until the file is sent in a message

        Parameters:
            file (:class:`"types.InputFile"`):
                File to upload

            file_type (:class:`"types.FileType"`):
                File type; pass null if unknown

            priority (:class:`int`):
                Priority of the upload \(1\-32\)\. The higher the priority, the earlier the file will be uploaded\. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "preliminaryUploadFile",
                "file": file,
                "file_type": file_type,
                "priority": priority,
            }
        )

    async def cancelPreliminaryUploadFile(
        self, file_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Stops the preliminary uploading of a file\. Supported only for files uploaded by using preliminaryUploadFile

        Parameters:
            file_id (:class:`int`):
                Identifier of the file to stop uploading

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "cancelPreliminaryUploadFile", "file_id": file_id}
        )

    async def writeGeneratedFilePart(
        self, generation_id: int = 0, offset: int = 0, data: bytes = b""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Writes a part of a generated file\. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

        Parameters:
            generation_id (:class:`int`):
                The identifier of the generation process

            offset (:class:`int`):
                The offset from which to write the data to the file

            data (:class:`bytes`):
                The data to write

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "writeGeneratedFilePart",
                "generation_id": generation_id,
                "offset": offset,
                "data": data,
            }
        )

    async def setFileGenerationProgress(
        self, generation_id: int = 0, expected_size: int = 0, local_prefix_size: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib on a file generation progress

        Parameters:
            generation_id (:class:`int`):
                The identifier of the generation process

            expected_size (:class:`int`):
                Expected size of the generated file, in bytes; 0 if unknown

            local_prefix_size (:class:`int`):
                The number of bytes already generated

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setFileGenerationProgress",
                "generation_id": generation_id,
                "expected_size": expected_size,
                "local_prefix_size": local_prefix_size,
            }
        )

    async def finishFileGeneration(
        self, generation_id: int = 0, error: "types.Error" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Finishes the file generation

        Parameters:
            generation_id (:class:`int`):
                The identifier of the generation process

            error (:class:`"types.Error"`):
                If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "finishFileGeneration",
                "generation_id": generation_id,
                "error": error,
            }
        )

    async def readFilePart(
        self, file_id: int = 0, offset: int = 0, count: int = 0
    ) -> Union["types.Error", "types.FilePart"]:
        r"""Reads a part of a file from the TDLib file cache and returns read bytes\. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

        Parameters:
            file_id (:class:`int`):
                Identifier of the file\. The file must be located in the TDLib file cache

            offset (:class:`int`):
                The offset from which to read the file

            count (:class:`int`):
                Number of bytes to read\. An error will be returned if there are not enough bytes available in the file from the specified position\. Pass 0 to read all available data from the specified position

        Returns:
            :class:`~pytdbot.types.FilePart`
        """

        return await self.invoke(
            {
                "@type": "readFilePart",
                "file_id": file_id,
                "offset": offset,
                "count": count,
            }
        )

    async def deleteFile(self, file_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a file from the TDLib file cache

        Parameters:
            file_id (:class:`int`):
                Identifier of the file to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deleteFile", "file_id": file_id})

    async def addFileToDownloads(
        self, file_id: int = 0, chat_id: int = 0, message_id: int = 0, priority: int = 0
    ) -> Union["types.Error", "types.File"]:
        r"""Adds a file from a message to the list of file downloads\. Download progress and completion of the download will be notified through updateFile updates\. If message database is used, the list of file downloads is persistent across application restarts\. The downloading is independent of download using downloadFile, i\.e\. it continues if downloadFile is canceled or is used to download a part of the file

        Parameters:
            file_id (:class:`int`):
                Identifier of the file to download

            chat_id (:class:`int`):
                Chat identifier of the message with the file

            message_id (:class:`int`):
                Message identifier

            priority (:class:`int`):
                Priority of the download \(1\-32\)\. The higher the priority, the earlier the file will be downloaded\. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "addFileToDownloads",
                "file_id": file_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "priority": priority,
            }
        )

    async def toggleDownloadIsPaused(
        self, file_id: int = 0, is_paused: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes pause state of a file in the file download list

        Parameters:
            file_id (:class:`int`):
                Identifier of the downloaded file

            is_paused (:class:`bool`):
                Pass true if the download is paused

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleDownloadIsPaused",
                "file_id": file_id,
                "is_paused": is_paused,
            }
        )

    async def toggleAllDownloadsArePaused(
        self, are_paused: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes pause state of all files in the file download list

        Parameters:
            are_paused (:class:`bool`):
                Pass true to pause all downloads; pass false to unpause them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "toggleAllDownloadsArePaused", "are_paused": are_paused}
        )

    async def removeFileFromDownloads(
        self, file_id: int = 0, delete_from_cache: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a file from the file download list

        Parameters:
            file_id (:class:`int`):
                Identifier of the downloaded file

            delete_from_cache (:class:`bool`):
                Pass true to delete the file from the TDLib file cache

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeFileFromDownloads",
                "file_id": file_id,
                "delete_from_cache": delete_from_cache,
            }
        )

    async def removeAllFilesFromDownloads(
        self,
        only_active: bool = False,
        only_completed: bool = False,
        delete_from_cache: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes all files from the file download list

        Parameters:
            only_active (:class:`bool`):
                Pass true to remove only active downloads, including paused

            only_completed (:class:`bool`):
                Pass true to remove only completed downloads

            delete_from_cache (:class:`bool`):
                Pass true to delete the file from the TDLib file cache

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeAllFilesFromDownloads",
                "only_active": only_active,
                "only_completed": only_completed,
                "delete_from_cache": delete_from_cache,
            }
        )

    async def searchFileDownloads(
        self,
        query: str = "",
        only_active: bool = False,
        only_completed: bool = False,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundFileDownloads"]:
        r"""Searches for files in the file download list or recently downloaded files from the list

        Parameters:
            query (:class:`str`):
                Query to search for; may be empty to return all downloaded files

            only_active (:class:`bool`):
                Pass true to search only for active downloads, including paused

            only_completed (:class:`bool`):
                Pass true to search only for completed downloads

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of files to be returned

        Returns:
            :class:`~pytdbot.types.FoundFileDownloads`
        """

        return await self.invoke(
            {
                "@type": "searchFileDownloads",
                "query": query,
                "only_active": only_active,
                "only_completed": only_completed,
                "offset": offset,
                "limit": limit,
            }
        )

    async def setApplicationVerificationToken(
        self, verification_id: int = 0, token: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Application or reCAPTCHA verification has been completed\. Can be called before authorization

        Parameters:
            verification_id (:class:`int`):
                Unique identifier for the verification process as received from updateApplicationVerificationRequired or updateApplicationRecaptchaVerificationRequired

            token (:class:`str`):
                Play Integrity API token for the Android application, or secret from push notification for the iOS application for application verification, or reCAPTCHA token for reCAPTCHA verifications; pass an empty string to abort verification and receive error VERIFICATION\_FAILED for the request

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setApplicationVerificationToken",
                "verification_id": verification_id,
                "token": token,
            }
        )

    async def getMessageFileType(
        self, message_file_head: str = ""
    ) -> Union["types.Error", "types.MessageFileType"]:
        r"""Returns information about a file with messages exported from another application

        Parameters:
            message_file_head (:class:`str`):
                Beginning of the message file; up to 100 first lines

        Returns:
            :class:`~pytdbot.types.MessageFileType`
        """

        return await self.invoke(
            {"@type": "getMessageFileType", "message_file_head": message_file_head}
        )

    async def getMessageImportConfirmationText(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns a confirmation text to be shown to the user before starting message import

        Parameters:
            chat_id (:class:`int`):
                Identifier of a chat to which the messages will be imported\. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can\_change\_info member right

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {"@type": "getMessageImportConfirmationText", "chat_id": chat_id}
        )

    async def importMessages(
        self,
        chat_id: int = 0,
        message_file: "types.InputFile" = None,
        attached_files: List["types.InputFile"] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Imports messages exported from another app

        Parameters:
            chat_id (:class:`int`):
                Identifier of a chat to which the messages will be imported\. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can\_change\_info member right

            message_file (:class:`"types.InputFile"`):
                File with messages to import\. Only inputFileLocal and inputFileGenerated are supported\. The file must not be previously uploaded

            attached_files (:class:`List["types.InputFile"]`):
                Files used in the imported messages\. Only inputFileLocal and inputFileGenerated are supported\. The files must not be previously uploaded

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "importMessages",
                "chat_id": chat_id,
                "message_file": message_file,
                "attached_files": attached_files,
            }
        )

    async def replacePrimaryChatInviteLink(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Replaces current primary invite link for a chat with a new primary invite link\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {"@type": "replacePrimaryChatInviteLink", "chat_id": chat_id}
        )

    async def createChatInviteLink(
        self,
        chat_id: int = 0,
        name: str = "",
        expiration_date: int = 0,
        member_limit: int = 0,
        creates_join_request: bool = False,
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Creates a new invite link for a chat\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right in the chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            name (:class:`str`):
                Invite link name; 0\-32 characters

            expiration_date (:class:`int`):
                Point in time \(Unix timestamp\) when the link will expire; pass 0 if never

            member_limit (:class:`int`):
                The maximum number of chat members that can join the chat via the link simultaneously; 0\-99999; pass 0 if not limited

            creates_join_request (:class:`bool`):
                Pass true if users joining the chat via the link need to be approved by chat administrators\. In this case, member\_limit must be 0

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {
                "@type": "createChatInviteLink",
                "chat_id": chat_id,
                "name": name,
                "expiration_date": expiration_date,
                "member_limit": member_limit,
                "creates_join_request": creates_join_request,
            }
        )

    async def createChatSubscriptionInviteLink(
        self,
        chat_id: int = 0,
        name: str = "",
        subscription_pricing: "types.StarSubscriptionPricing" = None,
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Creates a new subscription invite link for a channel chat\. Requires can\_invite\_users right in the chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            name (:class:`str`):
                Invite link name; 0\-32 characters

            subscription_pricing (:class:`"types.StarSubscriptionPricing"`):
                Information about subscription plan that will be applied to the users joining the chat via the link\. Subscription period must be 2592000 in production environment, and 60 or 300 if Telegram test environment is used

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {
                "@type": "createChatSubscriptionInviteLink",
                "chat_id": chat_id,
                "name": name,
                "subscription_pricing": subscription_pricing,
            }
        )

    async def editChatInviteLink(
        self,
        chat_id: int = 0,
        invite_link: str = "",
        name: str = "",
        expiration_date: int = 0,
        member_limit: int = 0,
        creates_join_request: bool = False,
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Edits a non\-primary invite link for a chat\. Available for basic groups, supergroups, and channels\. If the link creates a subscription, then expiration\_date, member\_limit and creates\_join\_request must not be used\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link to be edited

            name (:class:`str`):
                Invite link name; 0\-32 characters

            expiration_date (:class:`int`):
                Point in time \(Unix timestamp\) when the link will expire; pass 0 if never

            member_limit (:class:`int`):
                The maximum number of chat members that can join the chat via the link simultaneously; 0\-99999; pass 0 if not limited

            creates_join_request (:class:`bool`):
                Pass true if users joining the chat via the link need to be approved by chat administrators\. In this case, member\_limit must be 0

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {
                "@type": "editChatInviteLink",
                "chat_id": chat_id,
                "invite_link": invite_link,
                "name": name,
                "expiration_date": expiration_date,
                "member_limit": member_limit,
                "creates_join_request": creates_join_request,
            }
        )

    async def editChatSubscriptionInviteLink(
        self, chat_id: int = 0, invite_link: str = "", name: str = ""
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Edits a subscription invite link for a channel chat\. Requires can\_invite\_users right in the chat for own links and owner privileges for other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link to be edited

            name (:class:`str`):
                Invite link name; 0\-32 characters

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {
                "@type": "editChatSubscriptionInviteLink",
                "chat_id": chat_id,
                "invite_link": invite_link,
                "name": name,
            }
        )

    async def getChatInviteLink(
        self, chat_id: int = 0, invite_link: str = ""
    ) -> Union["types.Error", "types.ChatInviteLink"]:
        r"""Returns information about an invite link\. Requires administrator privileges and can\_invite\_users right in the chat to get own links and owner privileges to get other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link to get

        Returns:
            :class:`~pytdbot.types.ChatInviteLink`
        """

        return await self.invoke(
            {
                "@type": "getChatInviteLink",
                "chat_id": chat_id,
                "invite_link": invite_link,
            }
        )

    async def getChatInviteLinkCounts(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.ChatInviteLinkCounts"]:
        r"""Returns the list of chat administrators with number of their invite links\. Requires owner privileges in the chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.ChatInviteLinkCounts`
        """

        return await self.invoke(
            {"@type": "getChatInviteLinkCounts", "chat_id": chat_id}
        )

    async def getChatInviteLinks(
        self,
        chat_id: int = 0,
        creator_user_id: int = 0,
        is_revoked: bool = False,
        offset_date: int = 0,
        offset_invite_link: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.ChatInviteLinks"]:
        r"""Returns invite links for a chat created by specified administrator\. Requires administrator privileges and can\_invite\_users right in the chat to get own links and owner privileges to get other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            creator_user_id (:class:`int`):
                User identifier of a chat administrator\. Must be an identifier of the current user for non\-owner

            is_revoked (:class:`bool`):
                Pass true if revoked links needs to be returned instead of active or expired

            offset_date (:class:`int`):
                Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning

            offset_invite_link (:class:`str`):
                Invite link starting after which to return invite links; use empty string to get results from the beginning

            limit (:class:`int`):
                The maximum number of invite links to return; up to 100

        Returns:
            :class:`~pytdbot.types.ChatInviteLinks`
        """

        return await self.invoke(
            {
                "@type": "getChatInviteLinks",
                "chat_id": chat_id,
                "creator_user_id": creator_user_id,
                "is_revoked": is_revoked,
                "offset_date": offset_date,
                "offset_invite_link": offset_invite_link,
                "limit": limit,
            }
        )

    async def getChatInviteLinkMembers(
        self,
        chat_id: int = 0,
        invite_link: str = "",
        only_with_expired_subscription: bool = False,
        offset_member: "types.ChatInviteLinkMember" = None,
        limit: int = 0,
    ) -> Union["types.Error", "types.ChatInviteLinkMembers"]:
        r"""Returns chat members joined a chat via an invite link\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link for which to return chat members

            only_with_expired_subscription (:class:`bool`):
                Pass true if the link is a subscription link and only members with expired subscription must be returned

            offset_member (:class:`"types.ChatInviteLinkMember"`):
                A chat member from which to return next chat members; pass null to get results from the beginning

            limit (:class:`int`):
                The maximum number of chat members to return; up to 100

        Returns:
            :class:`~pytdbot.types.ChatInviteLinkMembers`
        """

        return await self.invoke(
            {
                "@type": "getChatInviteLinkMembers",
                "chat_id": chat_id,
                "invite_link": invite_link,
                "only_with_expired_subscription": only_with_expired_subscription,
                "offset_member": offset_member,
                "limit": limit,
            }
        )

    async def revokeChatInviteLink(
        self, chat_id: int = 0, invite_link: str = ""
    ) -> Union["types.Error", "types.ChatInviteLinks"]:
        r"""Revokes invite link for a chat\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links\. If a primary link is revoked, then additionally to the revoked link returns new primary link

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link to be revoked

        Returns:
            :class:`~pytdbot.types.ChatInviteLinks`
        """

        return await self.invoke(
            {
                "@type": "revokeChatInviteLink",
                "chat_id": chat_id,
                "invite_link": invite_link,
            }
        )

    async def deleteRevokedChatInviteLink(
        self, chat_id: int = 0, invite_link: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes revoked chat invite links\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link to revoke

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteRevokedChatInviteLink",
                "chat_id": chat_id,
                "invite_link": invite_link,
            }
        )

    async def deleteAllRevokedChatInviteLinks(
        self, chat_id: int = 0, creator_user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all revoked chat invite links created by a given chat administrator\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            creator_user_id (:class:`int`):
                User identifier of a chat administrator, which links will be deleted\. Must be an identifier of the current user for non\-owner

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteAllRevokedChatInviteLinks",
                "chat_id": chat_id,
                "creator_user_id": creator_user_id,
            }
        )

    async def checkChatInviteLink(
        self, invite_link: str = ""
    ) -> Union["types.Error", "types.ChatInviteLinkInfo"]:
        r"""Checks the validity of an invite link for a chat and returns information about the corresponding chat

        Parameters:
            invite_link (:class:`str`):
                Invite link to be checked

        Returns:
            :class:`~pytdbot.types.ChatInviteLinkInfo`
        """

        return await self.invoke(
            {"@type": "checkChatInviteLink", "invite_link": invite_link}
        )

    async def joinChatByInviteLink(
        self, invite_link: str = ""
    ) -> Union["types.Error", "types.Chat"]:
        r"""Uses an invite link to add the current user to the chat if possible\. May return an error with a message \"INVITE\_REQUEST\_SENT\" if only a join request was created

        Parameters:
            invite_link (:class:`str`):
                Invite link to use

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {"@type": "joinChatByInviteLink", "invite_link": invite_link}
        )

    async def getChatJoinRequests(
        self,
        chat_id: int = 0,
        invite_link: str = "",
        query: str = "",
        offset_request: "types.ChatJoinRequest" = None,
        limit: int = 0,
    ) -> Union["types.Error", "types.ChatJoinRequests"]:
        r"""Returns pending join requests in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link for which to return join requests\. If empty, all join requests will be returned\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

            query (:class:`str`):
                A query to search for in the first names, last names and usernames of the users to return

            offset_request (:class:`"types.ChatJoinRequest"`):
                A chat join request from which to return next requests; pass null to get results from the beginning

            limit (:class:`int`):
                The maximum number of requests to join the chat to return

        Returns:
            :class:`~pytdbot.types.ChatJoinRequests`
        """

        return await self.invoke(
            {
                "@type": "getChatJoinRequests",
                "chat_id": chat_id,
                "invite_link": invite_link,
                "query": query,
                "offset_request": offset_request,
                "limit": limit,
            }
        )

    async def processChatJoinRequest(
        self, chat_id: int = 0, user_id: int = 0, approve: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Handles a pending join request in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            user_id (:class:`int`):
                Identifier of the user that sent the request

            approve (:class:`bool`):
                Pass true to approve the request; pass false to decline it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "processChatJoinRequest",
                "chat_id": chat_id,
                "user_id": user_id,
                "approve": approve,
            }
        )

    async def processChatJoinRequests(
        self, chat_id: int = 0, invite_link: str = "", approve: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Handles all pending join requests for a given link in a chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            invite_link (:class:`str`):
                Invite link for which to process join requests\. If empty, all join requests will be processed\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

            approve (:class:`bool`):
                Pass true to approve all requests; pass false to decline them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "processChatJoinRequests",
                "chat_id": chat_id,
                "invite_link": invite_link,
                "approve": approve,
            }
        )

    async def createCall(
        self,
        user_id: int = 0,
        protocol: "types.CallProtocol" = None,
        is_video: bool = False,
        group_call_id: int = 0,
    ) -> Union["types.Error", "types.CallId"]:
        r"""Creates a new call

        Parameters:
            user_id (:class:`int`):
                Identifier of the user to be called

            protocol (:class:`"types.CallProtocol"`):
                The call protocols supported by the application

            is_video (:class:`bool`):
                Pass true to create a video call

            group_call_id (:class:`int`):
                Identifier of the group call to which the user will be added after exchanging private key via the call; pass 0 if none

        Returns:
            :class:`~pytdbot.types.CallId`
        """

        return await self.invoke(
            {
                "@type": "createCall",
                "user_id": user_id,
                "protocol": protocol,
                "is_video": is_video,
                "group_call_id": group_call_id,
            }
        )

    async def acceptCall(
        self, call_id: int = 0, protocol: "types.CallProtocol" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Accepts an incoming call

        Parameters:
            call_id (:class:`int`):
                Call identifier

            protocol (:class:`"types.CallProtocol"`):
                The call protocols supported by the application

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "acceptCall", "call_id": call_id, "protocol": protocol}
        )

    async def sendCallSignalingData(
        self, call_id: int = 0, data: bytes = b""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends call signaling data

        Parameters:
            call_id (:class:`int`):
                Call identifier

            data (:class:`bytes`):
                The data

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "sendCallSignalingData", "call_id": call_id, "data": data}
        )

    async def discardCall(
        self,
        call_id: int = 0,
        is_disconnected: bool = False,
        duration: int = 0,
        is_video: bool = False,
        connection_id: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Discards a call

        Parameters:
            call_id (:class:`int`):
                Call identifier

            is_disconnected (:class:`bool`):
                Pass true if the user was disconnected

            duration (:class:`int`):
                The call duration, in seconds

            is_video (:class:`bool`):
                Pass true if the call was a video call

            connection_id (:class:`int`):
                Identifier of the connection used during the call

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "discardCall",
                "call_id": call_id,
                "is_disconnected": is_disconnected,
                "duration": duration,
                "is_video": is_video,
                "connection_id": connection_id,
            }
        )

    async def sendCallRating(
        self,
        call_id: int = 0,
        rating: int = 0,
        comment: str = "",
        problems: List["types.CallProblem"] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends a call rating

        Parameters:
            call_id (:class:`int`):
                Call identifier

            rating (:class:`int`):
                Call rating; 1\-5

            comment (:class:`str`):
                An optional user comment if the rating is less than 5

            problems (:class:`List["types.CallProblem"]`):
                List of the exact types of problems with the call, specified by the user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendCallRating",
                "call_id": call_id,
                "rating": rating,
                "comment": comment,
                "problems": problems,
            }
        )

    async def sendCallDebugInformation(
        self, call_id: int = 0, debug_information: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends debug information for a call to Telegram servers

        Parameters:
            call_id (:class:`int`):
                Call identifier

            debug_information (:class:`str`):
                Debug information in application\-specific format

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendCallDebugInformation",
                "call_id": call_id,
                "debug_information": debug_information,
            }
        )

    async def sendCallLog(
        self, call_id: int = 0, log_file: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends log file for a call to Telegram servers

        Parameters:
            call_id (:class:`int`):
                Call identifier

            log_file (:class:`"types.InputFile"`):
                Call log file\. Only inputFileLocal and inputFileGenerated are supported

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "sendCallLog", "call_id": call_id, "log_file": log_file}
        )

    async def getVideoChatAvailableParticipants(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.MessageSenders"]:
        r"""Returns the list of participant identifiers, on whose behalf a video chat in the chat can be joined

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.MessageSenders`
        """

        return await self.invoke(
            {"@type": "getVideoChatAvailableParticipants", "chat_id": chat_id}
        )

    async def setVideoChatDefaultParticipant(
        self, chat_id: int = 0, default_participant_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes default participant identifier, on whose behalf a video chat in the chat will be joined

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            default_participant_id (:class:`"types.MessageSender"`):
                Default group call participant identifier to join the video chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setVideoChatDefaultParticipant",
                "chat_id": chat_id,
                "default_participant_id": default_participant_id,
            }
        )

    async def createVideoChat(
        self,
        chat_id: int = 0,
        title: str = "",
        start_date: int = 0,
        is_rtmp_stream: bool = False,
    ) -> Union["types.Error", "types.GroupCallId"]:
        r"""Creates a video chat \(a group call bound to a chat\)\. Available only for basic groups, supergroups and channels; requires can\_manage\_video\_chats administrator right

        Parameters:
            chat_id (:class:`int`):
                Identifier of a chat in which the video chat will be created

            title (:class:`str`):
                Group call title; if empty, chat title will be used

            start_date (:class:`int`):
                Point in time \(Unix timestamp\) when the group call is expected to be started by an administrator; 0 to start the video chat immediately\. The date must be at least 10 seconds and at most 8 days in the future

            is_rtmp_stream (:class:`bool`):
                Pass true to create an RTMP stream instead of an ordinary video chat

        Returns:
            :class:`~pytdbot.types.GroupCallId`
        """

        return await self.invoke(
            {
                "@type": "createVideoChat",
                "chat_id": chat_id,
                "title": title,
                "start_date": start_date,
                "is_rtmp_stream": is_rtmp_stream,
            }
        )

    async def createGroupCall(
        self, call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Creates a group call from a one\-to\-one call

        Parameters:
            call_id (:class:`int`):
                Call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "createGroupCall", "call_id": call_id})

    async def getVideoChatRtmpUrl(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.RtmpUrl"]:
        r"""Returns RTMP URL for streaming to the chat; requires can\_manage\_video\_chats administrator right

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.RtmpUrl`
        """

        return await self.invoke({"@type": "getVideoChatRtmpUrl", "chat_id": chat_id})

    async def replaceVideoChatRtmpUrl(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.RtmpUrl"]:
        r"""Replaces the current RTMP URL for streaming to the chat; requires owner privileges

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.RtmpUrl`
        """

        return await self.invoke(
            {"@type": "replaceVideoChatRtmpUrl", "chat_id": chat_id}
        )

    async def getGroupCall(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.GroupCall"]:
        r"""Returns information about a group call

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.GroupCall`
        """

        return await self.invoke(
            {"@type": "getGroupCall", "group_call_id": group_call_id}
        )

    async def startScheduledGroupCall(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Starts a scheduled group call

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "startScheduledGroupCall", "group_call_id": group_call_id}
        )

    async def toggleGroupCallEnabledStartNotification(
        self, group_call_id: int = 0, enabled_start_notification: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether the current user will receive a notification when the group call starts; scheduled group calls only

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            enabled_start_notification (:class:`bool`):
                New value of the enabled\_start\_notification setting

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallEnabledStartNotification",
                "group_call_id": group_call_id,
                "enabled_start_notification": enabled_start_notification,
            }
        )

    async def joinGroupCall(
        self,
        group_call_id: int = 0,
        participant_id: "types.MessageSender" = None,
        audio_source_id: int = 0,
        payload: str = "",
        is_muted: bool = False,
        is_my_video_enabled: bool = False,
        invite_hash: str = "",
        key_fingerprint: int = 0,
    ) -> Union["types.Error", "types.Text"]:
        r"""Joins an active group call\. Returns join response payload for tgcalls

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            participant_id (:class:`"types.MessageSender"`):
                Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only

            audio_source_id (:class:`int`):
                Caller audio channel synchronization source identifier; received from tgcalls

            payload (:class:`str`):
                Group call join payload; received from tgcalls

            is_muted (:class:`bool`):
                Pass true to join the call with muted microphone

            is_my_video_enabled (:class:`bool`):
                Pass true if the user's video is enabled

            invite_hash (:class:`str`):
                If non\-empty, invite hash to be used to join the group call without being muted by administrators

            key_fingerprint (:class:`int`):
                Fingerprint of the encryption key for E2E group calls not bound to a chat; pass 0 for voice chats

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "joinGroupCall",
                "group_call_id": group_call_id,
                "participant_id": participant_id,
                "audio_source_id": audio_source_id,
                "payload": payload,
                "is_muted": is_muted,
                "is_my_video_enabled": is_my_video_enabled,
                "invite_hash": invite_hash,
                "key_fingerprint": key_fingerprint,
            }
        )

    async def startGroupCallScreenSharing(
        self, group_call_id: int = 0, audio_source_id: int = 0, payload: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Starts screen sharing in a joined group call\. Returns join response payload for tgcalls

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            audio_source_id (:class:`int`):
                Screen sharing audio channel synchronization source identifier; received from tgcalls

            payload (:class:`str`):
                Group call join payload; received from tgcalls

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "startGroupCallScreenSharing",
                "group_call_id": group_call_id,
                "audio_source_id": audio_source_id,
                "payload": payload,
            }
        )

    async def toggleGroupCallScreenSharingIsPaused(
        self, group_call_id: int = 0, is_paused: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Pauses or unpauses screen sharing in a joined group call

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            is_paused (:class:`bool`):
                Pass true to pause screen sharing; pass false to unpause it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallScreenSharingIsPaused",
                "group_call_id": group_call_id,
                "is_paused": is_paused,
            }
        )

    async def endGroupCallScreenSharing(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Ends screen sharing in a joined group call

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "endGroupCallScreenSharing", "group_call_id": group_call_id}
        )

    async def setGroupCallTitle(
        self, group_call_id: int = 0, title: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets group call title\. Requires groupCall\.can\_be\_managed group call flag

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            title (:class:`str`):
                New group call title; 1\-64 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setGroupCallTitle",
                "group_call_id": group_call_id,
                "title": title,
            }
        )

    async def toggleGroupCallMuteNewParticipants(
        self, group_call_id: int = 0, mute_new_participants: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether new participants of a group call can be unmuted only by administrators of the group call\. Requires groupCall\.can\_toggle\_mute\_new\_participants group call flag

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            mute_new_participants (:class:`bool`):
                New value of the mute\_new\_participants setting

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallMuteNewParticipants",
                "group_call_id": group_call_id,
                "mute_new_participants": mute_new_participants,
            }
        )

    async def inviteGroupCallParticipants(
        self, group_call_id: int = 0, user_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Invites users to an active group call\. Sends a service message of type messageInviteVideoChatParticipants for video chats

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            user_ids (:class:`List[int]`):
                User identifiers\. At most 10 users can be invited simultaneously

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "inviteGroupCallParticipants",
                "group_call_id": group_call_id,
                "user_ids": user_ids,
            }
        )

    async def getGroupCallInviteLink(
        self, group_call_id: int = 0, can_self_unmute: bool = False
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns invite link to a video chat in a public chat

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            can_self_unmute (:class:`bool`):
                Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves\. Requires groupCall\.can\_be\_managed group call flag

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getGroupCallInviteLink",
                "group_call_id": group_call_id,
                "can_self_unmute": can_self_unmute,
            }
        )

    async def revokeGroupCallInviteLink(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Revokes invite link for a group call\. Requires groupCall\.can\_be\_managed group call flag

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "revokeGroupCallInviteLink", "group_call_id": group_call_id}
        )

    async def startGroupCallRecording(
        self,
        group_call_id: int = 0,
        title: str = "",
        record_video: bool = False,
        use_portrait_orientation: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Starts recording of an active group call\. Requires groupCall\.can\_be\_managed group call flag

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            title (:class:`str`):
                Group call recording title; 0\-64 characters

            record_video (:class:`bool`):
                Pass true to record a video file instead of an audio file

            use_portrait_orientation (:class:`bool`):
                Pass true to use portrait orientation for video instead of landscape one

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "startGroupCallRecording",
                "group_call_id": group_call_id,
                "title": title,
                "record_video": record_video,
                "use_portrait_orientation": use_portrait_orientation,
            }
        )

    async def endGroupCallRecording(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Ends recording of an active group call\. Requires groupCall\.can\_be\_managed group call flag

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "endGroupCallRecording", "group_call_id": group_call_id}
        )

    async def toggleGroupCallIsMyVideoPaused(
        self, group_call_id: int = 0, is_my_video_paused: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether current user's video is paused

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            is_my_video_paused (:class:`bool`):
                Pass true if the current user's video is paused

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallIsMyVideoPaused",
                "group_call_id": group_call_id,
                "is_my_video_paused": is_my_video_paused,
            }
        )

    async def toggleGroupCallIsMyVideoEnabled(
        self, group_call_id: int = 0, is_my_video_enabled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether current user's video is enabled

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            is_my_video_enabled (:class:`bool`):
                Pass true if the current user's video is enabled

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallIsMyVideoEnabled",
                "group_call_id": group_call_id,
                "is_my_video_enabled": is_my_video_enabled,
            }
        )

    async def setGroupCallParticipantIsSpeaking(
        self, group_call_id: int = 0, audio_source: int = 0, is_speaking: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that speaking state of a participant of an active group has changed

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            audio_source (:class:`int`):
                Group call participant's synchronization audio source identifier, or 0 for the current user

            is_speaking (:class:`bool`):
                Pass true if the user is speaking

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setGroupCallParticipantIsSpeaking",
                "group_call_id": group_call_id,
                "audio_source": audio_source,
                "is_speaking": is_speaking,
            }
        )

    async def toggleGroupCallParticipantIsMuted(
        self,
        group_call_id: int = 0,
        participant_id: "types.MessageSender" = None,
        is_muted: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            participant_id (:class:`"types.MessageSender"`):
                Participant identifier

            is_muted (:class:`bool`):
                Pass true to mute the user; pass false to unmute them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallParticipantIsMuted",
                "group_call_id": group_call_id,
                "participant_id": participant_id,
                "is_muted": is_muted,
            }
        )

    async def setGroupCallParticipantVolumeLevel(
        self,
        group_call_id: int = 0,
        participant_id: "types.MessageSender" = None,
        volume_level: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes volume level of a participant of an active group call\. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            participant_id (:class:`"types.MessageSender"`):
                Participant identifier

            volume_level (:class:`int`):
                New participant's volume level; 1\-20000 in hundreds of percents

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setGroupCallParticipantVolumeLevel",
                "group_call_id": group_call_id,
                "participant_id": participant_id,
                "volume_level": volume_level,
            }
        )

    async def toggleGroupCallParticipantIsHandRaised(
        self,
        group_call_id: int = 0,
        participant_id: "types.MessageSender" = None,
        is_hand_raised: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a group call participant hand is rased

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            participant_id (:class:`"types.MessageSender"`):
                Participant identifier

            is_hand_raised (:class:`bool`):
                Pass true if the user's hand needs to be raised\. Only self hand can be raised\. Requires groupCall\.can\_be\_managed group call flag to lower other's hand

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGroupCallParticipantIsHandRaised",
                "group_call_id": group_call_id,
                "participant_id": participant_id,
                "is_hand_raised": is_hand_raised,
            }
        )

    async def loadGroupCallParticipants(
        self, group_call_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Loads more participants of a group call\. The loaded participants will be received through updates\. Use the field groupCall\.loaded\_all\_participants to check whether all participants have already been loaded

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier\. The group call must be previously received through getGroupCall and must be joined or being joined

            limit (:class:`int`):
                The maximum number of participants to load; up to 100

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "loadGroupCallParticipants",
                "group_call_id": group_call_id,
                "limit": limit,
            }
        )

    async def leaveGroupCall(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Leaves a group call

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "leaveGroupCall", "group_call_id": group_call_id}
        )

    async def endGroupCall(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Ends a group call\. Requires groupCall\.can\_be\_managed

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "endGroupCall", "group_call_id": group_call_id}
        )

    async def getGroupCallStreams(
        self, group_call_id: int = 0
    ) -> Union["types.Error", "types.GroupCallStreams"]:
        r"""Returns information about available group call streams

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

        Returns:
            :class:`~pytdbot.types.GroupCallStreams`
        """

        return await self.invoke(
            {"@type": "getGroupCallStreams", "group_call_id": group_call_id}
        )

    async def getGroupCallStreamSegment(
        self,
        group_call_id: int = 0,
        time_offset: int = 0,
        scale: int = 0,
        channel_id: int = 0,
        video_quality: "types.GroupCallVideoQuality" = None,
    ) -> Union["types.Error", "types.FilePart"]:
        r"""Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG\-4 format for video

        Parameters:
            group_call_id (:class:`int`):
                Group call identifier

            time_offset (:class:`int`):
                Point in time when the stream segment begins; Unix timestamp in milliseconds

            scale (:class:`int`):
                Segment duration scale; 0\-1\. Segment's duration is 1000/\(2\*\*scale\) milliseconds

            channel_id (:class:`int`):
                Identifier of an audio/video channel to get as received from tgcalls

            video_quality (:class:`"types.GroupCallVideoQuality"`):
                Video quality as received from tgcalls; pass null to get the worst available quality

        Returns:
            :class:`~pytdbot.types.FilePart`
        """

        return await self.invoke(
            {
                "@type": "getGroupCallStreamSegment",
                "group_call_id": group_call_id,
                "time_offset": time_offset,
                "scale": scale,
                "channel_id": channel_id,
                "video_quality": video_quality,
            }
        )

    async def setMessageSenderBlockList(
        self,
        sender_id: "types.MessageSender" = None,
        block_list: "types.BlockList" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the block list of a message sender\. Currently, only users and supergroup chats can be blocked

        Parameters:
            sender_id (:class:`"types.MessageSender"`):
                Identifier of a message sender to block/unblock

            block_list (:class:`"types.BlockList"`):
                New block list for the message sender; pass null to unblock the message sender

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setMessageSenderBlockList",
                "sender_id": sender_id,
                "block_list": block_list,
            }
        )

    async def blockMessageSenderFromReplies(
        self,
        message_id: int = 0,
        delete_message: bool = False,
        delete_all_messages: bool = False,
        report_spam: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Blocks an original sender of a message in the Replies chat

        Parameters:
            message_id (:class:`int`):
                The identifier of an incoming message in the Replies chat

            delete_message (:class:`bool`):
                Pass true to delete the message

            delete_all_messages (:class:`bool`):
                Pass true to delete all messages from the same sender

            report_spam (:class:`bool`):
                Pass true to report the sender to the Telegram moderators

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "blockMessageSenderFromReplies",
                "message_id": message_id,
                "delete_message": delete_message,
                "delete_all_messages": delete_all_messages,
                "report_spam": report_spam,
            }
        )

    async def getBlockedMessageSenders(
        self, block_list: "types.BlockList" = None, offset: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.MessageSenders"]:
        r"""Returns users and chats that were blocked by the current user

        Parameters:
            block_list (:class:`"types.BlockList"`):
                Block list from which to return users

            offset (:class:`int`):
                Number of users and chats to skip in the result; must be non\-negative

            limit (:class:`int`):
                The maximum number of users and chats to return; up to 100

        Returns:
            :class:`~pytdbot.types.MessageSenders`
        """

        return await self.invoke(
            {
                "@type": "getBlockedMessageSenders",
                "block_list": block_list,
                "offset": offset,
                "limit": limit,
            }
        )

    async def addContact(
        self, contact: "types.Contact" = None, share_phone_number: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a user to the contact list or edits an existing contact by their user identifier

        Parameters:
            contact (:class:`"types.Contact"`):
                The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored

            share_phone_number (:class:`bool`):
                Pass true to share the current user's phone number with the new contact\. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed\. Use the field userFullInfo\.need\_phone\_number\_privacy\_exception to check whether the current user needs to be asked to share their phone number

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addContact",
                "contact": contact,
                "share_phone_number": share_phone_number,
            }
        )

    async def importContacts(
        self, contacts: List["types.Contact"] = None
    ) -> Union["types.Error", "types.ImportedContacts"]:
        r"""Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

        Parameters:
            contacts (:class:`List["types.Contact"]`):
                The list of contacts to import or edit; contacts' vCard are ignored and are not imported

        Returns:
            :class:`~pytdbot.types.ImportedContacts`
        """

        return await self.invoke({"@type": "importContacts", "contacts": contacts})

    async def getContacts(self) -> Union["types.Error", "types.Users"]:
        r"""Returns all contacts of the user

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {
                "@type": "getContacts",
            }
        )

    async def searchContacts(
        self, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Users"]:
        r"""Searches for the specified query in the first names, last names and usernames of the known user contacts

        Parameters:
            query (:class:`str`):
                Query to search for; may be empty to return all contacts

            limit (:class:`int`):
                The maximum number of users to be returned

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {"@type": "searchContacts", "query": query, "limit": limit}
        )

    async def removeContacts(
        self, user_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes users from the contact list

        Parameters:
            user_ids (:class:`List[int]`):
                Identifiers of users to be deleted

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeContacts", "user_ids": user_ids})

    async def getImportedContactCount(self) -> Union["types.Error", "types.Count"]:
        r"""Returns the total number of imported contacts

        Returns:
            :class:`~pytdbot.types.Count`
        """

        return await self.invoke(
            {
                "@type": "getImportedContactCount",
            }
        )

    async def changeImportedContacts(
        self, contacts: List["types.Contact"] = None
    ) -> Union["types.Error", "types.ImportedContacts"]:
        r"""Changes imported contacts using the list of contacts saved on the device\. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts\. Query result depends on the result of the previous query, so only one query is possible at the same time

        Parameters:
            contacts (:class:`List["types.Contact"]`):
                The new list of contacts, contact's vCard are ignored and are not imported

        Returns:
            :class:`~pytdbot.types.ImportedContacts`
        """

        return await self.invoke(
            {"@type": "changeImportedContacts", "contacts": contacts}
        )

    async def clearImportedContacts(self) -> Union["types.Error", "types.Ok"]:
        r"""Clears all imported contacts, contact list remains unchanged

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearImportedContacts",
            }
        )

    async def setCloseFriends(
        self, user_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the list of close friends of the current user

        Parameters:
            user_ids (:class:`List[int]`):
                User identifiers of close friends; the users must be contacts of the current user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setCloseFriends", "user_ids": user_ids})

    async def getCloseFriends(self) -> Union["types.Error", "types.Users"]:
        r"""Returns all close friends of the current user

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {
                "@type": "getCloseFriends",
            }
        )

    async def setUserPersonalProfilePhoto(
        self, user_id: int = 0, photo: "types.InputChatPhoto" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes a personal profile photo of a contact user

        Parameters:
            user_id (:class:`int`):
                User identifier

            photo (:class:`"types.InputChatPhoto"`):
                Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setUserPersonalProfilePhoto", "user_id": user_id, "photo": photo}
        )

    async def suggestUserProfilePhoto(
        self, user_id: int = 0, photo: "types.InputChatPhoto" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Suggests a profile photo to another regular user with common messages and allowing non\-paid messages

        Parameters:
            user_id (:class:`int`):
                User identifier

            photo (:class:`"types.InputChatPhoto"`):
                Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "suggestUserProfilePhoto", "user_id": user_id, "photo": photo}
        )

    async def toggleBotCanManageEmojiStatus(
        self, bot_user_id: int = 0, can_manage_emoji_status: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether the bot can manage emoji status of the current user

        Parameters:
            bot_user_id (:class:`int`):
                User identifier of the bot

            can_manage_emoji_status (:class:`bool`):
                Pass true if the bot is allowed to change emoji status of the user; pass false otherwise

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleBotCanManageEmojiStatus",
                "bot_user_id": bot_user_id,
                "can_manage_emoji_status": can_manage_emoji_status,
            }
        )

    async def setUserEmojiStatus(
        self, user_id: int = 0, emoji_status: "types.EmojiStatus" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the emoji status of a user; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user

            emoji_status (:class:`"types.EmojiStatus"`):
                New emoji status; pass null to switch to the default badge

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setUserEmojiStatus",
                "user_id": user_id,
                "emoji_status": emoji_status,
            }
        )

    async def searchUserByPhoneNumber(
        self, phone_number: str = "", only_local: bool = False
    ) -> Union["types.Error", "types.User"]:
        r"""Searches a user by their phone number\. Returns a 404 error if the user can't be found

        Parameters:
            phone_number (:class:`str`):
                Phone number to search for

            only_local (:class:`bool`):
                Pass true to get only locally available information without sending network requests

        Returns:
            :class:`~pytdbot.types.User`
        """

        return await self.invoke(
            {
                "@type": "searchUserByPhoneNumber",
                "phone_number": phone_number,
                "only_local": only_local,
            }
        )

    async def sharePhoneNumber(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Shares the phone number of the current user with a mutual contact\. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber

        Parameters:
            user_id (:class:`int`):
                Identifier of the user with whom to share the phone number\. The user must be a mutual contact

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "sharePhoneNumber", "user_id": user_id})

    async def getUserProfilePhotos(
        self, user_id: int = 0, offset: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.ChatPhotos"]:
        r"""Returns the profile photos of a user\. Personal and public photo aren't returned

        Parameters:
            user_id (:class:`int`):
                User identifier

            offset (:class:`int`):
                The number of photos to skip; must be non\-negative

            limit (:class:`int`):
                The maximum number of photos to be returned; up to 100

        Returns:
            :class:`~pytdbot.types.ChatPhotos`
        """

        return await self.invoke(
            {
                "@type": "getUserProfilePhotos",
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getStickerOutline(
        self,
        sticker_file_id: int = 0,
        for_animated_emoji: bool = False,
        for_clicked_animated_emoji_message: bool = False,
    ) -> Union["types.Error", "types.Outline"]:
        r"""Returns outline of a sticker\. This is an offline method\. Returns a 404 error if the outline isn't known

        Parameters:
            sticker_file_id (:class:`int`):
                File identifier of the sticker

            for_animated_emoji (:class:`bool`):
                Pass true to get the outline scaled for animated emoji

            for_clicked_animated_emoji_message (:class:`bool`):
                Pass true to get the outline scaled for clicked animated emoji message

        Returns:
            :class:`~pytdbot.types.Outline`
        """

        return await self.invoke(
            {
                "@type": "getStickerOutline",
                "sticker_file_id": sticker_file_id,
                "for_animated_emoji": for_animated_emoji,
                "for_clicked_animated_emoji_message": for_clicked_animated_emoji_message,
            }
        )

    async def getStickers(
        self,
        sticker_type: "types.StickerType" = None,
        query: str = "",
        limit: int = 0,
        chat_id: int = 0,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker\-specific keywords\. If the query is non\-empty, then favorite, recently used or trending stickers may also be returned

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the stickers to return

            query (:class:`str`):
                Search query; a space\-separated list of emojis or a keyword prefix\. If empty, returns all known installed stickers

            limit (:class:`int`):
                The maximum number of stickers to be returned

            chat_id (:class:`int`):
                Chat identifier for which to return stickers\. Available custom emoji stickers may be different for different chats

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getStickers",
                "sticker_type": sticker_type,
                "query": query,
                "limit": limit,
                "chat_id": chat_id,
            }
        )

    async def getAllStickerEmojis(
        self,
        sticker_type: "types.StickerType" = None,
        query: str = "",
        chat_id: int = 0,
        return_only_main_emoji: bool = False,
    ) -> Union["types.Error", "types.Emojis"]:
        r"""Returns unique emoji that correspond to stickers to be found by the getStickers\(sticker\_type, query, 1000000, chat\_id\)

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the stickers to search for

            query (:class:`str`):
                Search query

            chat_id (:class:`int`):
                Chat identifier for which to find stickers

            return_only_main_emoji (:class:`bool`):
                Pass true if only main emoji for each found sticker must be included in the result

        Returns:
            :class:`~pytdbot.types.Emojis`
        """

        return await self.invoke(
            {
                "@type": "getAllStickerEmojis",
                "sticker_type": sticker_type,
                "query": query,
                "chat_id": chat_id,
                "return_only_main_emoji": return_only_main_emoji,
            }
        )

    async def searchStickers(
        self,
        sticker_type: "types.StickerType" = None,
        emojis: str = "",
        query: str = "",
        input_language_codes: List[str] = None,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Searches for stickers from public sticker sets that correspond to any of the given emoji

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the stickers to return

            emojis (:class:`str`):
                Space\-separated list of emojis to search for

            query (:class:`str`):
                Query to search for; may be empty to search for emoji only

            input_language_codes (:class:`List[str]`):
                List of possible IETF language tags of the user's input language; may be empty if unknown

            offset (:class:`int`):
                The offset from which to return the stickers; must be non\-negative

            limit (:class:`int`):
                The maximum number of stickers to be returned; 0\-100

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "searchStickers",
                "sticker_type": sticker_type,
                "emojis": emojis,
                "query": query,
                "input_language_codes": input_language_codes,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getGreetingStickers(self) -> Union["types.Error", "types.Stickers"]:
        r"""Returns greeting stickers from regular sticker sets that can be used for the start page of other users

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getGreetingStickers",
            }
        )

    async def getPremiumStickers(
        self, limit: int = 0
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns premium stickers from regular sticker sets

        Parameters:
            limit (:class:`int`):
                The maximum number of stickers to be returned; 0\-100

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke({"@type": "getPremiumStickers", "limit": limit})

    async def getInstalledStickerSets(
        self, sticker_type: "types.StickerType" = None
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Returns a list of installed sticker sets

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to return

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {"@type": "getInstalledStickerSets", "sticker_type": sticker_type}
        )

    async def getArchivedStickerSets(
        self,
        sticker_type: "types.StickerType" = None,
        offset_sticker_set_id: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Returns a list of archived sticker sets

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to return

            offset_sticker_set_id (:class:`int`):
                Identifier of the sticker set from which to return the result; use 0 to get results from the beginning

            limit (:class:`int`):
                The maximum number of sticker sets to return; up to 100

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {
                "@type": "getArchivedStickerSets",
                "sticker_type": sticker_type,
                "offset_sticker_set_id": offset_sticker_set_id,
                "limit": limit,
            }
        )

    async def getTrendingStickerSets(
        self, sticker_type: "types.StickerType" = None, offset: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.TrendingStickerSets"]:
        r"""Returns a list of trending sticker sets\. For optimal performance, the number of returned sticker sets is chosen by TDLib

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to return

            offset (:class:`int`):
                The offset from which to return the sticker sets; must be non\-negative

            limit (:class:`int`):
                The maximum number of sticker sets to be returned; up to 100\. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached

        Returns:
            :class:`~pytdbot.types.TrendingStickerSets`
        """

        return await self.invoke(
            {
                "@type": "getTrendingStickerSets",
                "sticker_type": sticker_type,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getAttachedStickerSets(
        self, file_id: int = 0
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets\. Currently, only animations, photos, and videos can have attached sticker sets

        Parameters:
            file_id (:class:`int`):
                File identifier

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {"@type": "getAttachedStickerSets", "file_id": file_id}
        )

    async def getStickerSet(
        self, set_id: int = 0
    ) -> Union["types.Error", "types.StickerSet"]:
        r"""Returns information about a sticker set by its identifier

        Parameters:
            set_id (:class:`int`):
                Identifier of the sticker set

        Returns:
            :class:`~pytdbot.types.StickerSet`
        """

        return await self.invoke({"@type": "getStickerSet", "set_id": set_id})

    async def getStickerSetName(
        self, set_id: int = 0
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns name of a sticker set by its identifier

        Parameters:
            set_id (:class:`int`):
                Identifier of the sticker set

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke({"@type": "getStickerSetName", "set_id": set_id})

    async def searchStickerSet(
        self, name: str = "", ignore_cache: bool = False
    ) -> Union["types.Error", "types.StickerSet"]:
        r"""Searches for a sticker set by its name

        Parameters:
            name (:class:`str`):
                Name of the sticker set

            ignore_cache (:class:`bool`):
                Pass true to ignore local cache of sticker sets and always send a network request

        Returns:
            :class:`~pytdbot.types.StickerSet`
        """

        return await self.invoke(
            {"@type": "searchStickerSet", "name": name, "ignore_cache": ignore_cache}
        )

    async def searchInstalledStickerSets(
        self, sticker_type: "types.StickerType" = None, query: str = "", limit: int = 0
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Searches for installed sticker sets by looking for specified query in their title and name

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to search for

            query (:class:`str`):
                Query to search for

            limit (:class:`int`):
                The maximum number of sticker sets to return

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {
                "@type": "searchInstalledStickerSets",
                "sticker_type": sticker_type,
                "query": query,
                "limit": limit,
            }
        )

    async def searchStickerSets(
        self, sticker_type: "types.StickerType" = None, query: str = ""
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Searches for sticker sets by looking for specified query in their title and name\. Excludes installed sticker sets from the results

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to return

            query (:class:`str`):
                Query to search for

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {"@type": "searchStickerSets", "sticker_type": sticker_type, "query": query}
        )

    async def changeStickerSet(
        self, set_id: int = 0, is_installed: bool = False, is_archived: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Installs/uninstalls or activates/archives a sticker set

        Parameters:
            set_id (:class:`int`):
                Identifier of the sticker set

            is_installed (:class:`bool`):
                The new value of is\_installed

            is_archived (:class:`bool`):
                The new value of is\_archived\. A sticker set can't be installed and archived simultaneously

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "changeStickerSet",
                "set_id": set_id,
                "is_installed": is_installed,
                "is_archived": is_archived,
            }
        )

    async def viewTrendingStickerSets(
        self, sticker_set_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs the server that some trending sticker sets have been viewed by the user

        Parameters:
            sticker_set_ids (:class:`List[int]`):
                Identifiers of viewed trending sticker sets

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "viewTrendingStickerSets", "sticker_set_ids": sticker_set_ids}
        )

    async def reorderInstalledStickerSets(
        self,
        sticker_type: "types.StickerType" = None,
        sticker_set_ids: List[int] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the order of installed sticker sets

        Parameters:
            sticker_type (:class:`"types.StickerType"`):
                Type of the sticker sets to reorder

            sticker_set_ids (:class:`List[int]`):
                Identifiers of installed sticker sets in the new correct order

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reorderInstalledStickerSets",
                "sticker_type": sticker_type,
                "sticker_set_ids": sticker_set_ids,
            }
        )

    async def getRecentStickers(
        self, is_attached: bool = False
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns a list of recently used stickers

        Parameters:
            is_attached (:class:`bool`):
                Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {"@type": "getRecentStickers", "is_attached": is_attached}
        )

    async def addRecentSticker(
        self, is_attached: bool = False, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Manually adds a new sticker to the list of recently used stickers\. The new sticker is added to the top of the list\. If the sticker was already in the list, it is removed from the list first\. Only stickers belonging to a sticker set or in WEBP or WEBM format can be added to this list\. Emoji stickers can't be added to recent stickers

        Parameters:
            is_attached (:class:`bool`):
                Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers

            sticker (:class:`"types.InputFile"`):
                Sticker file to add

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "addRecentSticker",
                "is_attached": is_attached,
                "sticker": sticker,
            }
        )

    async def removeRecentSticker(
        self, is_attached: bool = False, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a sticker from the list of recently used stickers

        Parameters:
            is_attached (:class:`bool`):
                Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers

            sticker (:class:`"types.InputFile"`):
                Sticker file to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeRecentSticker",
                "is_attached": is_attached,
                "sticker": sticker,
            }
        )

    async def clearRecentStickers(
        self, is_attached: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of recently used stickers

        Parameters:
            is_attached (:class:`bool`):
                Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "clearRecentStickers", "is_attached": is_attached}
        )

    async def getFavoriteStickers(self) -> Union["types.Error", "types.Stickers"]:
        r"""Returns favorite stickers

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getFavoriteStickers",
            }
        )

    async def addFavoriteSticker(
        self, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a new sticker to the list of favorite stickers\. The new sticker is added to the top of the list\. If the sticker was already in the list, it is removed from the list first\. Only stickers belonging to a sticker set or in WEBP or WEBM format can be added to this list\. Emoji stickers can't be added to favorite stickers

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker file to add

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "addFavoriteSticker", "sticker": sticker})

    async def removeFavoriteSticker(
        self, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a sticker from the list of favorite stickers

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker file to delete from the list

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeFavoriteSticker", "sticker": sticker})

    async def getStickerEmojis(
        self, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Emojis"]:
        r"""Returns emoji corresponding to a sticker\. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker file identifier

        Returns:
            :class:`~pytdbot.types.Emojis`
        """

        return await self.invoke({"@type": "getStickerEmojis", "sticker": sticker})

    async def searchEmojis(
        self, text: str = "", input_language_codes: List[str] = None
    ) -> Union["types.Error", "types.EmojiKeywords"]:
        r"""Searches for emojis by keywords\. Supported only if the file database is enabled\. Order of results is unspecified

        Parameters:
            text (:class:`str`):
                Text to search for

            input_language_codes (:class:`List[str]`):
                List of possible IETF language tags of the user's input language; may be empty if unknown

        Returns:
            :class:`~pytdbot.types.EmojiKeywords`
        """

        return await self.invoke(
            {
                "@type": "searchEmojis",
                "text": text,
                "input_language_codes": input_language_codes,
            }
        )

    async def getKeywordEmojis(
        self, text: str = "", input_language_codes: List[str] = None
    ) -> Union["types.Error", "types.Emojis"]:
        r"""Return emojis matching the keyword\. Supported only if the file database is enabled\. Order of results is unspecified

        Parameters:
            text (:class:`str`):
                Text to search for

            input_language_codes (:class:`List[str]`):
                List of possible IETF language tags of the user's input language; may be empty if unknown

        Returns:
            :class:`~pytdbot.types.Emojis`
        """

        return await self.invoke(
            {
                "@type": "getKeywordEmojis",
                "text": text,
                "input_language_codes": input_language_codes,
            }
        )

    async def getEmojiCategories(
        self, type: "types.EmojiCategoryType" = None
    ) -> Union["types.Error", "types.EmojiCategories"]:
        r"""Returns available emoji categories

        Parameters:
            type (:class:`"types.EmojiCategoryType"`):
                Type of emoji categories to return; pass null to get default emoji categories

        Returns:
            :class:`~pytdbot.types.EmojiCategories`
        """

        return await self.invoke({"@type": "getEmojiCategories", "type": type})

    async def getAnimatedEmoji(
        self, emoji: str = ""
    ) -> Union["types.Error", "types.AnimatedEmoji"]:
        r"""Returns an animated emoji corresponding to a given emoji\. Returns a 404 error if the emoji has no animated emoji

        Parameters:
            emoji (:class:`str`):
                The emoji

        Returns:
            :class:`~pytdbot.types.AnimatedEmoji`
        """

        return await self.invoke({"@type": "getAnimatedEmoji", "emoji": emoji})

    async def getEmojiSuggestionsUrl(
        self, language_code: str = ""
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements\. The URL will be valid for 30 seconds after generation

        Parameters:
            language_code (:class:`str`):
                Language code for which the emoji replacements will be suggested

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {"@type": "getEmojiSuggestionsUrl", "language_code": language_code}
        )

    async def getCustomEmojiStickers(
        self, custom_emoji_ids: List[int] = None
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns the list of custom emoji stickers by their identifiers\. Stickers are returned in arbitrary order\. Only found stickers are returned

        Parameters:
            custom_emoji_ids (:class:`List[int]`):
                Identifiers of custom emoji stickers\. At most 200 custom emoji stickers can be received simultaneously

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {"@type": "getCustomEmojiStickers", "custom_emoji_ids": custom_emoji_ids}
        )

    async def getDefaultChatPhotoCustomEmojiStickers(
        self,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns default list of custom emoji stickers for placing on a chat photo

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getDefaultChatPhotoCustomEmojiStickers",
            }
        )

    async def getDefaultProfilePhotoCustomEmojiStickers(
        self,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns default list of custom emoji stickers for placing on a profile photo

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getDefaultProfilePhotoCustomEmojiStickers",
            }
        )

    async def getDefaultBackgroundCustomEmojiStickers(
        self,
    ) -> Union["types.Error", "types.Stickers"]:
        r"""Returns default list of custom emoji stickers for reply background

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getDefaultBackgroundCustomEmojiStickers",
            }
        )

    async def getSavedAnimations(self) -> Union["types.Error", "types.Animations"]:
        r"""Returns saved animations

        Returns:
            :class:`~pytdbot.types.Animations`
        """

        return await self.invoke(
            {
                "@type": "getSavedAnimations",
            }
        )

    async def addSavedAnimation(
        self, animation: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Manually adds a new animation to the list of saved animations\. The new animation is added to the beginning of the list\. If the animation was already in the list, it is removed first\. Only non\-secret video animations with MIME type \"video/mp4\" can be added to the list

        Parameters:
            animation (:class:`"types.InputFile"`):
                The animation file to be added\. Only animations known to the server \(i\.e\., successfully sent via a message\) can be added to the list

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "addSavedAnimation", "animation": animation})

    async def removeSavedAnimation(
        self, animation: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes an animation from the list of saved animations

        Parameters:
            animation (:class:`"types.InputFile"`):
                Animation file to be removed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "removeSavedAnimation", "animation": animation}
        )

    async def getRecentInlineBots(self) -> Union["types.Error", "types.Users"]:
        r"""Returns up to 20 recently used inline bots in the order of their last usage

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {
                "@type": "getRecentInlineBots",
            }
        )

    async def getOwnedBots(self) -> Union["types.Error", "types.Users"]:
        r"""Returns the list of bots owned by the current user

        Returns:
            :class:`~pytdbot.types.Users`
        """

        return await self.invoke(
            {
                "@type": "getOwnedBots",
            }
        )

    async def searchHashtags(
        self, prefix: str = "", limit: int = 0
    ) -> Union["types.Error", "types.Hashtags"]:
        r"""Searches for recently used hashtags by their prefix

        Parameters:
            prefix (:class:`str`):
                Hashtag prefix to search for

            limit (:class:`int`):
                The maximum number of hashtags to be returned

        Returns:
            :class:`~pytdbot.types.Hashtags`
        """

        return await self.invoke(
            {"@type": "searchHashtags", "prefix": prefix, "limit": limit}
        )

    async def removeRecentHashtag(
        self, hashtag: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a hashtag from the list of recently used hashtags

        Parameters:
            hashtag (:class:`str`):
                Hashtag to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeRecentHashtag", "hashtag": hashtag})

    async def getLinkPreview(
        self,
        text: "types.FormattedText" = None,
        link_preview_options: "types.LinkPreviewOptions" = None,
    ) -> Union["types.Error", "types.LinkPreview"]:
        r"""Returns a link preview by the text of a message\. Do not call this function too often\. Returns a 404 error if the text has no link preview

        Parameters:
            text (:class:`"types.FormattedText"`):
                Message text with formatting

            link_preview_options (:class:`"types.LinkPreviewOptions"`):
                Options to be used for generation of the link preview; pass null to use default link preview options

        Returns:
            :class:`~pytdbot.types.LinkPreview`
        """

        return await self.invoke(
            {
                "@type": "getLinkPreview",
                "text": text,
                "link_preview_options": link_preview_options,
            }
        )

    async def getWebPageInstantView(
        self, url: str = "", only_local: bool = False
    ) -> Union["types.Error", "types.WebPageInstantView"]:
        r"""Returns an instant view version of a web page if available\. This is an offline method if only\_local is true\. Returns a 404 error if the web page has no instant view page

        Parameters:
            url (:class:`str`):
                The web page URL

            only_local (:class:`bool`):
                Pass true to get only locally available information without sending network requests

        Returns:
            :class:`~pytdbot.types.WebPageInstantView`
        """

        return await self.invoke(
            {"@type": "getWebPageInstantView", "url": url, "only_local": only_local}
        )

    async def setProfilePhoto(
        self, photo: "types.InputChatPhoto" = None, is_public: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes a profile photo for the current user

        Parameters:
            photo (:class:`"types.InputChatPhoto"`):
                Profile photo to set

            is_public (:class:`bool`):
                Pass true to set the public photo, which will be visible even the main photo is hidden by privacy settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setProfilePhoto", "photo": photo, "is_public": is_public}
        )

    async def deleteProfilePhoto(
        self, profile_photo_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a profile photo

        Parameters:
            profile_photo_id (:class:`int`):
                Identifier of the profile photo to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteProfilePhoto", "profile_photo_id": profile_photo_id}
        )

    async def setAccentColor(
        self, accent_color_id: int = 0, background_custom_emoji_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes accent color and background custom emoji for the current user; for Telegram Premium users only

        Parameters:
            accent_color_id (:class:`int`):
                Identifier of the accent color to use

            background_custom_emoji_id (:class:`int`):
                Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setAccentColor",
                "accent_color_id": accent_color_id,
                "background_custom_emoji_id": background_custom_emoji_id,
            }
        )

    async def setProfileAccentColor(
        self,
        profile_accent_color_id: int = 0,
        profile_background_custom_emoji_id: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes accent color and background custom emoji for profile of the current user; for Telegram Premium users only

        Parameters:
            profile_accent_color_id (:class:`int`):
                Identifier of the accent color to use for profile; pass \-1 if none

            profile_background_custom_emoji_id (:class:`int`):
                Identifier of a custom emoji to be shown on the user's profile photo background; 0 if none

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setProfileAccentColor",
                "profile_accent_color_id": profile_accent_color_id,
                "profile_background_custom_emoji_id": profile_background_custom_emoji_id,
            }
        )

    async def setName(
        self, first_name: str = "", last_name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the first and last name of the current user

        Parameters:
            first_name (:class:`str`):
                The new value of the first name for the current user; 1\-64 characters

            last_name (:class:`str`):
                The new value of the optional last name for the current user; 0\-64 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setName", "first_name": first_name, "last_name": last_name}
        )

    async def setBio(self, bio: str = "") -> Union["types.Error", "types.Ok"]:
        r"""Changes the bio of the current user

        Parameters:
            bio (:class:`str`):
                The new value of the user bio; 0\-getOption\(\"bio\_length\_max\"\) characters without line feeds

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setBio", "bio": bio})

    async def setUsername(self, username: str = "") -> Union["types.Error", "types.Ok"]:
        r"""Changes the editable username of the current user

        Parameters:
            username (:class:`str`):
                The new value of the username\. Use an empty string to remove the username\. The username can't be completely removed if there is another active or disabled username

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setUsername", "username": username})

    async def toggleUsernameIsActive(
        self, username: str = "", is_active: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes active state for a username of the current user\. The editable username can't be disabled\. May return an error with a message \"USERNAMES\_ACTIVE\_TOO\_MUCH\" if the maximum number of active usernames has been reached

        Parameters:
            username (:class:`str`):
                The username to change

            is_active (:class:`bool`):
                Pass true to activate the username; pass false to disable it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleUsernameIsActive",
                "username": username,
                "is_active": is_active,
            }
        )

    async def reorderActiveUsernames(
        self, usernames: List[str] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes order of active usernames of the current user

        Parameters:
            usernames (:class:`List[str]`):
                The new order of active usernames\. All currently active usernames must be specified

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "reorderActiveUsernames", "usernames": usernames}
        )

    async def setBirthdate(
        self, birthdate: "types.Birthdate" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the birthdate of the current user

        Parameters:
            birthdate (:class:`"types.Birthdate"`):
                The new value of the current user's birthdate; pass null to remove the birthdate

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setBirthdate", "birthdate": birthdate})

    async def setPersonalChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the personal chat of the current user

        Parameters:
            chat_id (:class:`int`):
                Identifier of the new personal chat; pass 0 to remove the chat\. Use getSuitablePersonalChats to get suitable chats

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setPersonalChat", "chat_id": chat_id})

    async def setEmojiStatus(
        self, emoji_status: "types.EmojiStatus" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the emoji status of the current user; for Telegram Premium users only

        Parameters:
            emoji_status (:class:`"types.EmojiStatus"`):
                New emoji status; pass null to switch to the default badge

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setEmojiStatus", "emoji_status": emoji_status}
        )

    async def toggleHasSponsoredMessagesEnabled(
        self, has_sponsored_messages_enabled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether the current user has sponsored messages enabled\. The setting has no effect for users without Telegram Premium for which sponsored messages are always enabled

        Parameters:
            has_sponsored_messages_enabled (:class:`bool`):
                Pass true to enable sponsored messages for the current user; false to disable them

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleHasSponsoredMessagesEnabled",
                "has_sponsored_messages_enabled": has_sponsored_messages_enabled,
            }
        )

    async def setBusinessLocation(
        self, location: "types.BusinessLocation" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the business location of the current user\. Requires Telegram Business subscription

        Parameters:
            location (:class:`"types.BusinessLocation"`):
                The new location of the business; pass null to remove the location

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setBusinessLocation", "location": location})

    async def setBusinessOpeningHours(
        self, opening_hours: "types.BusinessOpeningHours" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the business opening hours of the current user\. Requires Telegram Business subscription

        Parameters:
            opening_hours (:class:`"types.BusinessOpeningHours"`):
                The new opening hours of the business; pass null to remove the opening hours; up to 28 time intervals can be specified

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setBusinessOpeningHours", "opening_hours": opening_hours}
        )

    async def setBusinessGreetingMessageSettings(
        self, greeting_message_settings: "types.BusinessGreetingMessageSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the business greeting message settings of the current user\. Requires Telegram Business subscription

        Parameters:
            greeting_message_settings (:class:`"types.BusinessGreetingMessageSettings"`):
                The new settings for the greeting message of the business; pass null to disable the greeting message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessGreetingMessageSettings",
                "greeting_message_settings": greeting_message_settings,
            }
        )

    async def setBusinessAwayMessageSettings(
        self, away_message_settings: "types.BusinessAwayMessageSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the business away message settings of the current user\. Requires Telegram Business subscription

        Parameters:
            away_message_settings (:class:`"types.BusinessAwayMessageSettings"`):
                The new settings for the away message of the business; pass null to disable the away message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBusinessAwayMessageSettings",
                "away_message_settings": away_message_settings,
            }
        )

    async def setBusinessStartPage(
        self, start_page: "types.InputBusinessStartPage" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the business start page of the current user\. Requires Telegram Business subscription

        Parameters:
            start_page (:class:`"types.InputBusinessStartPage"`):
                The new start page of the business; pass null to remove custom start page

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setBusinessStartPage", "start_page": start_page}
        )

    async def sendPhoneNumberCode(
        self,
        phone_number: str = "",
        settings: "types.PhoneNumberAuthenticationSettings" = None,
        type: "types.PhoneNumberCodeType" = None,
    ) -> Union["types.Error", "types.AuthenticationCodeInfo"]:
        r"""Sends a code to the specified phone number\. Aborts previous phone number verification if there was one\. On success, returns information about the sent code

        Parameters:
            phone_number (:class:`str`):
                The phone number, in international format

            settings (:class:`"types.PhoneNumberAuthenticationSettings"`):
                Settings for the authentication of the user's phone number; pass null to use default settings

            type (:class:`"types.PhoneNumberCodeType"`):
                Type of the request for which the code is sent

        Returns:
            :class:`~pytdbot.types.AuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "sendPhoneNumberCode",
                "phone_number": phone_number,
                "settings": settings,
                "type": type,
            }
        )

    async def sendPhoneNumberFirebaseSms(
        self, token: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends Firebase Authentication SMS to the specified phone number\. Works only when received a code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

        Parameters:
            token (:class:`str`):
                Play Integrity API or SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "sendPhoneNumberFirebaseSms", "token": token}
        )

    async def reportPhoneNumberCodeMissing(
        self, mobile_network_code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports that authentication code wasn't delivered via SMS to the specified phone number; for official mobile applications only

        Parameters:
            mobile_network_code (:class:`str`):
                Current mobile network code

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportPhoneNumberCodeMissing",
                "mobile_network_code": mobile_network_code,
            }
        )

    async def resendPhoneNumberCode(
        self, reason: "types.ResendCodeReason" = None
    ) -> Union["types.Error", "types.AuthenticationCodeInfo"]:
        r"""Resends the authentication code sent to a phone number\. Works only if the previously received authenticationCodeInfo next\_code\_type was not null and the server\-specified timeout has passed

        Parameters:
            reason (:class:`"types.ResendCodeReason"`):
                Reason of code resending; pass null if unknown

        Returns:
            :class:`~pytdbot.types.AuthenticationCodeInfo`
        """

        return await self.invoke({"@type": "resendPhoneNumberCode", "reason": reason})

    async def checkPhoneNumberCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Check the authentication code and completes the request for which the code was sent if appropriate

        Parameters:
            code (:class:`str`):
                Authentication code to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "checkPhoneNumberCode", "code": code})

    async def getBusinessConnectedBot(
        self,
    ) -> Union["types.Error", "types.BusinessConnectedBot"]:
        r"""Returns the business bot that is connected to the current user account\. Returns a 404 error if there is no connected bot

        Returns:
            :class:`~pytdbot.types.BusinessConnectedBot`
        """

        return await self.invoke(
            {
                "@type": "getBusinessConnectedBot",
            }
        )

    async def setBusinessConnectedBot(
        self, bot: "types.BusinessConnectedBot" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds or changes business bot that is connected to the current user account

        Parameters:
            bot (:class:`"types.BusinessConnectedBot"`):
                Connection settings for the bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setBusinessConnectedBot", "bot": bot})

    async def deleteBusinessConnectedBot(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes the business bot that is connected to the current user account

        Parameters:
            bot_user_id (:class:`int`):
                Unique user identifier for the bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteBusinessConnectedBot", "bot_user_id": bot_user_id}
        )

    async def toggleBusinessConnectedBotChatIsPaused(
        self, chat_id: int = 0, is_paused: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Pauses or resumes the connected business bot in a specific chat

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            is_paused (:class:`bool`):
                Pass true to pause the connected bot in the chat; pass false to resume the bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleBusinessConnectedBotChatIsPaused",
                "chat_id": chat_id,
                "is_paused": is_paused,
            }
        )

    async def removeBusinessConnectedBotFromChat(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes the connected business bot from a specific chat by adding the chat to businessRecipients\.excluded\_chat\_ids

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "removeBusinessConnectedBotFromChat", "chat_id": chat_id}
        )

    async def getBusinessChatLinks(
        self,
    ) -> Union["types.Error", "types.BusinessChatLinks"]:
        r"""Returns business chat links created for the current account

        Returns:
            :class:`~pytdbot.types.BusinessChatLinks`
        """

        return await self.invoke(
            {
                "@type": "getBusinessChatLinks",
            }
        )

    async def createBusinessChatLink(
        self, link_info: "types.InputBusinessChatLink" = None
    ) -> Union["types.Error", "types.BusinessChatLink"]:
        r"""Creates a business chat link for the current account\. Requires Telegram Business subscription\. There can be up to getOption\(\"business\_chat\_link\_count\_max\"\) links created\. Returns the created link

        Parameters:
            link_info (:class:`"types.InputBusinessChatLink"`):
                Information about the link to create

        Returns:
            :class:`~pytdbot.types.BusinessChatLink`
        """

        return await self.invoke(
            {"@type": "createBusinessChatLink", "link_info": link_info}
        )

    async def editBusinessChatLink(
        self, link: str = "", link_info: "types.InputBusinessChatLink" = None
    ) -> Union["types.Error", "types.BusinessChatLink"]:
        r"""Edits a business chat link of the current account\. Requires Telegram Business subscription\. Returns the edited link

        Parameters:
            link (:class:`str`):
                The link to edit

            link_info (:class:`"types.InputBusinessChatLink"`):
                New description of the link

        Returns:
            :class:`~pytdbot.types.BusinessChatLink`
        """

        return await self.invoke(
            {"@type": "editBusinessChatLink", "link": link, "link_info": link_info}
        )

    async def deleteBusinessChatLink(
        self, link: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a business chat link of the current account

        Parameters:
            link (:class:`str`):
                The link to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deleteBusinessChatLink", "link": link})

    async def getBusinessChatLinkInfo(
        self, link_name: str = ""
    ) -> Union["types.Error", "types.BusinessChatLinkInfo"]:
        r"""Returns information about a business chat link

        Parameters:
            link_name (:class:`str`):
                Name of the link

        Returns:
            :class:`~pytdbot.types.BusinessChatLinkInfo`
        """

        return await self.invoke(
            {"@type": "getBusinessChatLinkInfo", "link_name": link_name}
        )

    async def getUserLink(self) -> Union["types.Error", "types.UserLink"]:
        r"""Returns an HTTPS link, which can be used to get information about the current user

        Returns:
            :class:`~pytdbot.types.UserLink`
        """

        return await self.invoke(
            {
                "@type": "getUserLink",
            }
        )

    async def searchUserByToken(
        self, token: str = ""
    ) -> Union["types.Error", "types.User"]:
        r"""Searches a user by a token from the user's link

        Parameters:
            token (:class:`str`):
                Token to search for

        Returns:
            :class:`~pytdbot.types.User`
        """

        return await self.invoke({"@type": "searchUserByToken", "token": token})

    async def setCommands(
        self,
        scope: "types.BotCommandScope" = None,
        language_code: str = "",
        commands: List["types.BotCommand"] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the list of commands supported by the bot for the given user scope and language; for bots only

        Parameters:
            scope (:class:`"types.BotCommandScope"`):
                The scope to which the commands are relevant; pass null to change commands in the default bot command scope

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code\. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands

            commands (:class:`List["types.BotCommand"]`):
                List of the bot's commands

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setCommands",
                "scope": scope,
                "language_code": language_code,
                "commands": commands,
            }
        )

    async def deleteCommands(
        self, scope: "types.BotCommandScope" = None, language_code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes commands supported by the bot for the given user scope and language; for bots only

        Parameters:
            scope (:class:`"types.BotCommandScope"`):
                The scope to which the commands are relevant; pass null to delete commands in the default bot command scope

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code or an empty string

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteCommands", "scope": scope, "language_code": language_code}
        )

    async def getCommands(
        self, scope: "types.BotCommandScope" = None, language_code: str = ""
    ) -> Union["types.Error", "types.BotCommands"]:
        r"""Returns the list of commands supported by the bot for the given user scope and language; for bots only

        Parameters:
            scope (:class:`"types.BotCommandScope"`):
                The scope to which the commands are relevant; pass null to get commands in the default bot command scope

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code or an empty string

        Returns:
            :class:`~pytdbot.types.BotCommands`
        """

        return await self.invoke(
            {"@type": "getCommands", "scope": scope, "language_code": language_code}
        )

    async def setMenuButton(
        self, user_id: int = 0, menu_button: "types.BotMenuButton" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets menu button for the given user or for all users; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user or 0 to set menu button for all users

            menu_button (:class:`"types.BotMenuButton"`):
                New menu button

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setMenuButton", "user_id": user_id, "menu_button": menu_button}
        )

    async def getMenuButton(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.BotMenuButton"]:
        r"""Returns menu button set by the bot for the given user; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user or 0 to get the default menu button

        Returns:
            :class:`~pytdbot.types.BotMenuButton`
        """

        return await self.invoke({"@type": "getMenuButton", "user_id": user_id})

    async def setDefaultGroupAdministratorRights(
        self, default_group_administrator_rights: "types.ChatAdministratorRights" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

        Parameters:
            default_group_administrator_rights (:class:`"types.ChatAdministratorRights"`):
                Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setDefaultGroupAdministratorRights",
                "default_group_administrator_rights": default_group_administrator_rights,
            }
        )

    async def setDefaultChannelAdministratorRights(
        self,
        default_channel_administrator_rights: "types.ChatAdministratorRights" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets default administrator rights for adding the bot to channel chats; for bots only

        Parameters:
            default_channel_administrator_rights (:class:`"types.ChatAdministratorRights"`):
                Default administrator rights for adding the bot to channels; pass null to remove default rights

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setDefaultChannelAdministratorRights",
                "default_channel_administrator_rights": default_channel_administrator_rights,
            }
        )

    async def canBotSendMessages(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether the specified bot can send messages to the user\. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "canBotSendMessages", "bot_user_id": bot_user_id}
        )

    async def allowBotToSendMessages(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Allows the specified bot to send messages to the user

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "allowBotToSendMessages", "bot_user_id": bot_user_id}
        )

    async def sendWebAppCustomRequest(
        self, bot_user_id: int = 0, method: str = "", parameters: str = ""
    ) -> Union["types.Error", "types.CustomRequestResult"]:
        r"""Sends a custom request from a Web App

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the bot

            method (:class:`str`):
                The method name

            parameters (:class:`str`):
                JSON\-serialized method parameters

        Returns:
            :class:`~pytdbot.types.CustomRequestResult`
        """

        return await self.invoke(
            {
                "@type": "sendWebAppCustomRequest",
                "bot_user_id": bot_user_id,
                "method": method,
                "parameters": parameters,
            }
        )

    async def getBotMediaPreviews(
        self, bot_user_id: int = 0
    ) -> Union["types.Error", "types.BotMediaPreviews"]:
        r"""Returns the list of media previews of a bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must have the main Web App

        Returns:
            :class:`~pytdbot.types.BotMediaPreviews`
        """

        return await self.invoke(
            {"@type": "getBotMediaPreviews", "bot_user_id": bot_user_id}
        )

    async def getBotMediaPreviewInfo(
        self, bot_user_id: int = 0, language_code: str = ""
    ) -> Union["types.Error", "types.BotMediaPreviewInfo"]:
        r"""Returns the list of media previews for the given language and the list of languages for which the bot has dedicated previews

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must be owned and must have the main Web App

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code for which to get previews\. If empty, then default previews are returned

        Returns:
            :class:`~pytdbot.types.BotMediaPreviewInfo`
        """

        return await self.invoke(
            {
                "@type": "getBotMediaPreviewInfo",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
            }
        )

    async def addBotMediaPreview(
        self,
        bot_user_id: int = 0,
        language_code: str = "",
        content: "types.InputStoryContent" = None,
    ) -> Union["types.Error", "types.BotMediaPreview"]:
        r"""Adds a new media preview to the beginning of the list of media previews of a bot\. Returns the added preview after addition is completed server\-side\. The total number of previews must not exceed getOption\(\"bot\_media\_preview\_count\_max\"\) for the given language

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must be owned and must have the main Web App

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code for which preview is added\. If empty, then the preview will be shown to all users for whose languages there are no dedicated previews\. If non\-empty, then there must be an official language pack of the same name, which is returned by getLocalizationTargetInfo

            content (:class:`"types.InputStoryContent"`):
                Content of the added preview

        Returns:
            :class:`~pytdbot.types.BotMediaPreview`
        """

        return await self.invoke(
            {
                "@type": "addBotMediaPreview",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "content": content,
            }
        )

    async def editBotMediaPreview(
        self,
        bot_user_id: int = 0,
        language_code: str = "",
        file_id: int = 0,
        content: "types.InputStoryContent" = None,
    ) -> Union["types.Error", "types.BotMediaPreview"]:
        r"""Replaces media preview in the list of media previews of a bot\. Returns the new preview after edit is completed server\-side

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must be owned and must have the main Web App

            language_code (:class:`str`):
                Language code of the media preview to edit

            file_id (:class:`int`):
                File identifier of the media to replace

            content (:class:`"types.InputStoryContent"`):
                Content of the new preview

        Returns:
            :class:`~pytdbot.types.BotMediaPreview`
        """

        return await self.invoke(
            {
                "@type": "editBotMediaPreview",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "file_id": file_id,
                "content": content,
            }
        )

    async def reorderBotMediaPreviews(
        self, bot_user_id: int = 0, language_code: str = "", file_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes order of media previews in the list of media previews of a bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must be owned and must have the main Web App

            language_code (:class:`str`):
                Language code of the media previews to reorder

            file_ids (:class:`List[int]`):
                File identifiers of the media in the new order

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reorderBotMediaPreviews",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "file_ids": file_ids,
            }
        )

    async def deleteBotMediaPreviews(
        self, bot_user_id: int = 0, language_code: str = "", file_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Delete media previews from the list of media previews of a bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot\. The bot must be owned and must have the main Web App

            language_code (:class:`str`):
                Language code of the media previews to delete

            file_ids (:class:`List[int]`):
                File identifiers of the media to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteBotMediaPreviews",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "file_ids": file_ids,
            }
        )

    async def setBotName(
        self, bot_user_id: int = 0, language_code: str = "", name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the name of a bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code\. If empty, the name will be shown to all users for whose languages there is no dedicated name

            name (:class:`str`):
                New bot's name on the specified language; 0\-64 characters; must be non\-empty if language code is empty

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBotName",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "name": name,
            }
        )

    async def getBotName(
        self, bot_user_id: int = 0, language_code: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns the name of a bot in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code or an empty string

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getBotName",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
            }
        )

    async def setBotProfilePhoto(
        self, bot_user_id: int = 0, photo: "types.InputChatPhoto" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes a profile photo for a bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            photo (:class:`"types.InputChatPhoto"`):
                Profile photo to set; pass null to delete the chat photo

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setBotProfilePhoto", "bot_user_id": bot_user_id, "photo": photo}
        )

    async def toggleBotUsernameIsActive(
        self, bot_user_id: int = 0, username: str = "", is_active: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes active state for a username of a bot\. The editable username can't be disabled\. May return an error with a message \"USERNAMES\_ACTIVE\_TOO\_MUCH\" if the maximum number of active usernames has been reached\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            username (:class:`str`):
                The username to change

            is_active (:class:`bool`):
                Pass true to activate the username; pass false to disable it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleBotUsernameIsActive",
                "bot_user_id": bot_user_id,
                "username": username,
                "is_active": is_active,
            }
        )

    async def reorderBotActiveUsernames(
        self, bot_user_id: int = 0, usernames: List[str] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes order of active usernames of a bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            usernames (:class:`List[str]`):
                The new order of active usernames\. All currently active usernames must be specified

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reorderBotActiveUsernames",
                "bot_user_id": bot_user_id,
                "usernames": usernames,
            }
        )

    async def setBotInfoDescription(
        self, bot_user_id: int = 0, language_code: str = "", description: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the text shown in the chat with a bot if the chat is empty\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code\. If empty, the description will be shown to all users for whose languages there is no dedicated description

            description (:class:`str`):
                New bot's description on the specified language

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBotInfoDescription",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "description": description,
            }
        )

    async def getBotInfoDescription(
        self, bot_user_id: int = 0, language_code: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns the text shown in the chat with a bot if the chat is empty in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code or an empty string

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getBotInfoDescription",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
            }
        )

    async def setBotInfoShortDescription(
        self, bot_user_id: int = 0, language_code: str = "", short_description: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the text shown on a bot's profile page and sent together with the link when users share the bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code\. If empty, the short description will be shown to all users for whose languages there is no dedicated description

            short_description (:class:`str`):
                New bot's short description on the specified language

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBotInfoShortDescription",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
                "short_description": short_description,
            }
        )

    async def getBotInfoShortDescription(
        self, bot_user_id: int = 0, language_code: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns the text shown on a bot's profile page and sent together with the link when users share the bot in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the target bot

            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code or an empty string

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getBotInfoShortDescription",
                "bot_user_id": bot_user_id,
                "language_code": language_code,
            }
        )

    async def setMessageSenderBotVerification(
        self,
        bot_user_id: int = 0,
        verified_id: "types.MessageSender" = None,
        custom_description: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the verification status of a user or a chat by an owned bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the owned bot, which will verify the user or the chat

            verified_id (:class:`"types.MessageSender"`):
                Identifier of the user or the supergroup or channel chat, which will be verified by the bot

            custom_description (:class:`str`):
                Custom description of verification reason; 0\-getOption\(\"bot\_verification\_custom\_description\_length\_max\"\)\. If empty, then \"was verified by organization \"organization\_name\"\" will be used as description\. Can be specified only if the bot is allowed to provide custom description

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setMessageSenderBotVerification",
                "bot_user_id": bot_user_id,
                "verified_id": verified_id,
                "custom_description": custom_description,
            }
        )

    async def removeMessageSenderBotVerification(
        self, bot_user_id: int = 0, verified_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes the verification status of a user or a chat by an owned bot

        Parameters:
            bot_user_id (:class:`int`):
                Identifier of the owned bot, which verified the user or the chat

            verified_id (:class:`"types.MessageSender"`):
                Identifier of the user or the supergroup or channel chat, which verification is removed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "removeMessageSenderBotVerification",
                "bot_user_id": bot_user_id,
                "verified_id": verified_id,
            }
        )

    async def getActiveSessions(self) -> Union["types.Error", "types.Sessions"]:
        r"""Returns all active sessions of the current user

        Returns:
            :class:`~pytdbot.types.Sessions`
        """

        return await self.invoke(
            {
                "@type": "getActiveSessions",
            }
        )

    async def terminateSession(
        self, session_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Terminates a session of the current user

        Parameters:
            session_id (:class:`int`):
                Session identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "terminateSession", "session_id": session_id}
        )

    async def terminateAllOtherSessions(self) -> Union["types.Error", "types.Ok"]:
        r"""Terminates all other sessions of the current user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "terminateAllOtherSessions",
            }
        )

    async def confirmSession(
        self, session_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Confirms an unconfirmed session of the current user from another device

        Parameters:
            session_id (:class:`int`):
                Session identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "confirmSession", "session_id": session_id})

    async def toggleSessionCanAcceptCalls(
        self, session_id: int = 0, can_accept_calls: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a session can accept incoming calls

        Parameters:
            session_id (:class:`int`):
                Session identifier

            can_accept_calls (:class:`bool`):
                Pass true to allow accepting incoming calls by the session; pass false otherwise

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSessionCanAcceptCalls",
                "session_id": session_id,
                "can_accept_calls": can_accept_calls,
            }
        )

    async def toggleSessionCanAcceptSecretChats(
        self, session_id: int = 0, can_accept_secret_chats: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a session can accept incoming secret chats

        Parameters:
            session_id (:class:`int`):
                Session identifier

            can_accept_secret_chats (:class:`bool`):
                Pass true to allow accepting secret chats by the session; pass false otherwise

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSessionCanAcceptSecretChats",
                "session_id": session_id,
                "can_accept_secret_chats": can_accept_secret_chats,
            }
        )

    async def setInactiveSessionTtl(
        self, inactive_session_ttl_days: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the period of inactivity after which sessions will automatically be terminated

        Parameters:
            inactive_session_ttl_days (:class:`int`):
                New number of days of inactivity before sessions will be automatically terminated; 1\-366 days

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setInactiveSessionTtl",
                "inactive_session_ttl_days": inactive_session_ttl_days,
            }
        )

    async def getConnectedWebsites(
        self,
    ) -> Union["types.Error", "types.ConnectedWebsites"]:
        r"""Returns all website where the current user used Telegram to log in

        Returns:
            :class:`~pytdbot.types.ConnectedWebsites`
        """

        return await self.invoke(
            {
                "@type": "getConnectedWebsites",
            }
        )

    async def disconnectWebsite(
        self, website_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Disconnects website from the current user's Telegram account

        Parameters:
            website_id (:class:`int`):
                Website identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "disconnectWebsite", "website_id": website_id}
        )

    async def disconnectAllWebsites(self) -> Union["types.Error", "types.Ok"]:
        r"""Disconnects all websites from the current user's Telegram account

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "disconnectAllWebsites",
            }
        )

    async def setSupergroupUsername(
        self, supergroup_id: int = 0, username: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup or channel

            username (:class:`str`):
                New value of the username\. Use an empty string to remove the username\. The username can't be completely removed if there is another active or disabled username

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setSupergroupUsername",
                "supergroup_id": supergroup_id,
                "username": username,
            }
        )

    async def toggleSupergroupUsernameIsActive(
        self, supergroup_id: int = 0, username: str = "", is_active: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel\. The editable username can't be disabled\. May return an error with a message \"USERNAMES\_ACTIVE\_TOO\_MUCH\" if the maximum number of active usernames has been reached

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup or channel

            username (:class:`str`):
                The username to change

            is_active (:class:`bool`):
                Pass true to activate the username; pass false to disable it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupUsernameIsActive",
                "supergroup_id": supergroup_id,
                "username": username,
                "is_active": is_active,
            }
        )

    async def disableAllSupergroupUsernames(
        self, supergroup_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Disables all active non\-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup or channel

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "disableAllSupergroupUsernames", "supergroup_id": supergroup_id}
        )

    async def reorderSupergroupActiveUsernames(
        self, supergroup_id: int = 0, usernames: List[str] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup or channel

            usernames (:class:`List[str]`):
                The new order of active usernames\. All currently active usernames must be specified

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reorderSupergroupActiveUsernames",
                "supergroup_id": supergroup_id,
                "usernames": usernames,
            }
        )

    async def setSupergroupStickerSet(
        self, supergroup_id: int = 0, sticker_set_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the sticker set of a supergroup; requires can\_change\_info administrator right

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

            sticker_set_id (:class:`int`):
                New value of the supergroup sticker set identifier\. Use 0 to remove the supergroup sticker set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setSupergroupStickerSet",
                "supergroup_id": supergroup_id,
                "sticker_set_id": sticker_set_id,
            }
        )

    async def setSupergroupCustomEmojiStickerSet(
        self, supergroup_id: int = 0, custom_emoji_sticker_set_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the custom emoji sticker set of a supergroup; requires can\_change\_info administrator right\. The chat must have at least chatBoostFeatures\.min\_custom\_emoji\_sticker\_set\_boost\_level boost level to pass the corresponding color

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

            custom_emoji_sticker_set_id (:class:`int`):
                New value of the custom emoji sticker set identifier for the supergroup\. Use 0 to remove the custom emoji sticker set in the supergroup

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setSupergroupCustomEmojiStickerSet",
                "supergroup_id": supergroup_id,
                "custom_emoji_sticker_set_id": custom_emoji_sticker_set_id,
            }
        )

    async def setSupergroupUnrestrictBoostCount(
        self, supergroup_id: int = 0, unrestrict_boost_count: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the number of times the supergroup must be boosted by a user to ignore slow mode and chat permission restrictions; requires can\_restrict\_members administrator right

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

            unrestrict_boost_count (:class:`int`):
                New value of the unrestrict\_boost\_count supergroup setting; 0\-8\. Use 0 to remove the setting

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setSupergroupUnrestrictBoostCount",
                "supergroup_id": supergroup_id,
                "unrestrict_boost_count": unrestrict_boost_count,
            }
        )

    async def toggleSupergroupSignMessages(
        self,
        supergroup_id: int = 0,
        sign_messages: bool = False,
        show_message_sender: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether sender signature or link to the account is added to sent messages in a channel; requires can\_change\_info member right

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the channel

            sign_messages (:class:`bool`):
                New value of sign\_messages

            show_message_sender (:class:`bool`):
                New value of show\_message\_sender

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupSignMessages",
                "supergroup_id": supergroup_id,
                "sign_messages": sign_messages,
                "show_message_sender": show_message_sender,
            }
        )

    async def toggleSupergroupJoinToSendMessages(
        self, supergroup_id: int = 0, join_to_send_messages: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can\_restrict\_members administrator right

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup that isn't a broadcast group

            join_to_send_messages (:class:`bool`):
                New value of join\_to\_send\_messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupJoinToSendMessages",
                "supergroup_id": supergroup_id,
                "join_to_send_messages": join_to_send_messages,
            }
        )

    async def toggleSupergroupJoinByRequest(
        self, supergroup_id: int = 0, join_by_request: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can\_restrict\_members administrator right

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup that isn't a broadcast group

            join_by_request (:class:`bool`):
                New value of join\_by\_request

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupJoinByRequest",
                "supergroup_id": supergroup_id,
                "join_by_request": join_by_request,
            }
        )

    async def toggleSupergroupIsAllHistoryAvailable(
        self, supergroup_id: int = 0, is_all_history_available: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether the message history of a supergroup is available to new members; requires can\_change\_info member right

        Parameters:
            supergroup_id (:class:`int`):
                The identifier of the supergroup

            is_all_history_available (:class:`bool`):
                The new value of is\_all\_history\_available

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupIsAllHistoryAvailable",
                "supergroup_id": supergroup_id,
                "is_all_history_available": is_all_history_available,
            }
        )

    async def toggleSupergroupCanHaveSponsoredMessages(
        self, supergroup_id: int = 0, can_have_sponsored_messages: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether sponsored messages are shown in the channel chat; requires owner privileges in the channel\. The chat must have at least chatBoostFeatures\.min\_sponsored\_message\_disable\_boost\_level boost level to disable sponsored messages

        Parameters:
            supergroup_id (:class:`int`):
                The identifier of the channel

            can_have_sponsored_messages (:class:`bool`):
                The new value of can\_have\_sponsored\_messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupCanHaveSponsoredMessages",
                "supergroup_id": supergroup_id,
                "can_have_sponsored_messages": can_have_sponsored_messages,
            }
        )

    async def toggleSupergroupHasHiddenMembers(
        self, supergroup_id: int = 0, has_hidden_members: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether non\-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers\. Can be called only if supergroupFullInfo\.can\_hide\_members \=\= true

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

            has_hidden_members (:class:`bool`):
                New value of has\_hidden\_members

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupHasHiddenMembers",
                "supergroup_id": supergroup_id,
                "has_hidden_members": has_hidden_members,
            }
        )

    async def toggleSupergroupHasAggressiveAntiSpamEnabled(
        self, supergroup_id: int = 0, has_aggressive_anti_spam_enabled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether aggressive anti\-spam checks are enabled in the supergroup\. Can be called only if supergroupFullInfo\.can\_toggle\_aggressive\_anti\_spam \=\= true

        Parameters:
            supergroup_id (:class:`int`):
                The identifier of the supergroup, which isn't a broadcast group

            has_aggressive_anti_spam_enabled (:class:`bool`):
                The new value of has\_aggressive\_anti\_spam\_enabled

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupHasAggressiveAntiSpamEnabled",
                "supergroup_id": supergroup_id,
                "has_aggressive_anti_spam_enabled": has_aggressive_anti_spam_enabled,
            }
        )

    async def toggleSupergroupIsForum(
        self, supergroup_id: int = 0, is_forum: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether the supergroup is a forum; requires owner privileges in the supergroup\. Discussion supergroups can't be converted to forums

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

            is_forum (:class:`bool`):
                New value of is\_forum

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupIsForum",
                "supergroup_id": supergroup_id,
                "is_forum": is_forum,
            }
        )

    async def toggleSupergroupIsBroadcastGroup(
        self, supergroup_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleSupergroupIsBroadcastGroup",
                "supergroup_id": supergroup_id,
            }
        )

    async def reportSupergroupSpam(
        self, supergroup_id: int = 0, message_ids: List[int] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports messages in a supergroup as spam; requires administrator rights in the supergroup

        Parameters:
            supergroup_id (:class:`int`):
                Supergroup identifier

            message_ids (:class:`List[int]`):
                Identifiers of messages to report\. Use messageProperties\.can\_report\_supergroup\_spam to check whether the message can be reported

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportSupergroupSpam",
                "supergroup_id": supergroup_id,
                "message_ids": message_ids,
            }
        )

    async def reportSupergroupAntiSpamFalsePositive(
        self, supergroup_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports a false deletion of a message by aggressive anti\-spam checks; requires administrator rights in the supergroup\. Can be called only for messages from chatEventMessageDeleted with can\_report\_anti\_spam\_false\_positive \=\= true

        Parameters:
            supergroup_id (:class:`int`):
                Supergroup identifier

            message_id (:class:`int`):
                Identifier of the erroneously deleted message from chatEventMessageDeleted

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportSupergroupAntiSpamFalsePositive",
                "supergroup_id": supergroup_id,
                "message_id": message_id,
            }
        )

    async def getSupergroupMembers(
        self,
        supergroup_id: int = 0,
        filter: "types.SupergroupMembersFilter" = None,
        offset: int = 0,
        limit: int = 0,
    ) -> Union["types.Error", "types.ChatMembers"]:
        r"""Returns information about members or banned users in a supergroup or channel\. Can be used only if supergroupFullInfo\.can\_get\_members \=\= true; additionally, administrator privileges may be required for some filters

        Parameters:
            supergroup_id (:class:`int`):
                Identifier of the supergroup or channel

            filter (:class:`"types.SupergroupMembersFilter"`):
                The type of users to return; pass null to use supergroupMembersFilterRecent

            offset (:class:`int`):
                Number of users to skip

            limit (:class:`int`):
                The maximum number of users to be returned; up to 200

        Returns:
            :class:`~pytdbot.types.ChatMembers`
        """

        return await self.invoke(
            {
                "@type": "getSupergroupMembers",
                "supergroup_id": supergroup_id,
                "filter": filter,
                "offset": offset,
                "limit": limit,
            }
        )

    async def closeSecretChat(
        self, secret_chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Closes a secret chat, effectively transferring its state to secretChatStateClosed

        Parameters:
            secret_chat_id (:class:`int`):
                Secret chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "closeSecretChat", "secret_chat_id": secret_chat_id}
        )

    async def getChatEventLog(
        self,
        chat_id: int = 0,
        query: str = "",
        from_event_id: int = 0,
        limit: int = 0,
        filters: "types.ChatEventLogFilters" = None,
        user_ids: List[int] = None,
    ) -> Union["types.Error", "types.ChatEvents"]:
        r"""Returns a list of service actions taken by chat members and administrators in the last 48 hours\. Available only for supergroups and channels\. Requires administrator rights\. Returns results in reverse chronological order \(i\.e\., in order of decreasing event\_id\)

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            query (:class:`str`):
                Search query by which to filter events

            from_event_id (:class:`int`):
                Identifier of an event from which to return results\. Use 0 to get results from the latest events

            limit (:class:`int`):
                The maximum number of events to return; up to 100

            filters (:class:`"types.ChatEventLogFilters"`):
                The types of events to return; pass null to get chat events of all types

            user_ids (:class:`List[int]`):
                User identifiers by which to filter events\. By default, events relating to all users will be returned

        Returns:
            :class:`~pytdbot.types.ChatEvents`
        """

        return await self.invoke(
            {
                "@type": "getChatEventLog",
                "chat_id": chat_id,
                "query": query,
                "from_event_id": from_event_id,
                "limit": limit,
                "filters": filters,
                "user_ids": user_ids,
            }
        )

    async def getTimeZones(self) -> Union["types.Error", "types.TimeZones"]:
        r"""Returns the list of supported time zones

        Returns:
            :class:`~pytdbot.types.TimeZones`
        """

        return await self.invoke(
            {
                "@type": "getTimeZones",
            }
        )

    async def getPaymentForm(
        self,
        input_invoice: "types.InputInvoice" = None,
        theme: "types.ThemeParameters" = None,
    ) -> Union["types.Error", "types.PaymentForm"]:
        r"""Returns an invoice payment form\. This method must be called when the user presses inline button of the type inlineKeyboardButtonTypeBuy, or wants to buy access to media in a messagePaidMedia message

        Parameters:
            input_invoice (:class:`"types.InputInvoice"`):
                The invoice

            theme (:class:`"types.ThemeParameters"`):
                Preferred payment form theme; pass null to use the default theme

        Returns:
            :class:`~pytdbot.types.PaymentForm`
        """

        return await self.invoke(
            {"@type": "getPaymentForm", "input_invoice": input_invoice, "theme": theme}
        )

    async def validateOrderInfo(
        self,
        input_invoice: "types.InputInvoice" = None,
        order_info: "types.OrderInfo" = None,
        allow_save: bool = False,
    ) -> Union["types.Error", "types.ValidatedOrderInfo"]:
        r"""Validates the order information provided by a user and returns the available shipping options for a flexible invoice

        Parameters:
            input_invoice (:class:`"types.InputInvoice"`):
                The invoice

            order_info (:class:`"types.OrderInfo"`):
                The order information, provided by the user; pass null if empty

            allow_save (:class:`bool`):
                Pass true to save the order information

        Returns:
            :class:`~pytdbot.types.ValidatedOrderInfo`
        """

        return await self.invoke(
            {
                "@type": "validateOrderInfo",
                "input_invoice": input_invoice,
                "order_info": order_info,
                "allow_save": allow_save,
            }
        )

    async def sendPaymentForm(
        self,
        input_invoice: "types.InputInvoice" = None,
        payment_form_id: int = 0,
        order_info_id: str = "",
        shipping_option_id: str = "",
        credentials: "types.InputCredentials" = None,
        tip_amount: int = 0,
    ) -> Union["types.Error", "types.PaymentResult"]:
        r"""Sends a filled\-out payment form to the bot for final verification

        Parameters:
            input_invoice (:class:`"types.InputInvoice"`):
                The invoice

            payment_form_id (:class:`int`):
                Payment form identifier returned by getPaymentForm

            order_info_id (:class:`str`):
                Identifier returned by validateOrderInfo, or an empty string

            shipping_option_id (:class:`str`):
                Identifier of a chosen shipping option, if applicable

            credentials (:class:`"types.InputCredentials"`):
                The credentials chosen by user for payment; pass null for a payment in Telegram Stars

            tip_amount (:class:`int`):
                Chosen by the user amount of tip in the smallest units of the currency

        Returns:
            :class:`~pytdbot.types.PaymentResult`
        """

        return await self.invoke(
            {
                "@type": "sendPaymentForm",
                "input_invoice": input_invoice,
                "payment_form_id": payment_form_id,
                "order_info_id": order_info_id,
                "shipping_option_id": shipping_option_id,
                "credentials": credentials,
                "tip_amount": tip_amount,
            }
        )

    async def getPaymentReceipt(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.PaymentReceipt"]:
        r"""Returns information about a successful payment

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the messagePaymentSuccessful message

            message_id (:class:`int`):
                Message identifier

        Returns:
            :class:`~pytdbot.types.PaymentReceipt`
        """

        return await self.invoke(
            {"@type": "getPaymentReceipt", "chat_id": chat_id, "message_id": message_id}
        )

    async def getSavedOrderInfo(self) -> Union["types.Error", "types.OrderInfo"]:
        r"""Returns saved order information\. Returns a 404 error if there is no saved order information

        Returns:
            :class:`~pytdbot.types.OrderInfo`
        """

        return await self.invoke(
            {
                "@type": "getSavedOrderInfo",
            }
        )

    async def deleteSavedOrderInfo(self) -> Union["types.Error", "types.Ok"]:
        r"""Deletes saved order information

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteSavedOrderInfo",
            }
        )

    async def deleteSavedCredentials(self) -> Union["types.Error", "types.Ok"]:
        r"""Deletes saved credentials for all payment provider bots

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "deleteSavedCredentials",
            }
        )

    async def setGiftSettings(
        self, settings: "types.GiftSettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes settings for gift receiving for the current user

        Parameters:
            settings (:class:`"types.GiftSettings"`):
                The new settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setGiftSettings", "settings": settings})

    async def getAvailableGifts(self) -> Union["types.Error", "types.Gifts"]:
        r"""Returns gifts that can be sent to other users and channel chats

        Returns:
            :class:`~pytdbot.types.Gifts`
        """

        return await self.invoke(
            {
                "@type": "getAvailableGifts",
            }
        )

    async def sendGift(
        self,
        gift_id: int = 0,
        owner_id: "types.MessageSender" = None,
        text: "types.FormattedText" = None,
        is_private: bool = False,
        pay_for_upgrade: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends a gift to another user or channel chat\. May return an error with a message \"STARGIFT\_USAGE\_LIMITED\" if the gift was sold out

        Parameters:
            gift_id (:class:`int`):
                Identifier of the gift to send

            owner_id (:class:`"types.MessageSender"`):
                Identifier of the user or the channel chat that will receive the gift

            text (:class:`"types.FormattedText"`):
                Text to show along with the gift; 0\-getOption\(\"gift\_text\_length\_max\"\) characters\. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed\. Must be empty if the receiver enabled paid messages

            is_private (:class:`bool`):
                Pass true to show gift text and sender only to the gift receiver; otherwise, everyone will be able to see them

            pay_for_upgrade (:class:`bool`):
                Pass true to additionally pay for the gift upgrade and allow the receiver to upgrade it for free

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendGift",
                "gift_id": gift_id,
                "owner_id": owner_id,
                "text": text,
                "is_private": is_private,
                "pay_for_upgrade": pay_for_upgrade,
            }
        )

    async def sellGift(
        self, business_connection_id: str = "", received_gift_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sells a gift for Telegram Stars

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request; for bots only

            received_gift_id (:class:`str`):
                Identifier of the gift

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sellGift",
                "business_connection_id": business_connection_id,
                "received_gift_id": received_gift_id,
            }
        )

    async def toggleGiftIsSaved(
        self, received_gift_id: str = "", is_saved: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether a gift is shown on the current user's or the channel's profile page; requires can\_post\_messages administrator right in the channel chat

        Parameters:
            received_gift_id (:class:`str`):
                Identifier of the gift

            is_saved (:class:`bool`):
                Pass true to display the gift on the user's or the channel's profile page; pass false to remove it from the profile page

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleGiftIsSaved",
                "received_gift_id": received_gift_id,
                "is_saved": is_saved,
            }
        )

    async def setPinnedGifts(
        self,
        owner_id: "types.MessageSender" = None,
        received_gift_ids: List[str] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the list of pinned gifts on the current user's or the channel's profile page; requires can\_post\_messages administrator right in the channel chat

        Parameters:
            owner_id (:class:`"types.MessageSender"`):
                Identifier of the user or the channel chat that received the gifts

            received_gift_ids (:class:`List[str]`):
                New list of pinned gifts\. All gifts must be upgraded and saved on the profile page first\. There can be up to getOption\(\"pinned\_gift\_count\_max\"\) pinned gifts

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setPinnedGifts",
                "owner_id": owner_id,
                "received_gift_ids": received_gift_ids,
            }
        )

    async def toggleChatGiftNotifications(
        self, chat_id: int = 0, are_enabled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Toggles whether notifications for new gifts received by a channel chat are sent to the current user; requires can\_post\_messages administrator right in the chat

        Parameters:
            chat_id (:class:`int`):
                Identifier of the channel chat

            are_enabled (:class:`bool`):
                Pass true to enable notifications about new gifts owned by the channel chat; pass false to disable the notifications

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "toggleChatGiftNotifications",
                "chat_id": chat_id,
                "are_enabled": are_enabled,
            }
        )

    async def getGiftUpgradePreview(
        self, gift_id: int = 0
    ) -> Union["types.Error", "types.GiftUpgradePreview"]:
        r"""Returns examples of possible upgraded gifts for a regular gift

        Parameters:
            gift_id (:class:`int`):
                Identifier of the gift

        Returns:
            :class:`~pytdbot.types.GiftUpgradePreview`
        """

        return await self.invoke({"@type": "getGiftUpgradePreview", "gift_id": gift_id})

    async def upgradeGift(
        self,
        business_connection_id: str = "",
        received_gift_id: str = "",
        keep_original_details: bool = False,
        star_count: int = 0,
    ) -> Union["types.Error", "types.UpgradeGiftResult"]:
        r"""Upgrades a regular gift

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request; for bots only

            received_gift_id (:class:`str`):
                Identifier of the gift

            keep_original_details (:class:`bool`):
                Pass true to keep the original gift text, sender and receiver in the upgraded gift

            star_count (:class:`int`):
                The amount of Telegram Stars required to pay for the upgrade\. It the gift has prepaid\_upgrade\_star\_count \> 0, then pass 0, otherwise, pass gift\.upgrade\_star\_count

        Returns:
            :class:`~pytdbot.types.UpgradeGiftResult`
        """

        return await self.invoke(
            {
                "@type": "upgradeGift",
                "business_connection_id": business_connection_id,
                "received_gift_id": received_gift_id,
                "keep_original_details": keep_original_details,
                "star_count": star_count,
            }
        )

    async def transferGift(
        self,
        business_connection_id: str = "",
        received_gift_id: str = "",
        new_owner_id: "types.MessageSender" = None,
        star_count: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends an upgraded gift to another user or a channel chat

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request; for bots only

            received_gift_id (:class:`str`):
                Identifier of the gift

            new_owner_id (:class:`"types.MessageSender"`):
                Identifier of the user or the channel chat that will receive the gift

            star_count (:class:`int`):
                The amount of Telegram Stars required to pay for the transfer

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "transferGift",
                "business_connection_id": business_connection_id,
                "received_gift_id": received_gift_id,
                "new_owner_id": new_owner_id,
                "star_count": star_count,
            }
        )

    async def getReceivedGifts(
        self,
        business_connection_id: str = "",
        owner_id: "types.MessageSender" = None,
        exclude_unsaved: bool = False,
        exclude_saved: bool = False,
        exclude_unlimited: bool = False,
        exclude_limited: bool = False,
        exclude_upgraded: bool = False,
        sort_by_price: bool = False,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.ReceivedGifts"]:
        r"""Returns gifts received by the given user or chat

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request; for bots only

            owner_id (:class:`"types.MessageSender"`):
                Identifier of the gift receiver

            exclude_unsaved (:class:`bool`):
                Pass true to exclude gifts that aren't saved to the chat's profile page\. Always true for gifts received by other users and channel chats without can\_post\_messages administrator right

            exclude_saved (:class:`bool`):
                Pass true to exclude gifts that are saved to the chat's profile page\. Always false for gifts received by other users and channel chats without can\_post\_messages administrator right

            exclude_unlimited (:class:`bool`):
                Pass true to exclude gifts that can be purchased unlimited number of times

            exclude_limited (:class:`bool`):
                Pass true to exclude gifts that can be purchased limited number of times

            exclude_upgraded (:class:`bool`):
                Pass true to exclude upgraded gifts

            sort_by_price (:class:`bool`):
                Pass true to sort results by gift price instead of send date

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of gifts to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.ReceivedGifts`
        """

        return await self.invoke(
            {
                "@type": "getReceivedGifts",
                "business_connection_id": business_connection_id,
                "owner_id": owner_id,
                "exclude_unsaved": exclude_unsaved,
                "exclude_saved": exclude_saved,
                "exclude_unlimited": exclude_unlimited,
                "exclude_limited": exclude_limited,
                "exclude_upgraded": exclude_upgraded,
                "sort_by_price": sort_by_price,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getReceivedGift(
        self, received_gift_id: str = ""
    ) -> Union["types.Error", "types.ReceivedGift"]:
        r"""Returns information about a received gift

        Parameters:
            received_gift_id (:class:`str`):
                Identifier of the gift

        Returns:
            :class:`~pytdbot.types.ReceivedGift`
        """

        return await self.invoke(
            {"@type": "getReceivedGift", "received_gift_id": received_gift_id}
        )

    async def getUpgradedGift(
        self, name: str = ""
    ) -> Union["types.Error", "types.UpgradedGift"]:
        r"""Returns information about an upgraded gift by its name

        Parameters:
            name (:class:`str`):
                Unique name of the upgraded gift

        Returns:
            :class:`~pytdbot.types.UpgradedGift`
        """

        return await self.invoke({"@type": "getUpgradedGift", "name": name})

    async def getUpgradedGiftWithdrawalUrl(
        self, received_gift_id: str = "", password: str = ""
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns a URL for upgraded gift withdrawal in the TON blockchain as an NFT; requires owner privileges for gifts owned by a chat

        Parameters:
            received_gift_id (:class:`str`):
                Identifier of the gift

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getUpgradedGiftWithdrawalUrl",
                "received_gift_id": received_gift_id,
                "password": password,
            }
        )

    async def createInvoiceLink(
        self,
        business_connection_id: str = "",
        invoice: "types.InputMessageContent" = None,
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Creates a link for the given invoice; for bots only

        Parameters:
            business_connection_id (:class:`str`):
                Unique identifier of business connection on behalf of which to send the request

            invoice (:class:`"types.InputMessageContent"`):
                Information about the invoice of the type inputMessageInvoice

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "createInvoiceLink",
                "business_connection_id": business_connection_id,
                "invoice": invoice,
            }
        )

    async def refundStarPayment(
        self, user_id: int = 0, telegram_payment_charge_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Refunds a previously done payment in Telegram Stars; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user that did the payment

            telegram_payment_charge_id (:class:`str`):
                Telegram payment identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "refundStarPayment",
                "user_id": user_id,
                "telegram_payment_charge_id": telegram_payment_charge_id,
            }
        )

    async def getSupportUser(self) -> Union["types.Error", "types.User"]:
        r"""Returns a user that can be contacted to get support

        Returns:
            :class:`~pytdbot.types.User`
        """

        return await self.invoke(
            {
                "@type": "getSupportUser",
            }
        )

    async def getBackgroundUrl(
        self, name: str = "", type: "types.BackgroundType" = None
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Constructs a persistent HTTP URL for a background

        Parameters:
            name (:class:`str`):
                Background name

            type (:class:`"types.BackgroundType"`):
                Background type; backgroundTypeChatTheme isn't supported

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {"@type": "getBackgroundUrl", "name": name, "type": type}
        )

    async def searchBackground(
        self, name: str = ""
    ) -> Union["types.Error", "types.Background"]:
        r"""Searches for a background by its name

        Parameters:
            name (:class:`str`):
                The name of the background

        Returns:
            :class:`~pytdbot.types.Background`
        """

        return await self.invoke({"@type": "searchBackground", "name": name})

    async def setDefaultBackground(
        self,
        background: "types.InputBackground" = None,
        type: "types.BackgroundType" = None,
        for_dark_theme: bool = False,
    ) -> Union["types.Error", "types.Background"]:
        r"""Sets default background for chats; adds the background to the list of installed backgrounds

        Parameters:
            background (:class:`"types.InputBackground"`):
                The input background to use; pass null to create a new filled background

            type (:class:`"types.BackgroundType"`):
                Background type; pass null to use the default type of the remote background; backgroundTypeChatTheme isn't supported

            for_dark_theme (:class:`bool`):
                Pass true if the background is set for a dark theme

        Returns:
            :class:`~pytdbot.types.Background`
        """

        return await self.invoke(
            {
                "@type": "setDefaultBackground",
                "background": background,
                "type": type,
                "for_dark_theme": for_dark_theme,
            }
        )

    async def deleteDefaultBackground(
        self, for_dark_theme: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes default background for chats

        Parameters:
            for_dark_theme (:class:`bool`):
                Pass true if the background is deleted for a dark theme

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteDefaultBackground", "for_dark_theme": for_dark_theme}
        )

    async def getInstalledBackgrounds(
        self, for_dark_theme: bool = False
    ) -> Union["types.Error", "types.Backgrounds"]:
        r"""Returns backgrounds installed by the user

        Parameters:
            for_dark_theme (:class:`bool`):
                Pass true to order returned backgrounds for a dark theme

        Returns:
            :class:`~pytdbot.types.Backgrounds`
        """

        return await self.invoke(
            {"@type": "getInstalledBackgrounds", "for_dark_theme": for_dark_theme}
        )

    async def removeInstalledBackground(
        self, background_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes background from the list of installed backgrounds

        Parameters:
            background_id (:class:`int`):
                The background identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "removeInstalledBackground", "background_id": background_id}
        )

    async def resetInstalledBackgrounds(self) -> Union["types.Error", "types.Ok"]:
        r"""Resets list of installed backgrounds to its default value

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "resetInstalledBackgrounds",
            }
        )

    async def getLocalizationTargetInfo(
        self, only_local: bool = False
    ) -> Union["types.Error", "types.LocalizationTargetInfo"]:
        r"""Returns information about the current localization target\. This is an offline method if only\_local is true\. Can be called before authorization

        Parameters:
            only_local (:class:`bool`):
                Pass true to get only locally available information without sending network requests

        Returns:
            :class:`~pytdbot.types.LocalizationTargetInfo`
        """

        return await self.invoke(
            {"@type": "getLocalizationTargetInfo", "only_local": only_local}
        )

    async def getLanguagePackInfo(
        self, language_pack_id: str = ""
    ) -> Union["types.Error", "types.LanguagePackInfo"]:
        r"""Returns information about a language pack\. Returned language pack identifier may be different from a provided one\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Language pack identifier

        Returns:
            :class:`~pytdbot.types.LanguagePackInfo`
        """

        return await self.invoke(
            {"@type": "getLanguagePackInfo", "language_pack_id": language_pack_id}
        )

    async def getLanguagePackStrings(
        self, language_pack_id: str = "", keys: List[str] = None
    ) -> Union["types.Error", "types.LanguagePackStrings"]:
        r"""Returns strings from a language pack in the current localization target by their keys\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Language pack identifier of the strings to be returned

            keys (:class:`List[str]`):
                Language pack keys of the strings to be returned; leave empty to request all available strings

        Returns:
            :class:`~pytdbot.types.LanguagePackStrings`
        """

        return await self.invoke(
            {
                "@type": "getLanguagePackStrings",
                "language_pack_id": language_pack_id,
                "keys": keys,
            }
        )

    async def synchronizeLanguagePack(
        self, language_pack_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Fetches the latest versions of all strings from a language pack in the current localization target from the server\. This method doesn't need to be called explicitly for the current used/base language packs\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Language pack identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "synchronizeLanguagePack", "language_pack_id": language_pack_id}
        )

    async def addCustomServerLanguagePack(
        self, language_pack_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a custom server language pack to the list of installed language packs in current localization target\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Identifier of a language pack to be added

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addCustomServerLanguagePack",
                "language_pack_id": language_pack_id,
            }
        )

    async def setCustomLanguagePack(
        self,
        info: "types.LanguagePackInfo" = None,
        strings: List["types.LanguagePackString"] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds or changes a custom local language pack to the current localization target

        Parameters:
            info (:class:`"types.LanguagePackInfo"`):
                Information about the language pack\. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters\. Can be called before authorization

            strings (:class:`List["types.LanguagePackString"]`):
                Strings of the new language pack

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setCustomLanguagePack", "info": info, "strings": strings}
        )

    async def editCustomLanguagePackInfo(
        self, info: "types.LanguagePackInfo" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Edits information about a custom local language pack in the current localization target\. Can be called before authorization

        Parameters:
            info (:class:`"types.LanguagePackInfo"`):
                New information about the custom local language pack

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "editCustomLanguagePackInfo", "info": info})

    async def setCustomLanguagePackString(
        self, language_pack_id: str = "", new_string: "types.LanguagePackString" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds, edits or deletes a string in a custom local language pack\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Identifier of a previously added custom local language pack in the current localization target

            new_string (:class:`"types.LanguagePackString"`):
                New language pack string

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setCustomLanguagePackString",
                "language_pack_id": language_pack_id,
                "new_string": new_string,
            }
        )

    async def deleteLanguagePack(
        self, language_pack_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes all information about a language pack in the current localization target\. The language pack which is currently in use \(including base language pack\) or is being synchronized can't be deleted\. Can be called before authorization

        Parameters:
            language_pack_id (:class:`str`):
                Identifier of the language pack to delete

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteLanguagePack", "language_pack_id": language_pack_id}
        )

    async def registerDevice(
        self, device_token: "types.DeviceToken" = None, other_user_ids: List[int] = None
    ) -> Union["types.Error", "types.PushReceiverId"]:
        r"""Registers the currently used device for receiving push notifications\. Returns a globally unique identifier of the push notification subscription

        Parameters:
            device_token (:class:`"types.DeviceToken"`):
                Device token

            other_user_ids (:class:`List[int]`):
                List of user identifiers of other users currently using the application

        Returns:
            :class:`~pytdbot.types.PushReceiverId`
        """

        return await self.invoke(
            {
                "@type": "registerDevice",
                "device_token": device_token,
                "other_user_ids": other_user_ids,
            }
        )

    async def processPushNotification(
        self, payload: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Handles a push notification\. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data\. Can be called before authorization

        Parameters:
            payload (:class:`str`):
                JSON\-encoded push notification payload with all fields sent by the server, and \"google\.sent\_time\" and \"google\.notification\.sound\" fields added

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "processPushNotification", "payload": payload}
        )

    async def getPushReceiverId(
        self, payload: str = ""
    ) -> Union["types.Error", "types.PushReceiverId"]:
        r"""Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification\. Can be called synchronously

        Parameters:
            payload (:class:`str`):
                JSON\-encoded push notification payload

        Returns:
            :class:`~pytdbot.types.PushReceiverId`
        """

        return await self.invoke({"@type": "getPushReceiverId", "payload": payload})

    async def getRecentlyVisitedTMeUrls(
        self, referrer: str = ""
    ) -> Union["types.Error", "types.TMeUrls"]:
        r"""Returns t\.me URLs recently visited by a newly registered user

        Parameters:
            referrer (:class:`str`):
                Google Play referrer to identify the user

        Returns:
            :class:`~pytdbot.types.TMeUrls`
        """

        return await self.invoke(
            {"@type": "getRecentlyVisitedTMeUrls", "referrer": referrer}
        )

    async def setUserPrivacySettingRules(
        self,
        setting: "types.UserPrivacySetting" = None,
        rules: "types.UserPrivacySettingRules" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes user privacy settings

        Parameters:
            setting (:class:`"types.UserPrivacySetting"`):
                The privacy setting

            rules (:class:`"types.UserPrivacySettingRules"`):
                The new privacy rules

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setUserPrivacySettingRules", "setting": setting, "rules": rules}
        )

    async def getUserPrivacySettingRules(
        self, setting: "types.UserPrivacySetting" = None
    ) -> Union["types.Error", "types.UserPrivacySettingRules"]:
        r"""Returns the current privacy settings

        Parameters:
            setting (:class:`"types.UserPrivacySetting"`):
                The privacy setting

        Returns:
            :class:`~pytdbot.types.UserPrivacySettingRules`
        """

        return await self.invoke(
            {"@type": "getUserPrivacySettingRules", "setting": setting}
        )

    async def setReadDatePrivacySettings(
        self, settings: "types.ReadDatePrivacySettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes privacy settings for message read date

        Parameters:
            settings (:class:`"types.ReadDatePrivacySettings"`):
                New settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setReadDatePrivacySettings", "settings": settings}
        )

    async def getReadDatePrivacySettings(
        self,
    ) -> Union["types.Error", "types.ReadDatePrivacySettings"]:
        r"""Returns privacy settings for message read date

        Returns:
            :class:`~pytdbot.types.ReadDatePrivacySettings`
        """

        return await self.invoke(
            {
                "@type": "getReadDatePrivacySettings",
            }
        )

    async def setNewChatPrivacySettings(
        self, settings: "types.NewChatPrivacySettings" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes privacy settings for new chat creation; can be used only if getOption\(\"can\_set\_new\_chat\_privacy\_settings\"\)

        Parameters:
            settings (:class:`"types.NewChatPrivacySettings"`):
                New settings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setNewChatPrivacySettings", "settings": settings}
        )

    async def getNewChatPrivacySettings(
        self,
    ) -> Union["types.Error", "types.NewChatPrivacySettings"]:
        r"""Returns privacy settings for new chat creation

        Returns:
            :class:`~pytdbot.types.NewChatPrivacySettings`
        """

        return await self.invoke(
            {
                "@type": "getNewChatPrivacySettings",
            }
        )

    async def getPaidMessageRevenue(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.StarCount"]:
        r"""Returns the total number of Telegram Stars received by the current user for paid messages from the given user

        Parameters:
            user_id (:class:`int`):
                Identifier of the user

        Returns:
            :class:`~pytdbot.types.StarCount`
        """

        return await self.invoke({"@type": "getPaidMessageRevenue", "user_id": user_id})

    async def allowUnpaidMessagesFromUser(
        self, user_id: int = 0, refund_payments: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Allows the specified user to send unpaid private messages to the current user by adding a rule to userPrivacySettingAllowUnpaidMessages

        Parameters:
            user_id (:class:`int`):
                Identifier of the user

            refund_payments (:class:`bool`):
                Pass true to refund the user previously paid messages

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "allowUnpaidMessagesFromUser",
                "user_id": user_id,
                "refund_payments": refund_payments,
            }
        )

    async def setChatPaidMessageStarCount(
        self, chat_id: int = 0, paid_message_star_count: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the amount of Telegram Stars that must be paid to send a message to a supergroup chat; requires can\_restrict\_members administrator right and supergroupFullInfo\.can\_enable\_paid\_messages

        Parameters:
            chat_id (:class:`int`):
                Identifier of the supergroup chat

            paid_message_star_count (:class:`int`):
                The new number of Telegram Stars that must be paid for each message that is sent to the supergroup chat unless the sender is an administrator of the chat; 0\-getOption\(\"paid\_message\_star\_count\_max\"\)\. The supergroup will receive getOption\(\"paid\_message\_earnings\_per\_mille\"\) Telegram Stars for each 1000 Telegram Stars paid for message sending

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatPaidMessageStarCount",
                "chat_id": chat_id,
                "paid_message_star_count": paid_message_star_count,
            }
        )

    async def canSendMessageToUser(
        self, user_id: int = 0, only_local: bool = False
    ) -> Union["types.Error", "types.CanSendMessageToUserResult"]:
        r"""Check whether the current user can message another user or try to create a chat with them

        Parameters:
            user_id (:class:`int`):
                Identifier of the other user

            only_local (:class:`bool`):
                Pass true to get only locally available information without sending network requests

        Returns:
            :class:`~pytdbot.types.CanSendMessageToUserResult`
        """

        return await self.invoke(
            {
                "@type": "canSendMessageToUser",
                "user_id": user_id,
                "only_local": only_local,
            }
        )

    async def getOption(
        self, name: str = ""
    ) -> Union["types.Error", "types.OptionValue"]:
        r"""Returns the value of an option by its name\. \(Check the list of available options on https://core\.telegram\.org/tdlib/options\.\) Can be called before authorization\. Can be called synchronously for options \"version\" and \"commit\_hash\"

        Parameters:
            name (:class:`str`):
                The name of the option

        Returns:
            :class:`~pytdbot.types.OptionValue`
        """

        return await self.invoke({"@type": "getOption", "name": name})

    async def setOption(
        self, name: str = "", value: "types.OptionValue" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the value of an option\. \(Check the list of available options on https://core\.telegram\.org/tdlib/options\.\) Only writable options can be set\. Can be called before authorization

        Parameters:
            name (:class:`str`):
                The name of the option

            value (:class:`"types.OptionValue"`):
                The new value of the option; pass null to reset option value to a default value

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setOption", "name": name, "value": value})

    async def setAccountTtl(
        self, ttl: "types.AccountTtl" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the period of inactivity after which the account of the current user will automatically be deleted

        Parameters:
            ttl (:class:`"types.AccountTtl"`):
                New account TTL

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setAccountTtl", "ttl": ttl})

    async def getAccountTtl(self) -> Union["types.Error", "types.AccountTtl"]:
        r"""Returns the period of inactivity after which the account of the current user will automatically be deleted

        Returns:
            :class:`~pytdbot.types.AccountTtl`
        """

        return await self.invoke(
            {
                "@type": "getAccountTtl",
            }
        )

    async def deleteAccount(
        self, reason: str = "", password: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes the account of the current user, deleting all information associated with the user from the server\. The phone number of the account can be used to create a new account\. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

        Parameters:
            reason (:class:`str`):
                The reason why the account was deleted; optional

            password (:class:`str`):
                The 2\-step verification password of the current user\. If the current user isn't authorized, then an empty string can be passed and account deletion can be canceled within one week

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "deleteAccount", "reason": reason, "password": password}
        )

    async def setDefaultMessageAutoDeleteTime(
        self, message_auto_delete_time: "types.MessageAutoDeleteTime" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the default message auto\-delete time for new chats

        Parameters:
            message_auto_delete_time (:class:`"types.MessageAutoDeleteTime"`):
                New default message auto\-delete time; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setDefaultMessageAutoDeleteTime",
                "message_auto_delete_time": message_auto_delete_time,
            }
        )

    async def getDefaultMessageAutoDeleteTime(
        self,
    ) -> Union["types.Error", "types.MessageAutoDeleteTime"]:
        r"""Returns default message auto\-delete time setting for new chats

        Returns:
            :class:`~pytdbot.types.MessageAutoDeleteTime`
        """

        return await self.invoke(
            {
                "@type": "getDefaultMessageAutoDeleteTime",
            }
        )

    async def removeChatActionBar(
        self, chat_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a chat action bar without any other action

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeChatActionBar", "chat_id": chat_id})

    async def reportChat(
        self,
        chat_id: int = 0,
        option_id: bytes = b"",
        message_ids: List[int] = None,
        text: str = "",
    ) -> Union["types.Error", "types.ReportChatResult"]:
        r"""Reports a chat to the Telegram moderators\. A chat can be reported only from the chat action bar, or if chat\.can\_be\_reported

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            option_id (:class:`bytes`):
                Option identifier chosen by the user; leave empty for the initial request

            message_ids (:class:`List[int]`):
                Identifiers of reported messages\. Use messageProperties\.can\_report\_chat to check whether the message can be reported

            text (:class:`str`):
                Additional report details if asked by the server; 0\-1024 characters; leave empty for the initial request

        Returns:
            :class:`~pytdbot.types.ReportChatResult`
        """

        return await self.invoke(
            {
                "@type": "reportChat",
                "chat_id": chat_id,
                "option_id": option_id,
                "message_ids": message_ids,
                "text": text,
            }
        )

    async def reportChatPhoto(
        self,
        chat_id: int = 0,
        file_id: int = 0,
        reason: "types.ReportReason" = None,
        text: str = "",
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports a chat photo to the Telegram moderators\. A chat photo can be reported only if chat\.can\_be\_reported

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            file_id (:class:`int`):
                Identifier of the photo to report\. Only full photos from chatPhoto can be reported

            reason (:class:`"types.ReportReason"`):
                The reason for reporting the chat photo

            text (:class:`str`):
                Additional report details; 0\-1024 characters

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportChatPhoto",
                "chat_id": chat_id,
                "file_id": file_id,
                "reason": reason,
                "text": text,
            }
        )

    async def reportMessageReactions(
        self,
        chat_id: int = 0,
        message_id: int = 0,
        sender_id: "types.MessageSender" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reports reactions set on a message to the Telegram moderators\. Reactions on a message can be reported only if messageProperties\.can\_report\_reactions

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Message identifier

            sender_id (:class:`"types.MessageSender"`):
                Identifier of the sender, which added the reaction

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "reportMessageReactions",
                "chat_id": chat_id,
                "message_id": message_id,
                "sender_id": sender_id,
            }
        )

    async def getChatRevenueStatistics(
        self, chat_id: int = 0, is_dark: bool = False
    ) -> Union["types.Error", "types.ChatRevenueStatistics"]:
        r"""Returns detailed revenue statistics about a chat\. Currently, this method can be used only for channels if supergroupFullInfo\.can\_get\_revenue\_statistics \=\= true or bots if userFullInfo\.bot\_info\.can\_get\_revenue\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            is_dark (:class:`bool`):
                Pass true if a dark theme is used by the application

        Returns:
            :class:`~pytdbot.types.ChatRevenueStatistics`
        """

        return await self.invoke(
            {
                "@type": "getChatRevenueStatistics",
                "chat_id": chat_id,
                "is_dark": is_dark,
            }
        )

    async def getChatRevenueWithdrawalUrl(
        self, chat_id: int = 0, password: str = ""
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns a URL for chat revenue withdrawal; requires owner privileges in the channel chat or the bot\. Currently, this method can be used only if getOption\(\"can\_withdraw\_chat\_revenue\"\) for channels with supergroupFullInfo\.can\_get\_revenue\_statistics \=\= true or bots with userFullInfo\.bot\_info\.can\_get\_revenue\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getChatRevenueWithdrawalUrl",
                "chat_id": chat_id,
                "password": password,
            }
        )

    async def getChatRevenueTransactions(
        self, chat_id: int = 0, offset: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.ChatRevenueTransactions"]:
        r"""Returns the list of revenue transactions for a chat\. Currently, this method can be used only for channels if supergroupFullInfo\.can\_get\_revenue\_statistics \=\= true or bots if userFullInfo\.bot\_info\.can\_get\_revenue\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            offset (:class:`int`):
                Number of transactions to skip

            limit (:class:`int`):
                The maximum number of transactions to be returned; up to 200

        Returns:
            :class:`~pytdbot.types.ChatRevenueTransactions`
        """

        return await self.invoke(
            {
                "@type": "getChatRevenueTransactions",
                "chat_id": chat_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getStarRevenueStatistics(
        self, owner_id: "types.MessageSender" = None, is_dark: bool = False
    ) -> Union["types.Error", "types.StarRevenueStatistics"]:
        r"""Returns detailed Telegram Star revenue statistics

        Parameters:
            owner_id (:class:`"types.MessageSender"`):
                Identifier of the owner of the Telegram Stars; can be identifier of the current user, an owned bot, or a supergroup or a channel chat with supergroupFullInfo\.can\_get\_star\_revenue\_statistics \=\= true

            is_dark (:class:`bool`):
                Pass true if a dark theme is used by the application

        Returns:
            :class:`~pytdbot.types.StarRevenueStatistics`
        """

        return await self.invoke(
            {
                "@type": "getStarRevenueStatistics",
                "owner_id": owner_id,
                "is_dark": is_dark,
            }
        )

    async def getStarWithdrawalUrl(
        self,
        owner_id: "types.MessageSender" = None,
        star_count: int = 0,
        password: str = "",
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns a URL for Telegram Star withdrawal

        Parameters:
            owner_id (:class:`"types.MessageSender"`):
                Identifier of the owner of the Telegram Stars; can be identifier of the current user, an owned bot, or an owned supergroup or channel chat

            star_count (:class:`int`):
                The number of Telegram Stars to withdraw\. Must be at least getOption\(\"star\_withdrawal\_count\_min\"\)

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getStarWithdrawalUrl",
                "owner_id": owner_id,
                "star_count": star_count,
                "password": password,
            }
        )

    async def getStarAdAccountUrl(
        self, owner_id: "types.MessageSender" = None
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns a URL for a Telegram Ad platform account that can be used to set up advertisements for the chat paid in the owned Telegram Stars

        Parameters:
            owner_id (:class:`"types.MessageSender"`):
                Identifier of the owner of the Telegram Stars; can be identifier of an owned bot, or identifier of an owned channel chat

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke({"@type": "getStarAdAccountUrl", "owner_id": owner_id})

    async def getChatStatistics(
        self, chat_id: int = 0, is_dark: bool = False
    ) -> Union["types.Error", "types.ChatStatistics"]:
        r"""Returns detailed statistics about a chat\. Currently, this method can be used only for supergroups and channels\. Can be used only if supergroupFullInfo\.can\_get\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            is_dark (:class:`bool`):
                Pass true if a dark theme is used by the application

        Returns:
            :class:`~pytdbot.types.ChatStatistics`
        """

        return await self.invoke(
            {"@type": "getChatStatistics", "chat_id": chat_id, "is_dark": is_dark}
        )

    async def getMessageStatistics(
        self, chat_id: int = 0, message_id: int = 0, is_dark: bool = False
    ) -> Union["types.Error", "types.MessageStatistics"]:
        r"""Returns detailed statistics about a message\. Can be used only if messageProperties\.can\_get\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            message_id (:class:`int`):
                Message identifier

            is_dark (:class:`bool`):
                Pass true if a dark theme is used by the application

        Returns:
            :class:`~pytdbot.types.MessageStatistics`
        """

        return await self.invoke(
            {
                "@type": "getMessageStatistics",
                "chat_id": chat_id,
                "message_id": message_id,
                "is_dark": is_dark,
            }
        )

    async def getMessagePublicForwards(
        self, chat_id: int = 0, message_id: int = 0, offset: str = "", limit: int = 0
    ) -> Union["types.Error", "types.PublicForwards"]:
        r"""Returns forwarded copies of a channel message to different public channels and public reposts as a story\. Can be used only if messageProperties\.can\_get\_statistics \=\= true\. For optimal performance, the number of returned messages and stories is chosen by TDLib

        Parameters:
            chat_id (:class:`int`):
                Chat identifier of the message

            message_id (:class:`int`):
                Message identifier

            offset (:class:`str`):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of messages and stories to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.PublicForwards`
        """

        return await self.invoke(
            {
                "@type": "getMessagePublicForwards",
                "chat_id": chat_id,
                "message_id": message_id,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getStoryStatistics(
        self, chat_id: int = 0, story_id: int = 0, is_dark: bool = False
    ) -> Union["types.Error", "types.StoryStatistics"]:
        r"""Returns detailed statistics about a story\. Can be used only if story\.can\_get\_statistics \=\= true

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            story_id (:class:`int`):
                Story identifier

            is_dark (:class:`bool`):
                Pass true if a dark theme is used by the application

        Returns:
            :class:`~pytdbot.types.StoryStatistics`
        """

        return await self.invoke(
            {
                "@type": "getStoryStatistics",
                "chat_id": chat_id,
                "story_id": story_id,
                "is_dark": is_dark,
            }
        )

    async def getStatisticalGraph(
        self, chat_id: int = 0, token: str = "", x: int = 0
    ) -> Union["types.Error", "types.StatisticalGraph"]:
        r"""Loads an asynchronous or a zoomed in statistical graph

        Parameters:
            chat_id (:class:`int`):
                Chat identifier

            token (:class:`str`):
                The token for graph loading

            x (:class:`int`):
                X\-value for zoomed in graph or 0 otherwise

        Returns:
            :class:`~pytdbot.types.StatisticalGraph`
        """

        return await self.invoke(
            {"@type": "getStatisticalGraph", "chat_id": chat_id, "token": token, "x": x}
        )

    async def getStorageStatistics(
        self, chat_limit: int = 0
    ) -> Union["types.Error", "types.StorageStatistics"]:
        r"""Returns storage usage statistics\. Can be called before authorization

        Parameters:
            chat_limit (:class:`int`):
                The maximum number of chats with the largest storage usage for which separate statistics need to be returned\. All other chats will be grouped in entries with chat\_id \=\= 0\. If the chat info database is not used, the chat\_limit is ignored and is always set to 0

        Returns:
            :class:`~pytdbot.types.StorageStatistics`
        """

        return await self.invoke(
            {"@type": "getStorageStatistics", "chat_limit": chat_limit}
        )

    async def getStorageStatisticsFast(
        self,
    ) -> Union["types.Error", "types.StorageStatisticsFast"]:
        r"""Quickly returns approximate storage usage statistics\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.StorageStatisticsFast`
        """

        return await self.invoke(
            {
                "@type": "getStorageStatisticsFast",
            }
        )

    async def getDatabaseStatistics(
        self,
    ) -> Union["types.Error", "types.DatabaseStatistics"]:
        r"""Returns database statistics

        Returns:
            :class:`~pytdbot.types.DatabaseStatistics`
        """

        return await self.invoke(
            {
                "@type": "getDatabaseStatistics",
            }
        )

    async def optimizeStorage(
        self,
        size: int = 0,
        ttl: int = 0,
        count: int = 0,
        immunity_delay: int = 0,
        file_types: List["types.FileType"] = None,
        chat_ids: List[int] = None,
        exclude_chat_ids: List[int] = None,
        return_deleted_file_statistics: bool = False,
        chat_limit: int = 0,
    ) -> Union["types.Error", "types.StorageStatistics"]:
        r"""Optimizes storage usage, i\.e\. deletes some files and returns new storage usage statistics\. Secret thumbnails can't be deleted

        Parameters:
            size (:class:`int`):
                Limit on the total size of files after deletion, in bytes\. Pass \-1 to use the default limit

            ttl (:class:`int`):
                Limit on the time that has passed since the last time a file was accessed \(or creation time for some filesystems\)\. Pass \-1 to use the default limit

            count (:class:`int`):
                Limit on the total number of files after deletion\. Pass \-1 to use the default limit

            immunity_delay (:class:`int`):
                The amount of time after the creation of a file during which it can't be deleted, in seconds\. Pass \-1 to use the default value

            file_types (:class:`List["types.FileType"]`):
                If non\-empty, only files with the given types are considered\. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted

            chat_ids (:class:`List[int]`):
                If non\-empty, only files from the given chats are considered\. Use 0 as chat identifier to delete files not belonging to any chat \(e\.g\., profile photos\)

            exclude_chat_ids (:class:`List[int]`):
                If non\-empty, files from the given chats are excluded\. Use 0 as chat identifier to exclude all files not belonging to any chat \(e\.g\., profile photos\)

            return_deleted_file_statistics (:class:`bool`):
                Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics\. Affects only returned statistics

            chat_limit (:class:`int`):
                Same as in getStorageStatistics\. Affects only returned statistics

        Returns:
            :class:`~pytdbot.types.StorageStatistics`
        """

        return await self.invoke(
            {
                "@type": "optimizeStorage",
                "size": size,
                "ttl": ttl,
                "count": count,
                "immunity_delay": immunity_delay,
                "file_types": file_types,
                "chat_ids": chat_ids,
                "exclude_chat_ids": exclude_chat_ids,
                "return_deleted_file_statistics": return_deleted_file_statistics,
                "chat_limit": chat_limit,
            }
        )

    async def setNetworkType(
        self, type: "types.NetworkType" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the current network type\. Can be called before authorization\. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same\. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics

        Parameters:
            type (:class:`"types.NetworkType"`):
                The new network type; pass null to set network type to networkTypeOther

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setNetworkType", "type": type})

    async def getNetworkStatistics(
        self, only_current: bool = False
    ) -> Union["types.Error", "types.NetworkStatistics"]:
        r"""Returns network data usage statistics\. Can be called before authorization

        Parameters:
            only_current (:class:`bool`):
                Pass true to get statistics only for the current library launch

        Returns:
            :class:`~pytdbot.types.NetworkStatistics`
        """

        return await self.invoke(
            {"@type": "getNetworkStatistics", "only_current": only_current}
        )

    async def addNetworkStatistics(
        self, entry: "types.NetworkStatisticsEntry" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds the specified data to data usage statistics\. Can be called before authorization

        Parameters:
            entry (:class:`"types.NetworkStatisticsEntry"`):
                The network statistics entry with the data to be added to statistics

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "addNetworkStatistics", "entry": entry})

    async def resetNetworkStatistics(self) -> Union["types.Error", "types.Ok"]:
        r"""Resets all network data usage statistics to zero\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "resetNetworkStatistics",
            }
        )

    async def getAutoDownloadSettingsPresets(
        self,
    ) -> Union["types.Error", "types.AutoDownloadSettingsPresets"]:
        r"""Returns auto\-download settings presets for the current user

        Returns:
            :class:`~pytdbot.types.AutoDownloadSettingsPresets`
        """

        return await self.invoke(
            {
                "@type": "getAutoDownloadSettingsPresets",
            }
        )

    async def setAutoDownloadSettings(
        self,
        settings: "types.AutoDownloadSettings" = None,
        type: "types.NetworkType" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets auto\-download settings

        Parameters:
            settings (:class:`"types.AutoDownloadSettings"`):
                New user auto\-download settings

            type (:class:`"types.NetworkType"`):
                Type of the network for which the new settings are relevant

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setAutoDownloadSettings", "settings": settings, "type": type}
        )

    async def getAutosaveSettings(
        self,
    ) -> Union["types.Error", "types.AutosaveSettings"]:
        r"""Returns autosave settings for the current user

        Returns:
            :class:`~pytdbot.types.AutosaveSettings`
        """

        return await self.invoke(
            {
                "@type": "getAutosaveSettings",
            }
        )

    async def setAutosaveSettings(
        self,
        scope: "types.AutosaveSettingsScope" = None,
        settings: "types.ScopeAutosaveSettings" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets autosave settings for the given scope\. The method is guaranteed to work only after at least one call to getAutosaveSettings

        Parameters:
            scope (:class:`"types.AutosaveSettingsScope"`):
                Autosave settings scope

            settings (:class:`"types.ScopeAutosaveSettings"`):
                New autosave settings for the scope; pass null to set autosave settings to default

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setAutosaveSettings", "scope": scope, "settings": settings}
        )

    async def clearAutosaveSettingsExceptions(self) -> Union["types.Error", "types.Ok"]:
        r"""Clears the list of all autosave settings exceptions\. The method is guaranteed to work only after at least one call to getAutosaveSettings

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clearAutosaveSettingsExceptions",
            }
        )

    async def getBankCardInfo(
        self, bank_card_number: str = ""
    ) -> Union["types.Error", "types.BankCardInfo"]:
        r"""Returns information about a bank card

        Parameters:
            bank_card_number (:class:`str`):
                The bank card number

        Returns:
            :class:`~pytdbot.types.BankCardInfo`
        """

        return await self.invoke(
            {"@type": "getBankCardInfo", "bank_card_number": bank_card_number}
        )

    async def getPassportElement(
        self, type: "types.PassportElementType" = None, password: str = ""
    ) -> Union["types.Error", "types.PassportElement"]:
        r"""Returns one of the available Telegram Passport elements

        Parameters:
            type (:class:`"types.PassportElementType"`):
                Telegram Passport element type

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.PassportElement`
        """

        return await self.invoke(
            {"@type": "getPassportElement", "type": type, "password": password}
        )

    async def getAllPassportElements(
        self, password: str = ""
    ) -> Union["types.Error", "types.PassportElements"]:
        r"""Returns all available Telegram Passport elements

        Parameters:
            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.PassportElements`
        """

        return await self.invoke(
            {"@type": "getAllPassportElements", "password": password}
        )

    async def setPassportElement(
        self, element: "types.InputPassportElement" = None, password: str = ""
    ) -> Union["types.Error", "types.PassportElement"]:
        r"""Adds an element to the user's Telegram Passport\. May return an error with a message \"PHONE\_VERIFICATION\_NEEDED\" or \"EMAIL\_VERIFICATION\_NEEDED\" if the chosen phone number or the chosen email address must be verified first

        Parameters:
            element (:class:`"types.InputPassportElement"`):
                Input Telegram Passport element

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.PassportElement`
        """

        return await self.invoke(
            {"@type": "setPassportElement", "element": element, "password": password}
        )

    async def deletePassportElement(
        self, type: "types.PassportElementType" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Deletes a Telegram Passport element

        Parameters:
            type (:class:`"types.PassportElementType"`):
                Element type

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deletePassportElement", "type": type})

    async def setPassportElementErrors(
        self, user_id: int = 0, errors: List["types.InputPassportElementError"] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs the user that some of the elements in their Telegram Passport contain errors; for bots only\. The user will not be able to resend the elements, until the errors are fixed

        Parameters:
            user_id (:class:`int`):
                User identifier

            errors (:class:`List["types.InputPassportElementError"]`):
                The errors

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setPassportElementErrors", "user_id": user_id, "errors": errors}
        )

    async def getPreferredCountryLanguage(
        self, country_code: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details\. Returns a 404 error if unknown

        Parameters:
            country_code (:class:`str`):
                A two\-letter ISO 3166\-1 alpha\-2 country code

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {"@type": "getPreferredCountryLanguage", "country_code": country_code}
        )

    async def sendEmailAddressVerificationCode(
        self, email_address: str = ""
    ) -> Union["types.Error", "types.EmailAddressAuthenticationCodeInfo"]:
        r"""Sends a code to verify an email address to be added to a user's Telegram Passport

        Parameters:
            email_address (:class:`str`):
                Email address

        Returns:
            :class:`~pytdbot.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "sendEmailAddressVerificationCode",
                "email_address": email_address,
            }
        )

    async def resendEmailAddressVerificationCode(
        self,
    ) -> Union["types.Error", "types.EmailAddressAuthenticationCodeInfo"]:
        r"""Resends the code to verify an email address to be added to a user's Telegram Passport

        Returns:
            :class:`~pytdbot.types.EmailAddressAuthenticationCodeInfo`
        """

        return await self.invoke(
            {
                "@type": "resendEmailAddressVerificationCode",
            }
        )

    async def checkEmailAddressVerificationCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks the email address verification code for Telegram Passport

        Parameters:
            code (:class:`str`):
                Verification code to check

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "checkEmailAddressVerificationCode", "code": code}
        )

    async def getPassportAuthorizationForm(
        self,
        bot_user_id: int = 0,
        scope: str = "",
        public_key: str = "",
        nonce: str = "",
    ) -> Union["types.Error", "types.PassportAuthorizationForm"]:
        r"""Returns a Telegram Passport authorization form for sharing data with a service

        Parameters:
            bot_user_id (:class:`int`):
                User identifier of the service's bot

            scope (:class:`str`):
                Telegram Passport element types requested by the service

            public_key (:class:`str`):
                Service's public key

            nonce (:class:`str`):
                Unique request identifier provided by the service

        Returns:
            :class:`~pytdbot.types.PassportAuthorizationForm`
        """

        return await self.invoke(
            {
                "@type": "getPassportAuthorizationForm",
                "bot_user_id": bot_user_id,
                "scope": scope,
                "public_key": public_key,
                "nonce": nonce,
            }
        )

    async def getPassportAuthorizationFormAvailableElements(
        self, authorization_form_id: int = 0, password: str = ""
    ) -> Union["types.Error", "types.PassportElementsWithErrors"]:
        r"""Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form\. Result can be received only once for each authorization form

        Parameters:
            authorization_form_id (:class:`int`):
                Authorization form identifier

            password (:class:`str`):
                The 2\-step verification password of the current user

        Returns:
            :class:`~pytdbot.types.PassportElementsWithErrors`
        """

        return await self.invoke(
            {
                "@type": "getPassportAuthorizationFormAvailableElements",
                "authorization_form_id": authorization_form_id,
                "password": password,
            }
        )

    async def sendPassportAuthorizationForm(
        self,
        authorization_form_id: int = 0,
        types: List["types.PassportElementType"] = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends a Telegram Passport authorization form, effectively sharing data with the service\. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused

        Parameters:
            authorization_form_id (:class:`int`):
                Authorization form identifier

            types (:class:`List["types.PassportElementType"]`):
                Types of Telegram Passport elements chosen by user to complete the authorization form

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "sendPassportAuthorizationForm",
                "authorization_form_id": authorization_form_id,
                "types": types,
            }
        )

    async def setBotUpdatesStatus(
        self, pending_update_count: int = 0, error_message: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only

        Parameters:
            pending_update_count (:class:`int`):
                The number of pending updates

            error_message (:class:`str`):
                The last error message

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setBotUpdatesStatus",
                "pending_update_count": pending_update_count,
                "error_message": error_message,
            }
        )

    async def uploadStickerFile(
        self,
        user_id: int = 0,
        sticker_format: "types.StickerFormat" = None,
        sticker: "types.InputFile" = None,
    ) -> Union["types.Error", "types.File"]:
        r"""Uploads a file with a sticker; returns the uploaded file

        Parameters:
            user_id (:class:`int`):
                Sticker file owner; ignored for regular users

            sticker_format (:class:`"types.StickerFormat"`):
                Sticker format

            sticker (:class:`"types.InputFile"`):
                File file to upload; must fit in a 512x512 square\. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server\-side\. See https://core\.telegram\.org/animated\_stickers\#technical\-requirements for technical requirements

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "uploadStickerFile",
                "user_id": user_id,
                "sticker_format": sticker_format,
                "sticker": sticker,
            }
        )

    async def getSuggestedStickerSetName(
        self, title: str = ""
    ) -> Union["types.Error", "types.Text"]:
        r"""Returns a suggested name for a new sticker set with a given title

        Parameters:
            title (:class:`str`):
                Sticker set title; 1\-64 characters

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {"@type": "getSuggestedStickerSetName", "title": title}
        )

    async def checkStickerSetName(
        self, name: str = ""
    ) -> Union["types.Error", "types.CheckStickerSetNameResult"]:
        r"""Checks whether a name can be used for a new sticker set

        Parameters:
            name (:class:`str`):
                Name to be checked

        Returns:
            :class:`~pytdbot.types.CheckStickerSetNameResult`
        """

        return await self.invoke({"@type": "checkStickerSetName", "name": name})

    async def createNewStickerSet(
        self,
        user_id: int = 0,
        title: str = "",
        name: str = "",
        sticker_type: "types.StickerType" = None,
        needs_repainting: bool = False,
        stickers: List["types.InputSticker"] = None,
        source: str = "",
    ) -> Union["types.Error", "types.StickerSet"]:
        r"""Creates a new sticker set\. Returns the newly created sticker set

        Parameters:
            user_id (:class:`int`):
                Sticker set owner; ignored for regular users

            title (:class:`str`):
                Sticker set title; 1\-64 characters

            name (:class:`str`):
                Sticker set name\. Can contain only English letters, digits and underscores\. Must end with \*\"\_by\_<bot username\>\"\* \(\*<bot\_username\>\* is case insensitive\) for bots; 0\-64 characters\. If empty, then the name returned by getSuggestedStickerSetName will be used automatically

            sticker_type (:class:`"types.StickerType"`):
                Type of the stickers in the set

            needs_repainting (:class:`bool`):
                Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only

            stickers (:class:`List["types.InputSticker"]`):
                List of stickers to be added to the set; 1\-200 stickers for custom emoji sticker sets, and 1\-120 stickers otherwise\. For TGS stickers, uploadStickerFile must be used before the sticker is shown

            source (:class:`str`):
                Source of the sticker set; may be empty if unknown

        Returns:
            :class:`~pytdbot.types.StickerSet`
        """

        return await self.invoke(
            {
                "@type": "createNewStickerSet",
                "user_id": user_id,
                "title": title,
                "name": name,
                "sticker_type": sticker_type,
                "needs_repainting": needs_repainting,
                "stickers": stickers,
                "source": source,
            }
        )

    async def addStickerToSet(
        self, user_id: int = 0, name: str = "", sticker: "types.InputSticker" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a new sticker to a set

        Parameters:
            user_id (:class:`int`):
                Sticker set owner; ignored for regular users

            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user, and contain less than 200 stickers for custom emoji sticker sets and less than 120 otherwise

            sticker (:class:`"types.InputSticker"`):
                Sticker to add to the set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "addStickerToSet",
                "user_id": user_id,
                "name": name,
                "sticker": sticker,
            }
        )

    async def replaceStickerInSet(
        self,
        user_id: int = 0,
        name: str = "",
        old_sticker: "types.InputFile" = None,
        new_sticker: "types.InputSticker" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Replaces existing sticker in a set\. The function is equivalent to removeStickerFromSet, then addStickerToSet, then setStickerPositionInSet

        Parameters:
            user_id (:class:`int`):
                Sticker set owner; ignored for regular users

            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user

            old_sticker (:class:`"types.InputFile"`):
                Sticker to remove from the set

            new_sticker (:class:`"types.InputSticker"`):
                Sticker to add to the set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "replaceStickerInSet",
                "user_id": user_id,
                "name": name,
                "old_sticker": old_sticker,
                "new_sticker": new_sticker,
            }
        )

    async def setStickerSetThumbnail(
        self,
        user_id: int = 0,
        name: str = "",
        thumbnail: "types.InputFile" = None,
        format: "types.StickerFormat" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets a sticker set thumbnail

        Parameters:
            user_id (:class:`int`):
                Sticker set owner; ignored for regular users

            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user

            thumbnail (:class:`"types.InputFile"`):
                Thumbnail to set; pass null to remove the sticker set thumbnail

            format (:class:`"types.StickerFormat"`):
                Format of the thumbnail; pass null if thumbnail is removed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setStickerSetThumbnail",
                "user_id": user_id,
                "name": name,
                "thumbnail": thumbnail,
                "format": format,
            }
        )

    async def setCustomEmojiStickerSetThumbnail(
        self, name: str = "", custom_emoji_id: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets a custom emoji sticker set thumbnail

        Parameters:
            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user

            custom_emoji_id (:class:`int`):
                Identifier of the custom emoji from the sticker set, which will be set as sticker set thumbnail; pass 0 to remove the sticker set thumbnail

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setCustomEmojiStickerSetThumbnail",
                "name": name,
                "custom_emoji_id": custom_emoji_id,
            }
        )

    async def setStickerSetTitle(
        self, name: str = "", title: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets a sticker set title

        Parameters:
            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user

            title (:class:`str`):
                New sticker set title

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setStickerSetTitle", "name": name, "title": title}
        )

    async def deleteStickerSet(
        self, name: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Completely deletes a sticker set

        Parameters:
            name (:class:`str`):
                Sticker set name\. The sticker set must be owned by the current user

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "deleteStickerSet", "name": name})

    async def setStickerPositionInSet(
        self, sticker: "types.InputFile" = None, position: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the position of a sticker in the set to which it belongs\. The sticker set must be owned by the current user

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker

            position (:class:`int`):
                New position of the sticker in the set, 0\-based

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setStickerPositionInSet",
                "sticker": sticker,
                "position": position,
            }
        )

    async def removeStickerFromSet(
        self, sticker: "types.InputFile" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Removes a sticker from the set to which it belongs\. The sticker set must be owned by the current user

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker to remove from the set

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeStickerFromSet", "sticker": sticker})

    async def setStickerEmojis(
        self, sticker: "types.InputFile" = None, emojis: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the list of emojis corresponding to a sticker\. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker

            emojis (:class:`str`):
                New string with 1\-20 emoji corresponding to the sticker

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setStickerEmojis", "sticker": sticker, "emojis": emojis}
        )

    async def setStickerKeywords(
        self, sticker: "types.InputFile" = None, keywords: List[str] = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the list of keywords of a sticker\. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker

            keywords (:class:`List[str]`):
                List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "setStickerKeywords", "sticker": sticker, "keywords": keywords}
        )

    async def setStickerMaskPosition(
        self,
        sticker: "types.InputFile" = None,
        mask_position: "types.MaskPosition" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes the mask position of a mask sticker\. The sticker must belong to a mask sticker set that is owned by the current user

        Parameters:
            sticker (:class:`"types.InputFile"`):
                Sticker

            mask_position (:class:`"types.MaskPosition"`):
                Position where the mask is placed; pass null to remove mask position

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setStickerMaskPosition",
                "sticker": sticker,
                "mask_position": mask_position,
            }
        )

    async def getOwnedStickerSets(
        self, offset_sticker_set_id: int = 0, limit: int = 0
    ) -> Union["types.Error", "types.StickerSets"]:
        r"""Returns sticker sets owned by the current user

        Parameters:
            offset_sticker_set_id (:class:`int`):
                Identifier of the sticker set from which to return owned sticker sets; use 0 to get results from the beginning

            limit (:class:`int`):
                The maximum number of sticker sets to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit

        Returns:
            :class:`~pytdbot.types.StickerSets`
        """

        return await self.invoke(
            {
                "@type": "getOwnedStickerSets",
                "offset_sticker_set_id": offset_sticker_set_id,
                "limit": limit,
            }
        )

    async def getMapThumbnailFile(
        self,
        location: "types.Location" = None,
        zoom: int = 0,
        width: int = 0,
        height: int = 0,
        scale: int = 0,
        chat_id: int = 0,
    ) -> Union["types.Error", "types.File"]:
        r"""Returns information about a file with a map thumbnail in PNG format\. Only map thumbnail files with size less than 1MB can be downloaded

        Parameters:
            location (:class:`"types.Location"`):
                Location of the map center

            zoom (:class:`int`):
                Map zoom level; 13\-20

            width (:class:`int`):
                Map width in pixels before applying scale; 16\-1024

            height (:class:`int`):
                Map height in pixels before applying scale; 16\-1024

            scale (:class:`int`):
                Map scale; 1\-3

            chat_id (:class:`int`):
                Identifier of a chat in which the thumbnail will be shown\. Use 0 if unknown

        Returns:
            :class:`~pytdbot.types.File`
        """

        return await self.invoke(
            {
                "@type": "getMapThumbnailFile",
                "location": location,
                "zoom": zoom,
                "width": width,
                "height": height,
                "scale": scale,
                "chat_id": chat_id,
            }
        )

    async def getPremiumLimit(
        self, limit_type: "types.PremiumLimitType" = None
    ) -> Union["types.Error", "types.PremiumLimit"]:
        r"""Returns information about a limit, increased for Premium users\. Returns a 404 error if the limit is unknown

        Parameters:
            limit_type (:class:`"types.PremiumLimitType"`):
                Type of the limit

        Returns:
            :class:`~pytdbot.types.PremiumLimit`
        """

        return await self.invoke({"@type": "getPremiumLimit", "limit_type": limit_type})

    async def getPremiumFeatures(
        self, source: "types.PremiumSource" = None
    ) -> Union["types.Error", "types.PremiumFeatures"]:
        r"""Returns information about features, available to Premium users

        Parameters:
            source (:class:`"types.PremiumSource"`):
                Source of the request; pass null if the method is called from some non\-standard source

        Returns:
            :class:`~pytdbot.types.PremiumFeatures`
        """

        return await self.invoke({"@type": "getPremiumFeatures", "source": source})

    async def getPremiumStickerExamples(self) -> Union["types.Error", "types.Stickers"]:
        r"""Returns examples of premium stickers for demonstration purposes

        Returns:
            :class:`~pytdbot.types.Stickers`
        """

        return await self.invoke(
            {
                "@type": "getPremiumStickerExamples",
            }
        )

    async def getPremiumInfoSticker(
        self, month_count: int = 0
    ) -> Union["types.Error", "types.Sticker"]:
        r"""Returns the sticker to be used as representation of the Telegram Premium subscription

        Parameters:
            month_count (:class:`int`):
                Number of months the Telegram Premium subscription will be active

        Returns:
            :class:`~pytdbot.types.Sticker`
        """

        return await self.invoke(
            {"@type": "getPremiumInfoSticker", "month_count": month_count}
        )

    async def viewPremiumFeature(
        self, feature: "types.PremiumFeature" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

        Parameters:
            feature (:class:`"types.PremiumFeature"`):
                The viewed premium feature

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "viewPremiumFeature", "feature": feature})

    async def clickPremiumSubscriptionButton(self) -> Union["types.Error", "types.Ok"]:
        r"""Informs TDLib that the user clicked Premium subscription button on the Premium features screen

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "clickPremiumSubscriptionButton",
            }
        )

    async def getPremiumState(self) -> Union["types.Error", "types.PremiumState"]:
        r"""Returns state of Telegram Premium subscription and promotion videos for Premium features

        Returns:
            :class:`~pytdbot.types.PremiumState`
        """

        return await self.invoke(
            {
                "@type": "getPremiumState",
            }
        )

    async def getPremiumGiftPaymentOptions(
        self,
    ) -> Union["types.Error", "types.PremiumGiftPaymentOptions"]:
        r"""Returns available options for gifting Telegram Premium to a user

        Returns:
            :class:`~pytdbot.types.PremiumGiftPaymentOptions`
        """

        return await self.invoke(
            {
                "@type": "getPremiumGiftPaymentOptions",
            }
        )

    async def getPremiumGiveawayPaymentOptions(
        self, boosted_chat_id: int = 0
    ) -> Union["types.Error", "types.PremiumGiveawayPaymentOptions"]:
        r"""Returns available options for creating of Telegram Premium giveaway or manual distribution of Telegram Premium among chat members

        Parameters:
            boosted_chat_id (:class:`int`):
                Identifier of the supergroup or channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user

        Returns:
            :class:`~pytdbot.types.PremiumGiveawayPaymentOptions`
        """

        return await self.invoke(
            {
                "@type": "getPremiumGiveawayPaymentOptions",
                "boosted_chat_id": boosted_chat_id,
            }
        )

    async def checkPremiumGiftCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.PremiumGiftCodeInfo"]:
        r"""Return information about a Telegram Premium gift code

        Parameters:
            code (:class:`str`):
                The code to check

        Returns:
            :class:`~pytdbot.types.PremiumGiftCodeInfo`
        """

        return await self.invoke({"@type": "checkPremiumGiftCode", "code": code})

    async def applyPremiumGiftCode(
        self, code: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Applies a Telegram Premium gift code

        Parameters:
            code (:class:`str`):
                The code to apply

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "applyPremiumGiftCode", "code": code})

    async def giftPremiumWithStars(
        self,
        user_id: int = 0,
        star_count: int = 0,
        month_count: int = 0,
        text: "types.FormattedText" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Allows to buy a Telegram Premium subscription for another user with payment in Telegram Stars; for bots only

        Parameters:
            user_id (:class:`int`):
                Identifier of the user which will receive Telegram Premium

            star_count (:class:`int`):
                The number of Telegram Stars to pay for subscription

            month_count (:class:`int`):
                Number of months the Telegram Premium subscription will be active for the user

            text (:class:`"types.FormattedText"`):
                Text to show to the user receiving Telegram Premium; 0\-getOption\(\"gift\_text\_length\_max\"\) characters\. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "giftPremiumWithStars",
                "user_id": user_id,
                "star_count": star_count,
                "month_count": month_count,
                "text": text,
            }
        )

    async def launchPrepaidGiveaway(
        self,
        giveaway_id: int = 0,
        parameters: "types.GiveawayParameters" = None,
        winner_count: int = 0,
        star_count: int = 0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Launches a prepaid giveaway

        Parameters:
            giveaway_id (:class:`int`):
                Unique identifier of the prepaid giveaway

            parameters (:class:`"types.GiveawayParameters"`):
                Giveaway parameters

            winner_count (:class:`int`):
                The number of users to receive giveaway prize

            star_count (:class:`int`):
                The number of Telegram Stars to be distributed through the giveaway; pass 0 for Telegram Premium giveaways

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "launchPrepaidGiveaway",
                "giveaway_id": giveaway_id,
                "parameters": parameters,
                "winner_count": winner_count,
                "star_count": star_count,
            }
        )

    async def getGiveawayInfo(
        self, chat_id: int = 0, message_id: int = 0
    ) -> Union["types.Error", "types.GiveawayInfo"]:
        r"""Returns information about a giveaway

        Parameters:
            chat_id (:class:`int`):
                Identifier of the channel chat which started the giveaway

            message_id (:class:`int`):
                Identifier of the giveaway or a giveaway winners message in the chat

        Returns:
            :class:`~pytdbot.types.GiveawayInfo`
        """

        return await self.invoke(
            {"@type": "getGiveawayInfo", "chat_id": chat_id, "message_id": message_id}
        )

    async def getStarPaymentOptions(
        self,
    ) -> Union["types.Error", "types.StarPaymentOptions"]:
        r"""Returns available options for Telegram Stars purchase

        Returns:
            :class:`~pytdbot.types.StarPaymentOptions`
        """

        return await self.invoke(
            {
                "@type": "getStarPaymentOptions",
            }
        )

    async def getStarGiftPaymentOptions(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.StarPaymentOptions"]:
        r"""Returns available options for Telegram Stars gifting

        Parameters:
            user_id (:class:`int`):
                Identifier of the user that will receive Telegram Stars; pass 0 to get options for an unspecified user

        Returns:
            :class:`~pytdbot.types.StarPaymentOptions`
        """

        return await self.invoke(
            {"@type": "getStarGiftPaymentOptions", "user_id": user_id}
        )

    async def getStarGiveawayPaymentOptions(
        self,
    ) -> Union["types.Error", "types.StarGiveawayPaymentOptions"]:
        r"""Returns available options for Telegram Star giveaway creation

        Returns:
            :class:`~pytdbot.types.StarGiveawayPaymentOptions`
        """

        return await self.invoke(
            {
                "@type": "getStarGiveawayPaymentOptions",
            }
        )

    async def getStarTransactions(
        self,
        owner_id: "types.MessageSender" = None,
        subscription_id: str = "",
        direction: "types.StarTransactionDirection" = None,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.StarTransactions"]:
        r"""Returns the list of Telegram Star transactions for the specified owner

        Parameters:
            owner_id (:class:`"types.MessageSender"`):
                Identifier of the owner of the Telegram Stars; can be the identifier of the current user, identifier of an owned bot, or identifier of a supergroup or a channel chat with supergroupFullInfo\.can\_get\_star\_revenue\_statistics \=\= true

            subscription_id (:class:`str`):
                If non\-empty, only transactions related to the Star Subscription will be returned

            direction (:class:`"types.StarTransactionDirection"`):
                Direction of the transactions to receive; pass null to get all transactions

            offset (:class:`str`):
                Offset of the first transaction to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of transactions to return

        Returns:
            :class:`~pytdbot.types.StarTransactions`
        """

        return await self.invoke(
            {
                "@type": "getStarTransactions",
                "owner_id": owner_id,
                "subscription_id": subscription_id,
                "direction": direction,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getStarSubscriptions(
        self, only_expiring: bool = False, offset: str = ""
    ) -> Union["types.Error", "types.StarSubscriptions"]:
        r"""Returns the list of Telegram Star subscriptions for the current user

        Parameters:
            only_expiring (:class:`bool`):
                Pass true to receive only expiring subscriptions for which there are no enough Telegram Stars to extend

            offset (:class:`str`):
                Offset of the first subscription to return as received from the previous request; use empty string to get the first chunk of results

        Returns:
            :class:`~pytdbot.types.StarSubscriptions`
        """

        return await self.invoke(
            {
                "@type": "getStarSubscriptions",
                "only_expiring": only_expiring,
                "offset": offset,
            }
        )

    async def canPurchaseFromStore(
        self, purpose: "types.StorePaymentPurpose" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Checks whether an in\-store purchase is possible\. Must be called before any in\-store purchase\. For official applications only

        Parameters:
            purpose (:class:`"types.StorePaymentPurpose"`):
                Transaction purpose

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "canPurchaseFromStore", "purpose": purpose})

    async def assignStoreTransaction(
        self,
        transaction: "types.StoreTransaction" = None,
        purpose: "types.StorePaymentPurpose" = None,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Informs server about an in\-store purchase\. For official applications only

        Parameters:
            transaction (:class:`"types.StoreTransaction"`):
                Information about the transaction

            purpose (:class:`"types.StorePaymentPurpose"`):
                Transaction purpose

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "assignStoreTransaction",
                "transaction": transaction,
                "purpose": purpose,
            }
        )

    async def editStarSubscription(
        self, subscription_id: str = "", is_canceled: bool = False
    ) -> Union["types.Error", "types.Ok"]:
        r"""Cancels or re\-enables Telegram Star subscription

        Parameters:
            subscription_id (:class:`str`):
                Identifier of the subscription to change

            is_canceled (:class:`bool`):
                New value of is\_canceled

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editStarSubscription",
                "subscription_id": subscription_id,
                "is_canceled": is_canceled,
            }
        )

    async def editUserStarSubscription(
        self,
        user_id: int = 0,
        telegram_payment_charge_id: str = "",
        is_canceled: bool = False,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Cancels or re\-enables Telegram Star subscription for a user; for bots only

        Parameters:
            user_id (:class:`int`):
                User identifier

            telegram_payment_charge_id (:class:`str`):
                Telegram payment identifier of the subscription

            is_canceled (:class:`bool`):
                Pass true to cancel the subscription; pass false to allow the user to enable it

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "editUserStarSubscription",
                "user_id": user_id,
                "telegram_payment_charge_id": telegram_payment_charge_id,
                "is_canceled": is_canceled,
            }
        )

    async def reuseStarSubscription(
        self, subscription_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Reuses an active Telegram Star subscription to a channel chat and joins the chat again

        Parameters:
            subscription_id (:class:`str`):
                Identifier of the subscription

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "reuseStarSubscription", "subscription_id": subscription_id}
        )

    async def setChatAffiliateProgram(
        self, chat_id: int = 0, parameters: "types.AffiliateProgramParameters" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Changes affiliate program for a bot

        Parameters:
            chat_id (:class:`int`):
                Identifier of the chat with an owned bot for which affiliate program is changed

            parameters (:class:`"types.AffiliateProgramParameters"`):
                Parameters of the affiliate program; pass null to close the currently active program\. If there is an active program, then commission and program duration can only be increased\. If the active program is scheduled to be closed, then it can't be changed anymore

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setChatAffiliateProgram",
                "chat_id": chat_id,
                "parameters": parameters,
            }
        )

    async def searchChatAffiliateProgram(
        self, username: str = "", referrer: str = ""
    ) -> Union["types.Error", "types.Chat"]:
        r"""Searches a chat with an affiliate program\. Returns the chat if found and the program is active

        Parameters:
            username (:class:`str`):
                Username of the chat

            referrer (:class:`str`):
                The referrer from an internalLinkTypeChatAffiliateProgram link

        Returns:
            :class:`~pytdbot.types.Chat`
        """

        return await self.invoke(
            {
                "@type": "searchChatAffiliateProgram",
                "username": username,
                "referrer": referrer,
            }
        )

    async def searchAffiliatePrograms(
        self,
        affiliate: "types.AffiliateType" = None,
        sort_order: "types.AffiliateProgramSortOrder" = None,
        offset: str = "",
        limit: int = 0,
    ) -> Union["types.Error", "types.FoundAffiliatePrograms"]:
        r"""Searches affiliate programs that can be connected to the given affiliate

        Parameters:
            affiliate (:class:`"types.AffiliateType"`):
                The affiliate for which affiliate programs are searched for

            sort_order (:class:`"types.AffiliateProgramSortOrder"`):
                Sort order for the results

            offset (:class:`str`):
                Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of affiliate programs to return

        Returns:
            :class:`~pytdbot.types.FoundAffiliatePrograms`
        """

        return await self.invoke(
            {
                "@type": "searchAffiliatePrograms",
                "affiliate": affiliate,
                "sort_order": sort_order,
                "offset": offset,
                "limit": limit,
            }
        )

    async def connectAffiliateProgram(
        self, affiliate: "types.AffiliateType" = None, bot_user_id: int = 0
    ) -> Union["types.Error", "types.ConnectedAffiliateProgram"]:
        r"""Connects an affiliate program to the given affiliate\. Returns information about the connected affiliate program

        Parameters:
            affiliate (:class:`"types.AffiliateType"`):
                The affiliate to which the affiliate program will be connected

            bot_user_id (:class:`int`):
                Identifier of the bot, which affiliate program is connected

        Returns:
            :class:`~pytdbot.types.ConnectedAffiliateProgram`
        """

        return await self.invoke(
            {
                "@type": "connectAffiliateProgram",
                "affiliate": affiliate,
                "bot_user_id": bot_user_id,
            }
        )

    async def disconnectAffiliateProgram(
        self, affiliate: "types.AffiliateType" = None, url: str = ""
    ) -> Union["types.Error", "types.ConnectedAffiliateProgram"]:
        r"""Disconnects an affiliate program from the given affiliate and immediately deactivates its referral link\. Returns updated information about the disconnected affiliate program

        Parameters:
            affiliate (:class:`"types.AffiliateType"`):
                The affiliate to which the affiliate program is connected

            url (:class:`str`):
                The referral link of the affiliate program

        Returns:
            :class:`~pytdbot.types.ConnectedAffiliateProgram`
        """

        return await self.invoke(
            {"@type": "disconnectAffiliateProgram", "affiliate": affiliate, "url": url}
        )

    async def getConnectedAffiliateProgram(
        self, affiliate: "types.AffiliateType" = None, bot_user_id: int = 0
    ) -> Union["types.Error", "types.ConnectedAffiliateProgram"]:
        r"""Returns an affiliate program that were connected to the given affiliate by identifier of the bot that created the program

        Parameters:
            affiliate (:class:`"types.AffiliateType"`):
                The affiliate to which the affiliate program will be connected

            bot_user_id (:class:`int`):
                Identifier of the bot that created the program

        Returns:
            :class:`~pytdbot.types.ConnectedAffiliateProgram`
        """

        return await self.invoke(
            {
                "@type": "getConnectedAffiliateProgram",
                "affiliate": affiliate,
                "bot_user_id": bot_user_id,
            }
        )

    async def getConnectedAffiliatePrograms(
        self, affiliate: "types.AffiliateType" = None, offset: str = "", limit: int = 0
    ) -> Union["types.Error", "types.ConnectedAffiliatePrograms"]:
        r"""Returns affiliate programs that were connected to the given affiliate

        Parameters:
            affiliate (:class:`"types.AffiliateType"`):
                The affiliate to which the affiliate program were connected

            offset (:class:`str`):
                Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results

            limit (:class:`int`):
                The maximum number of affiliate programs to return

        Returns:
            :class:`~pytdbot.types.ConnectedAffiliatePrograms`
        """

        return await self.invoke(
            {
                "@type": "getConnectedAffiliatePrograms",
                "affiliate": affiliate,
                "offset": offset,
                "limit": limit,
            }
        )

    async def getBusinessFeatures(
        self, source: "types.BusinessFeature" = None
    ) -> Union["types.Error", "types.BusinessFeatures"]:
        r"""Returns information about features, available to Business users

        Parameters:
            source (:class:`"types.BusinessFeature"`):
                Source of the request; pass null if the method is called from settings or some non\-standard source

        Returns:
            :class:`~pytdbot.types.BusinessFeatures`
        """

        return await self.invoke({"@type": "getBusinessFeatures", "source": source})

    async def acceptTermsOfService(
        self, terms_of_service_id: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Accepts Telegram terms of services

        Parameters:
            terms_of_service_id (:class:`str`):
                Terms of service identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "acceptTermsOfService",
                "terms_of_service_id": terms_of_service_id,
            }
        )

    async def searchStringsByPrefix(
        self,
        strings: List[str] = None,
        query: str = "",
        limit: int = 0,
        return_none_for_empty_query: bool = False,
    ) -> Union["types.Error", "types.FoundPositions"]:
        r"""Searches specified query by word prefixes in the provided strings\. Returns 0\-based positions of strings that matched\. Can be called synchronously

        Parameters:
            strings (:class:`List[str]`):
                The strings to search in for the query

            query (:class:`str`):
                Query to search for

            limit (:class:`int`):
                The maximum number of objects to return

            return_none_for_empty_query (:class:`bool`):
                Pass true to receive no results for an empty query

        Returns:
            :class:`~pytdbot.types.FoundPositions`
        """

        return await self.invoke(
            {
                "@type": "searchStringsByPrefix",
                "strings": strings,
                "query": query,
                "limit": limit,
                "return_none_for_empty_query": return_none_for_empty_query,
            }
        )

    async def sendCustomRequest(
        self, method: str = "", parameters: str = ""
    ) -> Union["types.Error", "types.CustomRequestResult"]:
        r"""Sends a custom request; for bots only

        Parameters:
            method (:class:`str`):
                The method name

            parameters (:class:`str`):
                JSON\-serialized method parameters

        Returns:
            :class:`~pytdbot.types.CustomRequestResult`
        """

        return await self.invoke(
            {"@type": "sendCustomRequest", "method": method, "parameters": parameters}
        )

    async def answerCustomQuery(
        self, custom_query_id: int = 0, data: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Answers a custom query; for bots only

        Parameters:
            custom_query_id (:class:`int`):
                Identifier of a custom query

            data (:class:`str`):
                JSON\-serialized answer to the query

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "answerCustomQuery",
                "custom_query_id": custom_query_id,
                "data": data,
            }
        )

    async def setAlarm(self, seconds: float = 0.0) -> Union["types.Error", "types.Ok"]:
        r"""Succeeds after a specified amount of time has passed\. Can be called before initialization

        Parameters:
            seconds (:class:`float`):
                Number of seconds before the function returns

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setAlarm", "seconds": seconds})

    async def getCountries(self) -> Union["types.Error", "types.Countries"]:
        r"""Returns information about existing countries\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Countries`
        """

        return await self.invoke(
            {
                "@type": "getCountries",
            }
        )

    async def getCountryCode(self) -> Union["types.Error", "types.Text"]:
        r"""Uses the current IP address to find the current country\. Returns two\-letter ISO 3166\-1 alpha\-2 country code\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getCountryCode",
            }
        )

    async def getPhoneNumberInfo(
        self, phone_number_prefix: str = ""
    ) -> Union["types.Error", "types.PhoneNumberInfo"]:
        r"""Returns information about a phone number by its prefix\. Can be called before authorization

        Parameters:
            phone_number_prefix (:class:`str`):
                The phone number prefix

        Returns:
            :class:`~pytdbot.types.PhoneNumberInfo`
        """

        return await self.invoke(
            {"@type": "getPhoneNumberInfo", "phone_number_prefix": phone_number_prefix}
        )

    async def getPhoneNumberInfoSync(
        self, language_code: str = "", phone_number_prefix: str = ""
    ) -> Union["types.Error", "types.PhoneNumberInfo"]:
        r"""Returns information about a phone number by its prefix synchronously\. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected\. Can be called synchronously

        Parameters:
            language_code (:class:`str`):
                A two\-letter ISO 639\-1 language code for country information localization

            phone_number_prefix (:class:`str`):
                The phone number prefix

        Returns:
            :class:`~pytdbot.types.PhoneNumberInfo`
        """

        return await self.invoke(
            {
                "@type": "getPhoneNumberInfoSync",
                "language_code": language_code,
                "phone_number_prefix": phone_number_prefix,
            }
        )

    async def getCollectibleItemInfo(
        self, type: "types.CollectibleItemType" = None
    ) -> Union["types.Error", "types.CollectibleItemInfo"]:
        r"""Returns information about a given collectible item that was purchased at https://fragment\.com

        Parameters:
            type (:class:`"types.CollectibleItemType"`):
                Type of the collectible item\. The item must be used by a user and must be visible to the current user

        Returns:
            :class:`~pytdbot.types.CollectibleItemInfo`
        """

        return await self.invoke({"@type": "getCollectibleItemInfo", "type": type})

    async def getDeepLinkInfo(
        self, link: str = ""
    ) -> Union["types.Error", "types.DeepLinkInfo"]:
        r"""Returns information about a tg:// deep link\. Use \"tg://need\_update\_for\_some\_feature\" or \"tg:some\_unsupported\_feature\" for testing\. Returns a 404 error for unknown links\. Can be called before authorization

        Parameters:
            link (:class:`str`):
                The link

        Returns:
            :class:`~pytdbot.types.DeepLinkInfo`
        """

        return await self.invoke({"@type": "getDeepLinkInfo", "link": link})

    async def getApplicationConfig(self) -> Union["types.Error", "types.JsonValue"]:
        r"""Returns application config, provided by the server\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.JsonValue`
        """

        return await self.invoke(
            {
                "@type": "getApplicationConfig",
            }
        )

    async def saveApplicationLogEvent(
        self, type: str = "", chat_id: int = 0, data: "types.JsonValue" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Saves application log event on the server\. Can be called before authorization

        Parameters:
            type (:class:`str`):
                Event type

            chat_id (:class:`int`):
                Optional chat identifier, associated with the event

            data (:class:`"types.JsonValue"`):
                The log event data

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "saveApplicationLogEvent",
                "type": type,
                "chat_id": chat_id,
                "data": data,
            }
        )

    async def getApplicationDownloadLink(self) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke(
            {
                "@type": "getApplicationDownloadLink",
            }
        )

    async def addProxy(
        self,
        server: str = "",
        port: int = 0,
        enable: bool = False,
        type: "types.ProxyType" = None,
    ) -> Union["types.Error", "types.Proxy"]:
        r"""Adds a proxy server for network requests\. Can be called before authorization

        Parameters:
            server (:class:`str`):
                Proxy server domain or IP address

            port (:class:`int`):
                Proxy server port

            enable (:class:`bool`):
                Pass true to immediately enable the proxy

            type (:class:`"types.ProxyType"`):
                Proxy type

        Returns:
            :class:`~pytdbot.types.Proxy`
        """

        return await self.invoke(
            {
                "@type": "addProxy",
                "server": server,
                "port": port,
                "enable": enable,
                "type": type,
            }
        )

    async def editProxy(
        self,
        proxy_id: int = 0,
        server: str = "",
        port: int = 0,
        enable: bool = False,
        type: "types.ProxyType" = None,
    ) -> Union["types.Error", "types.Proxy"]:
        r"""Edits an existing proxy server for network requests\. Can be called before authorization

        Parameters:
            proxy_id (:class:`int`):
                Proxy identifier

            server (:class:`str`):
                Proxy server domain or IP address

            port (:class:`int`):
                Proxy server port

            enable (:class:`bool`):
                Pass true to immediately enable the proxy

            type (:class:`"types.ProxyType"`):
                Proxy type

        Returns:
            :class:`~pytdbot.types.Proxy`
        """

        return await self.invoke(
            {
                "@type": "editProxy",
                "proxy_id": proxy_id,
                "server": server,
                "port": port,
                "enable": enable,
                "type": type,
            }
        )

    async def enableProxy(self, proxy_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Enables a proxy\. Only one proxy can be enabled at a time\. Can be called before authorization

        Parameters:
            proxy_id (:class:`int`):
                Proxy identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "enableProxy", "proxy_id": proxy_id})

    async def disableProxy(self) -> Union["types.Error", "types.Ok"]:
        r"""Disables the currently enabled proxy\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "disableProxy",
            }
        )

    async def removeProxy(self, proxy_id: int = 0) -> Union["types.Error", "types.Ok"]:
        r"""Removes a proxy server\. Can be called before authorization

        Parameters:
            proxy_id (:class:`int`):
                Proxy identifier

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "removeProxy", "proxy_id": proxy_id})

    async def getProxies(self) -> Union["types.Error", "types.Proxies"]:
        r"""Returns the list of proxies that are currently set up\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Proxies`
        """

        return await self.invoke(
            {
                "@type": "getProxies",
            }
        )

    async def getProxyLink(
        self, proxy_id: int = 0
    ) -> Union["types.Error", "types.HttpUrl"]:
        r"""Returns an HTTPS link, which can be used to add a proxy\. Available only for SOCKS5 and MTProto proxies\. Can be called before authorization

        Parameters:
            proxy_id (:class:`int`):
                Proxy identifier

        Returns:
            :class:`~pytdbot.types.HttpUrl`
        """

        return await self.invoke({"@type": "getProxyLink", "proxy_id": proxy_id})

    async def pingProxy(
        self, proxy_id: int = 0
    ) -> Union["types.Error", "types.Seconds"]:
        r"""Computes time needed to receive a response from a Telegram server through a proxy\. Can be called before authorization

        Parameters:
            proxy_id (:class:`int`):
                Proxy identifier\. Use 0 to ping a Telegram server without a proxy

        Returns:
            :class:`~pytdbot.types.Seconds`
        """

        return await self.invoke({"@type": "pingProxy", "proxy_id": proxy_id})

    async def setLogStream(
        self, log_stream: "types.LogStream" = None
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets new log stream for internal logging of TDLib\. Can be called synchronously

        Parameters:
            log_stream (:class:`"types.LogStream"`):
                New log stream

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke({"@type": "setLogStream", "log_stream": log_stream})

    async def getLogStream(self) -> Union["types.Error", "types.LogStream"]:
        r"""Returns information about currently used log stream for internal logging of TDLib\. Can be called synchronously

        Returns:
            :class:`~pytdbot.types.LogStream`
        """

        return await self.invoke(
            {
                "@type": "getLogStream",
            }
        )

    async def setLogVerbosityLevel(
        self, new_verbosity_level: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the verbosity level of the internal logging of TDLib\. Can be called synchronously

        Parameters:
            new_verbosity_level (:class:`int`):
                New value of the verbosity level for logging\. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setLogVerbosityLevel",
                "new_verbosity_level": new_verbosity_level,
            }
        )

    async def getLogVerbosityLevel(
        self,
    ) -> Union["types.Error", "types.LogVerbosityLevel"]:
        r"""Returns current verbosity level of the internal logging of TDLib\. Can be called synchronously

        Returns:
            :class:`~pytdbot.types.LogVerbosityLevel`
        """

        return await self.invoke(
            {
                "@type": "getLogVerbosityLevel",
            }
        )

    async def getLogTags(self) -> Union["types.Error", "types.LogTags"]:
        r"""Returns the list of available TDLib internal log tags, for example, \[\"actor\", \"binlog\", \"connections\", \"notifications\", \"proxy\"\]\. Can be called synchronously

        Returns:
            :class:`~pytdbot.types.LogTags`
        """

        return await self.invoke(
            {
                "@type": "getLogTags",
            }
        )

    async def setLogTagVerbosityLevel(
        self, tag: str = "", new_verbosity_level: int = 0
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sets the verbosity level for a specified TDLib internal log tag\. Can be called synchronously

        Parameters:
            tag (:class:`str`):
                Logging tag to change verbosity level

            new_verbosity_level (:class:`int`):
                New verbosity level; 1\-1024

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "setLogTagVerbosityLevel",
                "tag": tag,
                "new_verbosity_level": new_verbosity_level,
            }
        )

    async def getLogTagVerbosityLevel(
        self, tag: str = ""
    ) -> Union["types.Error", "types.LogVerbosityLevel"]:
        r"""Returns current verbosity level for a specified TDLib internal log tag\. Can be called synchronously

        Parameters:
            tag (:class:`str`):
                Logging tag to change verbosity level

        Returns:
            :class:`~pytdbot.types.LogVerbosityLevel`
        """

        return await self.invoke({"@type": "getLogTagVerbosityLevel", "tag": tag})

    async def addLogMessage(
        self, verbosity_level: int = 0, text: str = ""
    ) -> Union["types.Error", "types.Ok"]:
        r"""Adds a message to TDLib internal log\. Can be called synchronously

        Parameters:
            verbosity_level (:class:`int`):
                The minimum verbosity level needed for the message to be logged; 0\-1023

            text (:class:`str`):
                Text of a message to log

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {"@type": "addLogMessage", "verbosity_level": verbosity_level, "text": text}
        )

    async def getUserSupportInfo(
        self, user_id: int = 0
    ) -> Union["types.Error", "types.UserSupportInfo"]:
        r"""Returns support information for the given user; for Telegram support only

        Parameters:
            user_id (:class:`int`):
                User identifier

        Returns:
            :class:`~pytdbot.types.UserSupportInfo`
        """

        return await self.invoke({"@type": "getUserSupportInfo", "user_id": user_id})

    async def setUserSupportInfo(
        self, user_id: int = 0, message: "types.FormattedText" = None
    ) -> Union["types.Error", "types.UserSupportInfo"]:
        r"""Sets support information for the given user; for Telegram support only

        Parameters:
            user_id (:class:`int`):
                User identifier

            message (:class:`"types.FormattedText"`):
                New information message

        Returns:
            :class:`~pytdbot.types.UserSupportInfo`
        """

        return await self.invoke(
            {"@type": "setUserSupportInfo", "user_id": user_id, "message": message}
        )

    async def getSupportName(self) -> Union["types.Error", "types.Text"]:
        r"""Returns localized name of the Telegram support user; for Telegram support only

        Returns:
            :class:`~pytdbot.types.Text`
        """

        return await self.invoke(
            {
                "@type": "getSupportName",
            }
        )

    async def testCallEmpty(self) -> Union["types.Error", "types.Ok"]:
        r"""Does nothing; for testing only\. This is an offline method\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "testCallEmpty",
            }
        )

    async def testCallString(
        self, x: str = ""
    ) -> Union["types.Error", "types.TestString"]:
        r"""Returns the received string; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`str`):
                String to return

        Returns:
            :class:`~pytdbot.types.TestString`
        """

        return await self.invoke({"@type": "testCallString", "x": x})

    async def testCallBytes(
        self, x: bytes = b""
    ) -> Union["types.Error", "types.TestBytes"]:
        r"""Returns the received bytes; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`bytes`):
                Bytes to return

        Returns:
            :class:`~pytdbot.types.TestBytes`
        """

        return await self.invoke({"@type": "testCallBytes", "x": x})

    async def testCallVectorInt(
        self, x: List[int] = None
    ) -> Union["types.Error", "types.TestVectorInt"]:
        r"""Returns the received vector of numbers; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`List[int]`):
                Vector of numbers to return

        Returns:
            :class:`~pytdbot.types.TestVectorInt`
        """

        return await self.invoke({"@type": "testCallVectorInt", "x": x})

    async def testCallVectorIntObject(
        self, x: List["types.TestInt"] = None
    ) -> Union["types.Error", "types.TestVectorIntObject"]:
        r"""Returns the received vector of objects containing a number; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`List["types.TestInt"]`):
                Vector of objects to return

        Returns:
            :class:`~pytdbot.types.TestVectorIntObject`
        """

        return await self.invoke({"@type": "testCallVectorIntObject", "x": x})

    async def testCallVectorString(
        self, x: List[str] = None
    ) -> Union["types.Error", "types.TestVectorString"]:
        r"""Returns the received vector of strings; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`List[str]`):
                Vector of strings to return

        Returns:
            :class:`~pytdbot.types.TestVectorString`
        """

        return await self.invoke({"@type": "testCallVectorString", "x": x})

    async def testCallVectorStringObject(
        self, x: List["types.TestString"] = None
    ) -> Union["types.Error", "types.TestVectorStringObject"]:
        r"""Returns the received vector of objects containing a string; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`List["types.TestString"]`):
                Vector of objects to return

        Returns:
            :class:`~pytdbot.types.TestVectorStringObject`
        """

        return await self.invoke({"@type": "testCallVectorStringObject", "x": x})

    async def testSquareInt(self, x: int = 0) -> Union["types.Error", "types.TestInt"]:
        r"""Returns the squared received number; for testing only\. This is an offline method\. Can be called before authorization

        Parameters:
            x (:class:`int`):
                Number to square

        Returns:
            :class:`~pytdbot.types.TestInt`
        """

        return await self.invoke({"@type": "testSquareInt", "x": x})

    async def testNetwork(self) -> Union["types.Error", "types.Ok"]:
        r"""Sends a simple network request to the Telegram servers; for testing only\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "testNetwork",
            }
        )

    async def testProxy(
        self,
        server: str = "",
        port: int = 0,
        type: "types.ProxyType" = None,
        dc_id: int = 0,
        timeout: float = 0.0,
    ) -> Union["types.Error", "types.Ok"]:
        r"""Sends a simple network request to the Telegram servers via proxy; for testing only\. Can be called before authorization

        Parameters:
            server (:class:`str`):
                Proxy server domain or IP address

            port (:class:`int`):
                Proxy server port

            type (:class:`"types.ProxyType"`):
                Proxy type

            dc_id (:class:`int`):
                Identifier of a datacenter with which to test connection

            timeout (:class:`float`):
                The maximum overall timeout for the request

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "testProxy",
                "server": server,
                "port": port,
                "type": type,
                "dc_id": dc_id,
                "timeout": timeout,
            }
        )

    async def testGetDifference(self) -> Union["types.Error", "types.Ok"]:
        r"""Forces an updates\.getDifference call to the Telegram servers; for testing only

        Returns:
            :class:`~pytdbot.types.Ok`
        """

        return await self.invoke(
            {
                "@type": "testGetDifference",
            }
        )

    async def testUseUpdate(self) -> Union["types.Error", "types.Update"]:
        r"""Does nothing and ensures that the Update object is used; for testing only\. This is an offline method\. Can be called before authorization

        Returns:
            :class:`~pytdbot.types.Update`
        """

        return await self.invoke(
            {
                "@type": "testUseUpdate",
            }
        )

    async def testReturnError(
        self, error: "types.Error" = None
    ) -> Union["types.Error", "types.Error"]:
        r"""Returns the specified error and ensures that the Error object is used; for testing only\. Can be called synchronously

        Parameters:
            error (:class:`"types.Error"`):
                The error to be returned

        Returns:
            :class:`~pytdbot.types.Error`
        """

        return await self.invoke({"@type": "testReturnError", "error": error})
