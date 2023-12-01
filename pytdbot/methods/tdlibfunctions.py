from ..types import Result


class TDLibFunctions:
    """Auto generated TDLib functions"""

    async def getAuthorizationState(self) -> Result:
        """Returns the current authorization state; this is an offline request\. For informational purposes only\. Use updateAuthorizationState instead to maintain the current authorization state\. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Result` (``AuthorizationState``)
        """

        data = {
            "@type": "getAuthorizationState",
        }

        return await self.invoke(data)

    async def setTdlibParameters(
        self,
        use_test_dc: bool,
        database_directory: str,
        files_directory: str,
        database_encryption_key: bytes,
        use_file_database: bool,
        use_chat_info_database: bool,
        use_message_database: bool,
        use_secret_chats: bool,
        api_id: int,
        api_hash: str,
        system_language_code: str,
        device_model: str,
        system_version: str,
        application_version: str,
        enable_storage_optimizer: bool,
        ignore_file_names: bool,
    ) -> Result:
        """Sets the parameters for TDLib initialization\. Works only when the current authorization state is authorizationStateWaitTdlibParameters

        Args:
            use_test_dc (``bool``):
                Pass true to use Telegram test environment instead of the production environment

            database_directory (``str``):
                The path to the directory for the persistent database; if empty, the current working directory will be used

            files_directory (``str``):
                The path to the directory for storing files; if empty, database\_directory will be used

            database_encryption_key (``bytes``):
                Encryption key for the database\. If the encryption key is invalid, then an error with code 401 will be returned

            use_file_database (``bool``):
                Pass true to keep information about downloaded and uploaded files between application restarts

            use_chat_info_database (``bool``):
                Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts\. Implies use\_file\_database

            use_message_database (``bool``):
                Pass true to keep cache of chats and messages between restarts\. Implies use\_chat\_info\_database

            use_secret_chats (``bool``):
                Pass true to enable support for secret chats

            api_id (``int``):
                Application identifier for Telegram API access, which can be obtained at https://my\.telegram\.org

            api_hash (``str``):
                Application identifier hash for Telegram API access, which can be obtained at https://my\.telegram\.org

            system_language_code (``str``):
                IETF language tag of the user's operating system language; must be non\-empty

            device_model (``str``):
                Model of the device the application is being run on; must be non\-empty

            system_version (``str``):
                Version of the operating system the application is being run on\. If empty, the version is automatically detected by TDLib

            application_version (``str``):
                Application version; must be non\-empty

            enable_storage_optimizer (``bool``):
                Pass true to automatically delete old files in background

            ignore_file_names (``bool``):
                Pass true to ignore original file names for downloaded files\. Otherwise, downloaded files are saved under names as close as possible to the original name


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
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
            "enable_storage_optimizer": enable_storage_optimizer,
            "ignore_file_names": ignore_file_names,
        }

        return await self.invoke(data)

    async def setAuthenticationPhoneNumber(
        self, phone_number: str, settings: dict = None
    ) -> Result:
        """Sets the phone number of the user and sends an authentication code to the user\. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Args:
            phone_number (``str``):
                The phone number of the user, in international format

            settings (``phoneNumberAuthenticationSettings``, *optional*):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAuthenticationPhoneNumber",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data)

    async def setAuthenticationEmailAddress(self, email_address: str) -> Result:
        """Sets the email address of the user and sends an authentication code to the email address\. Works only when the current authorization state is authorizationStateWaitEmailAddress

        Args:
            email_address (``str``):
                The email address of the user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAuthenticationEmailAddress",
            "email_address": email_address,
        }

        return await self.invoke(data)

    async def resendAuthenticationCode(self) -> Result:
        """Resends an authentication code to the user\. Works only when the current authorization state is authorizationStateWaitCode, the next\_code\_type of the result is not null and the server\-specified timeout has passed, or when the current authorization state is authorizationStateWaitEmailCode


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "resendAuthenticationCode",
        }

        return await self.invoke(data)

    async def checkAuthenticationEmailCode(self, code: dict) -> Result:
        """Checks the authentication of a email address\. Works only when the current authorization state is authorizationStateWaitEmailCode

        Args:
            code (``EmailAddressAuthentication``):
                Email address authentication to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkAuthenticationEmailCode",
            "code": code,
        }

        return await self.invoke(data)

    async def checkAuthenticationCode(self, code: str) -> Result:
        """Checks the authentication code\. Works only when the current authorization state is authorizationStateWaitCode

        Args:
            code (``str``):
                Authentication code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkAuthenticationCode",
            "code": code,
        }

        return await self.invoke(data)

    async def requestQrCodeAuthentication(self, other_user_ids: list) -> Result:
        """Requests QR code authentication by scanning a QR code on another logged in device\. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitEmailAddress, authorizationStateWaitEmailCode, authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Args:
            other_user_ids (``list``):
                List of user identifiers of other users currently using the application


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "requestQrCodeAuthentication",
            "other_user_ids": other_user_ids,
        }

        return await self.invoke(data)

    async def registerUser(self, first_name: str, last_name: str) -> Result:
        """Finishes user registration\. Works only when the current authorization state is authorizationStateWaitRegistration

        Args:
            first_name (``str``):
                The first name of the user; 1\-64 characters

            last_name (``str``):
                The last name of the user; 0\-64 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "registerUser",
            "first_name": first_name,
            "last_name": last_name,
        }

        return await self.invoke(data)

    async def resetAuthenticationEmailAddress(self) -> Result:
        """Resets the login email address\. May return an error with a message "TASK\_ALREADY\_EXISTS" if reset is still pending\. Works only when the current authorization state is authorizationStateWaitEmailCode and authorization\_state\.can\_reset\_email\_address \=\= true


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "resetAuthenticationEmailAddress",
        }

        return await self.invoke(data)

    async def checkAuthenticationPassword(self, password: str) -> Result:
        """Checks the 2\-step verification password for correctness\. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            password (``str``):
                The 2\-step verification password to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkAuthenticationPassword",
            "password": password,
        }

        return await self.invoke(data)

    async def requestAuthenticationPasswordRecovery(self) -> Result:
        """Requests to send a 2\-step verification password recovery code to an email address that was previously set up\. Works only when the current authorization state is authorizationStateWaitPassword


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "requestAuthenticationPasswordRecovery",
        }

        return await self.invoke(data)

    async def checkAuthenticationPasswordRecoveryCode(
        self, recovery_code: str
    ) -> Result:
        """Checks whether a 2\-step verification password recovery code sent to an email address is valid\. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            recovery_code (``str``):
                Recovery code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkAuthenticationPasswordRecoveryCode",
            "recovery_code": recovery_code,
        }

        return await self.invoke(data)

    async def recoverAuthenticationPassword(
        self, recovery_code: str, new_password: str = None, new_hint: str = None
    ) -> Result:
        """Recovers the 2\-step verification password with a password recovery code sent to an email address that was previously set up\. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            recovery_code (``str``):
                Recovery code to check

            new_password (``str``, *optional*):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (``str``, *optional*):
                New password hint; may be empty


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "recoverAuthenticationPassword",
            "recovery_code": recovery_code,
            "new_password": new_password,
            "new_hint": new_hint,
        }

        return await self.invoke(data)

    async def sendAuthenticationFirebaseSms(self, token: str) -> Result:
        """Sends Firebase Authentication SMS to the phone number of the user\. Works only when the current authorization state is authorizationStateWaitCode and the server returned code of the type authenticationCodeTypeFirebaseAndroid or authenticationCodeTypeFirebaseIos

        Args:
            token (``str``):
                SafetyNet Attestation API token for the Android application, or secret from push notification for the iOS application


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendAuthenticationFirebaseSms",
            "token": token,
        }

        return await self.invoke(data)

    async def checkAuthenticationBotToken(self, token: str) -> Result:
        """Checks the authentication token of a bot; to log in as a bot\. Works only when the current authorization state is authorizationStateWaitPhoneNumber\. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

        Args:
            token (``str``):
                The bot token


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkAuthenticationBotToken",
            "token": token,
        }

        return await self.invoke(data)

    async def logOut(self) -> Result:
        """Closes the TDLib instance after a proper logout\. Requires an available network connection\. All local data will be destroyed\. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "logOut",
        }

        return await self.invoke(data)

    async def close(self) -> Result:
        """Closes the TDLib instance\. All databases will be flushed to disk and properly closed\. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent\. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "close",
        }

        return await self.invoke(data)

    async def destroy(self) -> Result:
        """Closes the TDLib instance, destroying all local data without a proper logout\. The current user session will remain in the list of all active sessions\. All local data will be destroyed\. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "destroy",
        }

        return await self.invoke(data)

    async def confirmQrCodeAuthentication(self, link: str) -> Result:
        """Confirms QR code authentication on another device\. Returns created session on success

        Args:
            link (``str``):
                A link from a QR code\. The link must be scanned by the in\-app camera


        Returns:
            :class:`~pytdbot.types.Result` (``Session``)
        """

        data = {
            "@type": "confirmQrCodeAuthentication",
            "link": link,
        }

        return await self.invoke(data)

    async def getCurrentState(self) -> Result:
        """Returns all updates needed to restore current TDLib state, i\.e\. all actual updateAuthorizationState/updateUser/updateNewChat and others\. This is especially useful if TDLib is run in a separate process\. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Result` (``Updates``)
        """

        data = {
            "@type": "getCurrentState",
        }

        return await self.invoke(data)

    async def setDatabaseEncryptionKey(self, new_encryption_key: bytes) -> Result:
        """Changes the database encryption key\. Usually the encryption key is never changed and is stored in some OS keychain

        Args:
            new_encryption_key (``bytes``):
                New encryption key


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setDatabaseEncryptionKey",
            "new_encryption_key": new_encryption_key,
        }

        return await self.invoke(data)

    async def getPasswordState(self) -> Result:
        """Returns the current state of 2\-step verification


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "getPasswordState",
        }

        return await self.invoke(data)

    async def setPassword(
        self,
        old_password: str,
        set_recovery_email_address: bool,
        new_password: str = None,
        new_hint: str = None,
        new_recovery_email_address: str = None,
    ) -> Result:
        """Changes the 2\-step verification password for the current user\. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

        Args:
            old_password (``str``):
                Previous 2\-step verification password of the user

            set_recovery_email_address (``bool``):
                Pass true to change also the recovery email address

            new_password (``str``, *optional*):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (``str``, *optional*):
                New password hint; may be empty

            new_recovery_email_address (``str``, *optional*):
                New recovery email address; may be empty


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "setPassword",
            "old_password": old_password,
            "new_password": new_password,
            "new_hint": new_hint,
            "set_recovery_email_address": set_recovery_email_address,
            "new_recovery_email_address": new_recovery_email_address,
        }

        return await self.invoke(data)

    async def setLoginEmailAddress(self, new_login_email_address: str) -> Result:
        """Changes the login email address of the user\. The email address can be changed only if the current user already has login email and passwordState\.login\_email\_address\_pattern is non\-empty\. The change will not be applied until the new login email address is confirmed with checkLoginEmailAddressCode\. To use Apple ID/Google ID instead of a email address, call checkLoginEmailAddressCode directly

        Args:
            new_login_email_address (``str``):
                New login email address


        Returns:
            :class:`~pytdbot.types.Result` (``EmailAddressAuthenticationCodeInfo``)
        """

        data = {
            "@type": "setLoginEmailAddress",
            "new_login_email_address": new_login_email_address,
        }

        return await self.invoke(data)

    async def resendLoginEmailAddressCode(self) -> Result:
        """Resends the login email address verification code


        Returns:
            :class:`~pytdbot.types.Result` (``EmailAddressAuthenticationCodeInfo``)
        """

        data = {
            "@type": "resendLoginEmailAddressCode",
        }

        return await self.invoke(data)

    async def checkLoginEmailAddressCode(self, code: dict) -> Result:
        """Checks the login email address authentication

        Args:
            code (``EmailAddressAuthentication``):
                Email address authentication to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkLoginEmailAddressCode",
            "code": code,
        }

        return await self.invoke(data)

    async def getRecoveryEmailAddress(self, password: str) -> Result:
        """Returns a 2\-step verification recovery email address that was previously set up\. This method can be used to verify a password provided by the user

        Args:
            password (``str``):
                The 2\-step verification password for the current user


        Returns:
            :class:`~pytdbot.types.Result` (``RecoveryEmailAddress``)
        """

        data = {
            "@type": "getRecoveryEmailAddress",
            "password": password,
        }

        return await self.invoke(data)

    async def setRecoveryEmailAddress(
        self, password: str, new_recovery_email_address: str
    ) -> Result:
        """Changes the 2\-step verification recovery email address of the user\. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed\. If new\_recovery\_email\_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation

        Args:
            password (``str``):
                The 2\-step verification password of the current user

            new_recovery_email_address (``str``):
                New recovery email address


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "setRecoveryEmailAddress",
            "password": password,
            "new_recovery_email_address": new_recovery_email_address,
        }

        return await self.invoke(data)

    async def checkRecoveryEmailAddressCode(self, code: str) -> Result:
        """Checks the 2\-step verification recovery email address verification code

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "checkRecoveryEmailAddressCode",
            "code": code,
        }

        return await self.invoke(data)

    async def resendRecoveryEmailAddressCode(self) -> Result:
        """Resends the 2\-step verification recovery email address verification code


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "resendRecoveryEmailAddressCode",
        }

        return await self.invoke(data)

    async def requestPasswordRecovery(self) -> Result:
        """Requests to send a 2\-step verification password recovery code to an email address that was previously set up


        Returns:
            :class:`~pytdbot.types.Result` (``EmailAddressAuthenticationCodeInfo``)
        """

        data = {
            "@type": "requestPasswordRecovery",
        }

        return await self.invoke(data)

    async def checkPasswordRecoveryCode(self, recovery_code: str) -> Result:
        """Checks whether a 2\-step verification password recovery code sent to an email address is valid

        Args:
            recovery_code (``str``):
                Recovery code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkPasswordRecoveryCode",
            "recovery_code": recovery_code,
        }

        return await self.invoke(data)

    async def recoverPassword(
        self, recovery_code: str, new_password: str = None, new_hint: str = None
    ) -> Result:
        """Recovers the 2\-step verification password using a recovery code sent to an email address that was previously set up

        Args:
            recovery_code (``str``):
                Recovery code to check

            new_password (``str``, *optional*):
                New 2\-step verification password of the user; may be empty to remove the password

            new_hint (``str``, *optional*):
                New password hint; may be empty


        Returns:
            :class:`~pytdbot.types.Result` (``PasswordState``)
        """

        data = {
            "@type": "recoverPassword",
            "recovery_code": recovery_code,
            "new_password": new_password,
            "new_hint": new_hint,
        }

        return await self.invoke(data)

    async def resetPassword(self) -> Result:
        """Removes 2\-step verification password without previous password and access to recovery email address\. The password can't be reset immediately and the request needs to be repeated after the specified time


        Returns:
            :class:`~pytdbot.types.Result` (``ResetPasswordResult``)
        """

        data = {
            "@type": "resetPassword",
        }

        return await self.invoke(data)

    async def cancelPasswordReset(self) -> Result:
        """Cancels reset of 2\-step verification password\. The method can be called if passwordState\.pending\_reset\_date \> 0


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "cancelPasswordReset",
        }

        return await self.invoke(data)

    async def createTemporaryPassword(self, password: str, valid_for: int) -> Result:
        """Creates a new temporary password for processing payments

        Args:
            password (``str``):
                The 2\-step verification password of the current user

            valid_for (``int``):
                Time during which the temporary password will be valid, in seconds; must be between 60 and 86400


        Returns:
            :class:`~pytdbot.types.Result` (``TemporaryPasswordState``)
        """

        data = {
            "@type": "createTemporaryPassword",
            "password": password,
            "valid_for": valid_for,
        }

        return await self.invoke(data)

    async def getTemporaryPasswordState(self) -> Result:
        """Returns information about the current temporary password


        Returns:
            :class:`~pytdbot.types.Result` (``TemporaryPasswordState``)
        """

        data = {
            "@type": "getTemporaryPasswordState",
        }

        return await self.invoke(data)

    async def getMe(self) -> Result:
        """Returns the current user


        Returns:
            :class:`~pytdbot.types.Result` (``User``)
        """

        data = {
            "@type": "getMe",
        }

        return await self.invoke(data)

    async def getUser(self, user_id: int) -> Result:
        """Returns information about a user by their identifier\. This is an offline request if the current user is not a bot

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Result` (``User``)
        """

        data = {
            "@type": "getUser",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def getUserFullInfo(self, user_id: int) -> Result:
        """Returns full information about a user by their identifier

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Result` (``UserFullInfo``)
        """

        data = {
            "@type": "getUserFullInfo",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def getBasicGroup(self, basic_group_id: int) -> Result:
        """Returns information about a basic group by its identifier\. This is an offline request if the current user is not a bot

        Args:
            basic_group_id (``int``):
                Basic group identifier


        Returns:
            :class:`~pytdbot.types.Result` (``BasicGroup``)
        """

        data = {
            "@type": "getBasicGroup",
            "basic_group_id": basic_group_id,
        }

        return await self.invoke(data)

    async def getBasicGroupFullInfo(self, basic_group_id: int) -> Result:
        """Returns full information about a basic group by its identifier

        Args:
            basic_group_id (``int``):
                Basic group identifier


        Returns:
            :class:`~pytdbot.types.Result` (``BasicGroupFullInfo``)
        """

        data = {
            "@type": "getBasicGroupFullInfo",
            "basic_group_id": basic_group_id,
        }

        return await self.invoke(data)

    async def getSupergroup(self, supergroup_id: int) -> Result:
        """Returns information about a supergroup or a channel by its identifier\. This is an offline request if the current user is not a bot

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Supergroup``)
        """

        data = {
            "@type": "getSupergroup",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data)

    async def getSupergroupFullInfo(self, supergroup_id: int) -> Result:
        """Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier


        Returns:
            :class:`~pytdbot.types.Result` (``SupergroupFullInfo``)
        """

        data = {
            "@type": "getSupergroupFullInfo",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data)

    async def getSecretChat(self, secret_chat_id: int) -> Result:
        """Returns information about a secret chat by its identifier\. This is an offline request

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``SecretChat``)
        """

        data = {
            "@type": "getSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data)

    async def getChat(self, chat_id: int) -> Result:
        """Returns information about a chat by its identifier; this is an offline request if the current user is not a bot

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "getChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getMessage(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a message

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the message to get


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getMessageLocally(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a message, if it is available without sending network request\. This is an offline request

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the message to get


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getMessageLocally",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getRepliedMessage(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a non\-bundled message that is replied by a given message\. Also, returns the pinned message, the game message, the invoice message, the message with a previously set same background, and the topic creation message for messages of the types messagePinMessage, messageGameScore, messagePaymentSuccessful, messageChatSetBackground and topic messages without non\-bundled replied message respectively

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the reply message


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getRepliedMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getChatPinnedMessage(self, chat_id: int) -> Result:
        """Returns information about a newest pinned message in the chat

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getChatPinnedMessage",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getCallbackQueryMessage(
        self, chat_id: int, message_id: int, callback_query_id: int
    ) -> Result:
        """Returns information about a message with the callback button that originated a callback query; for bots only

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Message identifier

            callback_query_id (``int``):
                Identifier of the callback query


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getCallbackQueryMessage",
            "chat_id": chat_id,
            "message_id": message_id,
            "callback_query_id": callback_query_id,
        }

        return await self.invoke(data)

    async def getMessages(self, chat_id: int, message_ids: list) -> Result:
        """Returns information about messages\. If a message is not found, returns null on the corresponding position of the result

        Args:
            chat_id (``int``):
                Identifier of the chat the messages belong to

            message_ids (``list``):
                Identifiers of the messages to get


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "getMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
        }

        return await self.invoke(data)

    async def getMessageThread(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a message thread\. Can be used only if message\.can\_get\_message\_thread \=\= true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Result` (``MessageThreadInfo``)
        """

        data = {
            "@type": "getMessageThread",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getMessageViewers(self, chat_id: int, message_id: int) -> Result:
        """Returns viewers of a recent outgoing message in a basic group or a supergroup chat\. For video notes and voice notes only users, opened content of the message, are returned\. The method can be called if message\.can\_get\_viewers \=\= true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Result` (``MessageViewers``)
        """

        data = {
            "@type": "getMessageViewers",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getFile(self, file_id: int) -> Result:
        """Returns information about a file; this is an offline request

        Args:
            file_id (``int``):
                Identifier of the file to get


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "getFile",
            "file_id": file_id,
        }

        return await self.invoke(data)

    async def getRemoteFile(
        self, remote_file_id: str, file_type: dict = None
    ) -> Result:
        """Returns information about a file by its remote identifier; this is an offline request\. Can be used to register a URL as a file for further uploading, or sending as a message\. Even the request succeeds, the file can be used only if it is still accessible to the user\. For example, if the file is from a message, then the message must be not deleted and accessible to the user\. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

        Args:
            remote_file_id (``str``):
                Remote identifier of the file to get

            file_type (``FileType``, *optional*):
                File type; pass null if unknown


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "getRemoteFile",
            "remote_file_id": remote_file_id,
            "file_type": file_type,
        }

        return await self.invoke(data)

    async def loadChats(self, limit: int, chat_list: dict = None) -> Result:
        """Loads more chats from a chat list\. The loaded chats and their positions in the chat list will be sent through updates\. Chats are sorted by the pair \(chat\.position\.order, chat\.id\) in descending order\. Returns a 404 error if all chats have been loaded

        Args:
            limit (``int``):
                The maximum number of chats to be loaded\. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached

            chat_list (``ChatList``, *optional*):
                The chat list in which to load chats; pass null to load chats from the main chat list


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "loadChats",
            "chat_list": chat_list,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getChats(self, limit: int, chat_list: dict = None) -> Result:
        """Returns an ordered list of chats from the beginning of a chat list\. For informational purposes only\. Use loadChats and updates processing instead to maintain chat lists in a consistent state

        Args:
            limit (``int``):
                The maximum number of chats to be returned

            chat_list (``ChatList``, *optional*):
                The chat list in which to return chats; pass null to get chats from the main chat list


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChats",
            "chat_list": chat_list,
            "limit": limit,
        }

        return await self.invoke(data)

    async def searchPublicChat(self, username: str) -> Result:
        """Searches a public chat by its username\. Currently, only private chats, supergroups and channels can be public\. Returns the chat if found; otherwise, an error is returned

        Args:
            username (``str``):
                Username to be resolved


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "searchPublicChat",
            "username": username,
        }

        return await self.invoke(data)

    async def searchPublicChats(self, query: str) -> Result:
        """Searches public chats by looking for specified query in their username and title\. Currently, only private chats, supergroups and channels can be public\. Returns a meaningful number of results\. Excludes private chats with contacts and chats from the chat list from the results

        Args:
            query (``str``):
                Query to search for


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "searchPublicChats",
            "query": query,
        }

        return await self.invoke(data)

    async def searchChats(self, query: str, limit: int) -> Result:
        """Searches for the specified query in the title and username of already known chats; this is an offline request\. Returns chats in the order seen in the main chat list

        Args:
            query (``str``):
                Query to search for\. If the query is empty, returns up to 50 recently found chats

            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "searchChats",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def searchChatsOnServer(self, query: str, limit: int) -> Result:
        """Searches for the specified query in the title and username of already known chats via request to the server\. Returns chats in the order seen in the main chat list

        Args:
            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "searchChatsOnServer",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def searchChatsNearby(self, location: dict) -> Result:
        """Returns a list of users and location\-based supergroups nearby\. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby\. The request must be sent again every 25 seconds with adjusted location to not miss new chats

        Args:
            location (``location``):
                Current user location


        Returns:
            :class:`~pytdbot.types.Result` (``ChatsNearby``)
        """

        data = {
            "@type": "searchChatsNearby",
            "location": location,
        }

        return await self.invoke(data)

    async def getChatSimilarChats(self, chat_id: int) -> Result:
        """Returns a list of chats similar to the given chat

        Args:
            chat_id (``int``):
                Identifier of the target chat; must be an identifier of a channel chat


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatSimilarChats",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatSimilarChatCount(self, chat_id: int, return_local: bool) -> Result:
        """Returns approximate number of chats similar to the given chat

        Args:
            chat_id (``int``):
                Identifier of the target chat; must be an identifier of a channel chat

            return_local (``bool``):
                Pass true to get the number of chats without sending network requests, or \-1 if the number of chats is unknown locally


        Returns:
            :class:`~pytdbot.types.Result` (``Count``)
        """

        data = {
            "@type": "getChatSimilarChatCount",
            "chat_id": chat_id,
            "return_local": return_local,
        }

        return await self.invoke(data)

    async def getTopChats(self, category: dict, limit: int) -> Result:
        """Returns a list of frequently used chats

        Args:
            category (``TopChatCategory``):
                Category of chats to be returned

            limit (``int``):
                The maximum number of chats to be returned; up to 30


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getTopChats",
            "category": category,
            "limit": limit,
        }

        return await self.invoke(data)

    async def removeTopChat(self, category: dict, chat_id: int) -> Result:
        """Removes a chat from the list of frequently used chats\. Supported only if the chat info database is enabled

        Args:
            category (``TopChatCategory``):
                Category of frequently used chats

            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeTopChat",
            "category": category,
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def searchRecentlyFoundChats(self, query: str, limit: int) -> Result:
        """Searches for the specified query in the title and username of up to 50 recently found chats; this is an offline request

        Args:
            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "searchRecentlyFoundChats",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def addRecentlyFoundChat(self, chat_id: int) -> Result:
        """Adds a chat to the list of recently found chats\. The chat is added to the beginning of the list\. If the chat is already in the list, it will be removed from the list first

        Args:
            chat_id (``int``):
                Identifier of the chat to add


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addRecentlyFoundChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def removeRecentlyFoundChat(self, chat_id: int) -> Result:
        """Removes a chat from the list of recently found chats

        Args:
            chat_id (``int``):
                Identifier of the chat to be removed


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeRecentlyFoundChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def clearRecentlyFoundChats(self) -> Result:
        """Clears the list of recently found chats


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearRecentlyFoundChats",
        }

        return await self.invoke(data)

    async def getRecentlyOpenedChats(self, limit: int) -> Result:
        """Returns recently opened chats; this is an offline request\. Returns chats in the order of last opening

        Args:
            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getRecentlyOpenedChats",
            "limit": limit,
        }

        return await self.invoke(data)

    async def checkChatUsername(self, chat_id: int, username: str) -> Result:
        """Checks whether a username can be set for a chat

        Args:
            chat_id (``int``):
                Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created

            username (``str``):
                Username to be checked


        Returns:
            :class:`~pytdbot.types.Result` (``CheckChatUsernameResult``)
        """

        data = {
            "@type": "checkChatUsername",
            "chat_id": chat_id,
            "username": username,
        }

        return await self.invoke(data)

    async def getCreatedPublicChats(self, type: dict) -> Result:
        """Returns a list of public chats of the specified type, owned by the user

        Args:
            type (``PublicChatType``):
                Type of the public chats to return


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getCreatedPublicChats",
            "type": type,
        }

        return await self.invoke(data)

    async def checkCreatedPublicChatsLimit(self, type: dict) -> Result:
        """Checks whether the maximum number of owned public chats has been reached\. Returns corresponding error if the limit was reached\. The limit can be increased with Telegram Premium

        Args:
            type (``PublicChatType``):
                Type of the public chats, for which to check the limit


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkCreatedPublicChatsLimit",
            "type": type,
        }

        return await self.invoke(data)

    async def getSuitableDiscussionChats(self) -> Result:
        """Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel\. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group\. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getSuitableDiscussionChats",
        }

        return await self.invoke(data)

    async def getInactiveSupergroupChats(self) -> Result:
        """Returns a list of recently inactive supergroups and channels\. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS\_TOO\_MUCH error\. Also, the limit can be increased with Telegram Premium


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getInactiveSupergroupChats",
        }

        return await self.invoke(data)

    async def getGroupsInCommon(
        self, user_id: int, offset_chat_id: int, limit: int
    ) -> Result:
        """Returns a list of common group chats with a given user\. Chats are sorted by their type and creation date

        Args:
            user_id (``int``):
                User identifier

            offset_chat_id (``int``):
                Chat identifier starting from which to return chats; use 0 for the first request

            limit (``int``):
                The maximum number of chats to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getGroupsInCommon",
            "user_id": user_id,
            "offset_chat_id": offset_chat_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getChatHistory(
        self,
        chat_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        only_local: bool,
    ) -> Result:
        """Returns messages in a chat\. The messages are returned in a reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib\. This is an offline request if only\_local is true

        Args:
            chat_id (``int``):
                Chat identifier

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from\_message\_id or a negative offset up to 99 to get additionally some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than or equal to \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_local (``bool``):
                Pass true to get only messages that are available without sending network requests


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "getChatHistory",
            "chat_id": chat_id,
            "from_message_id": from_message_id,
            "offset": offset,
            "limit": limit,
            "only_local": only_local,
        }

        return await self.invoke(data)

    async def getMessageThreadHistory(
        self,
        chat_id: int,
        message_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
    ) -> Result:
        """Returns messages in a message thread of a message\. Can be used only if message\.can\_get\_message\_thread \=\= true\. Message thread of a channel message is in the channel's linked supergroup\. The messages are returned in a reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier, which thread history needs to be returned

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from\_message\_id or a negative offset up to 99 to get additionally some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than or equal to \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "getMessageThreadHistory",
            "chat_id": chat_id,
            "message_id": message_id,
            "from_message_id": from_message_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def deleteChatHistory(
        self, chat_id: int, remove_from_chat_list: bool, revoke: bool
    ) -> Result:
        """Deletes all messages in the chat\. Use chat\.can\_be\_deleted\_only\_for\_self and chat\.can\_be\_deleted\_for\_all\_users fields to find whether and how the method can be applied to the chat

        Args:
            chat_id (``int``):
                Chat identifier

            remove_from_chat_list (``bool``):
                Pass true to remove the chat from all chat lists

            revoke (``bool``):
                Pass true to delete chat history for all users


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatHistory",
            "chat_id": chat_id,
            "remove_from_chat_list": remove_from_chat_list,
            "revoke": revoke,
        }

        return await self.invoke(data)

    async def deleteChat(self, chat_id: int) -> Result:
        """Deletes a chat along with all messages in the corresponding chat for all chat members\. For group chats this will release the usernames and remove all members\. Use the field chat\.can\_be\_deleted\_for\_all\_users to find whether the method can be applied to the chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def searchChatMessages(
        self,
        chat_id: int,
        query: str,
        from_message_id: int,
        offset: int,
        limit: int,
        message_thread_id: int,
        sender_id: dict = None,
        filter: dict = None,
    ) -> Result:
        """Searches for messages with given words in the chat\. Returns the results in reverse chronological order, i\.e\. in order of decreasing message\_id\. Cannot be used in secret chats with a non\-empty query \(searchSecretMessages must be used instead\), or without an enabled message database\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit\. A combination of query, sender\_id, filter and message\_thread\_id search criteria is expected to be supported, only if it is required for Telegram official application implementation

        Args:
            chat_id (``int``):
                Identifier of the chat in which to search messages

            query (``str``):
                Query to search for

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from\_message\_id or a negative offset to get the specified message and some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. If the offset is negative, the limit must be greater than \-offset\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            message_thread_id (``int``):
                If not 0, only messages in the specified thread will be returned; supergroups only

            sender_id (``MessageSender``, *optional*):
                Identifier of the sender of messages to search for; pass null to search for messages from any sender\. Not supported in secret chats

            filter (``SearchMessagesFilter``, *optional*):
                Additional filter for messages to search; pass null to search for all messages


        Returns:
            :class:`~pytdbot.types.Result` (``FoundChatMessages``)
        """

        data = {
            "@type": "searchChatMessages",
            "chat_id": chat_id,
            "query": query,
            "sender_id": sender_id,
            "from_message_id": from_message_id,
            "offset": offset,
            "limit": limit,
            "filter": filter,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def searchMessages(
        self,
        query: str,
        offset: str,
        limit: int,
        min_date: int,
        max_date: int,
        chat_list: dict = None,
        filter: dict = None,
    ) -> Result:
        """Searches for messages in all chats except secret chats\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing \(date, chat\_id, message\_id\)\)\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Args:
            query (``str``):
                Query to search for

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            min_date (``int``):
                If not 0, the minimum date of the messages to return

            max_date (``int``):
                If not 0, the maximum date of the messages to return

            chat_list (``ChatList``, *optional*):
                Chat list in which to search messages; pass null to search in all chats regardless of their chat list\. Only Main and Archive chat lists are supported

            filter (``SearchMessagesFilter``, *optional*):
                Additional filter for messages to search; pass null to search for all messages\. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function


        Returns:
            :class:`~pytdbot.types.Result` (``FoundMessages``)
        """

        data = {
            "@type": "searchMessages",
            "chat_list": chat_list,
            "query": query,
            "offset": offset,
            "limit": limit,
            "filter": filter,
            "min_date": min_date,
            "max_date": max_date,
        }

        return await self.invoke(data)

    async def searchSecretMessages(
        self, chat_id: int, query: str, offset: str, limit: int, filter: dict = None
    ) -> Result:
        """Searches for messages in secret chats\. Returns the results in reverse chronological order\. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Identifier of the chat in which to search\. Specify 0 to search in all secret chats

            query (``str``):
                Query to search for\. If empty, searchChatMessages must be used instead

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            filter (``SearchMessagesFilter``, *optional*):
                Additional filter for messages to search; pass null to search for all messages


        Returns:
            :class:`~pytdbot.types.Result` (``FoundMessages``)
        """

        data = {
            "@type": "searchSecretMessages",
            "chat_id": chat_id,
            "query": query,
            "offset": offset,
            "limit": limit,
            "filter": filter,
        }

        return await self.invoke(data)

    async def searchCallMessages(
        self, offset: str, limit: int, only_missed: bool
    ) -> Result:
        """Searches for call messages\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; up to 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_missed (``bool``):
                Pass true to search only for messages with missed/declined calls


        Returns:
            :class:`~pytdbot.types.Result` (``FoundMessages``)
        """

        data = {
            "@type": "searchCallMessages",
            "offset": offset,
            "limit": limit,
            "only_missed": only_missed,
        }

        return await self.invoke(data)

    async def searchOutgoingDocumentMessages(self, query: str, limit: int) -> Result:
        """Searches for outgoing messages with content of the type messageDocument in all chats except secret chats\. Returns the results in reverse chronological order

        Args:
            query (``str``):
                Query to search for in document file name and message caption

            limit (``int``):
                The maximum number of messages to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``FoundMessages``)
        """

        data = {
            "@type": "searchOutgoingDocumentMessages",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def deleteAllCallMessages(self, revoke: bool) -> Result:
        """Deletes all call messages

        Args:
            revoke (``bool``):
                Pass true to delete the messages for all users


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteAllCallMessages",
            "revoke": revoke,
        }

        return await self.invoke(data)

    async def searchChatRecentLocationMessages(
        self, chat_id: int, limit: int
    ) -> Result:
        """Returns information about the recent locations of chat members that were sent to the chat\. Returns up to 1 location message per user

        Args:
            chat_id (``int``):
                Chat identifier

            limit (``int``):
                The maximum number of messages to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "searchChatRecentLocationMessages",
            "chat_id": chat_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getActiveLiveLocationMessages(self) -> Result:
        """Returns all active live locations that need to be updated by the application\. The list is persistent across application restarts only if the message database is used


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "getActiveLiveLocationMessages",
        }

        return await self.invoke(data)

    async def getChatMessageByDate(self, chat_id: int, date: int) -> Result:
        """Returns the last message sent in a chat no later than the specified date

        Args:
            chat_id (``int``):
                Chat identifier

            date (``int``):
                Point in time \(Unix timestamp\) relative to which to search for messages


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "getChatMessageByDate",
            "chat_id": chat_id,
            "date": date,
        }

        return await self.invoke(data)

    async def getChatSparseMessagePositions(
        self, chat_id: int, filter: dict, from_message_id: int, limit: int
    ) -> Result:
        """Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation\. Returns the results in reverse chronological order \(i\.e\., in order of decreasing message\_id\)\. Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

        Args:
            chat_id (``int``):
                Identifier of the chat in which to return information about message positions

            filter (``SearchMessagesFilter``):
                Filter for message content\. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (``int``):
                The message identifier from which to return information about message positions

            limit (``int``):
                The expected number of message positions to be returned; 50\-2000\. A smaller number of positions can be returned, if there are not enough appropriate messages


        Returns:
            :class:`~pytdbot.types.Result` (``MessagePositions``)
        """

        data = {
            "@type": "getChatSparseMessagePositions",
            "chat_id": chat_id,
            "filter": filter,
            "from_message_id": from_message_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getChatMessageCalendar(
        self, chat_id: int, filter: dict, from_message_id: int
    ) -> Result:
        """Returns information about the next messages of the specified type in the chat split by days\. Returns the results in reverse chronological order\. Can return partial result for the last returned day\. Behavior of this method depends on the value of the option "utc\_time\_offset"

        Args:
            chat_id (``int``):
                Identifier of the chat in which to return information about messages

            filter (``SearchMessagesFilter``):
                Filter for message content\. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (``int``):
                The message identifier from which to return information about messages; use 0 to get results from the last message


        Returns:
            :class:`~pytdbot.types.Result` (``MessageCalendar``)
        """

        data = {
            "@type": "getChatMessageCalendar",
            "chat_id": chat_id,
            "filter": filter,
            "from_message_id": from_message_id,
        }

        return await self.invoke(data)

    async def getChatMessageCount(
        self, chat_id: int, filter: dict, return_local: bool
    ) -> Result:
        """Returns approximate number of messages of the specified type in the chat

        Args:
            chat_id (``int``):
                Identifier of the chat in which to count messages

            filter (``SearchMessagesFilter``):
                Filter for message content; searchMessagesFilterEmpty is unsupported in this function

            return_local (``bool``):
                Pass true to get the number of messages without sending network requests, or \-1 if the number of messages is unknown locally


        Returns:
            :class:`~pytdbot.types.Result` (``Count``)
        """

        data = {
            "@type": "getChatMessageCount",
            "chat_id": chat_id,
            "filter": filter,
            "return_local": return_local,
        }

        return await self.invoke(data)

    async def getChatMessagePosition(
        self, chat_id: int, message_id: int, filter: dict, message_thread_id: int
    ) -> Result:
        """Returns approximate 1\-based position of a message among messages, which can be found by the specified filter in the chat\. Cannot be used in secret chats

        Args:
            chat_id (``int``):
                Identifier of the chat in which to find message position

            message_id (``int``):
                Message identifier

            filter (``SearchMessagesFilter``):
                Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function

            message_thread_id (``int``):
                If not 0, only messages in the specified thread will be considered; supergroups only


        Returns:
            :class:`~pytdbot.types.Result` (``Count``)
        """

        data = {
            "@type": "getChatMessagePosition",
            "chat_id": chat_id,
            "message_id": message_id,
            "filter": filter,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def getChatScheduledMessages(self, chat_id: int) -> Result:
        """Returns all scheduled messages in a chat\. The messages are returned in a reverse chronological order \(i\.e\., in order of decreasing message\_id\)

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "getChatScheduledMessages",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatSponsoredMessages(self, chat_id: int) -> Result:
        """Returns sponsored messages to be shown in a chat; for channel chats only

        Args:
            chat_id (``int``):
                Identifier of the chat


        Returns:
            :class:`~pytdbot.types.Result` (``SponsoredMessages``)
        """

        data = {
            "@type": "getChatSponsoredMessages",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def clickChatSponsoredMessage(self, chat_id: int, message_id: int) -> Result:
        """Informs TDLib that the user opened the sponsored chat via the button, the name, the photo, or a mention in the sponsored message

        Args:
            chat_id (``int``):
                Chat identifier of the sponsored message

            message_id (``int``):
                Identifier of the sponsored message


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clickChatSponsoredMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def removeNotification(
        self, notification_group_id: int, notification_id: int
    ) -> Result:
        """Removes an active notification from notification list\. Needs to be called only if the notification is removed by the current user

        Args:
            notification_group_id (``int``):
                Identifier of notification group to which the notification belongs

            notification_id (``int``):
                Identifier of removed notification


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeNotification",
            "notification_group_id": notification_group_id,
            "notification_id": notification_id,
        }

        return await self.invoke(data)

    async def removeNotificationGroup(
        self, notification_group_id: int, max_notification_id: int
    ) -> Result:
        """Removes a group of active notifications\. Needs to be called only if the notification group is removed by the current user

        Args:
            notification_group_id (``int``):
                Notification group identifier

            max_notification_id (``int``):
                The maximum identifier of removed notifications


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeNotificationGroup",
            "notification_group_id": notification_group_id,
            "max_notification_id": max_notification_id,
        }

        return await self.invoke(data)

    async def getMessageLink(
        self,
        chat_id: int,
        message_id: int,
        media_timestamp: int,
        for_album: bool,
        in_message_thread: bool,
    ) -> Result:
        """Returns an HTTPS link to a message in a chat\. Available only for already sent messages in supergroups and channels, or if message\.can\_get\_media\_timestamp\_links and a media timestamp link is generated\. This is an offline request

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            media_timestamp (``int``):
                If not 0, timestamp from which the video/audio/video note/voice note/story playing must start, in seconds\. The media can be in the message content or in its web page preview

            for_album (``bool``):
                Pass true to create a link for the whole media album

            in_message_thread (``bool``):
                Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic


        Returns:
            :class:`~pytdbot.types.Result` (``MessageLink``)
        """

        data = {
            "@type": "getMessageLink",
            "chat_id": chat_id,
            "message_id": message_id,
            "media_timestamp": media_timestamp,
            "for_album": for_album,
            "in_message_thread": in_message_thread,
        }

        return await self.invoke(data)

    async def getMessageEmbeddingCode(
        self, chat_id: int, message_id: int, for_album: bool
    ) -> Result:
        """Returns an HTML code for embedding the message\. Available only for messages in supergroups and channels with a username

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            for_album (``bool``):
                Pass true to return an HTML code for embedding of the whole media album


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getMessageEmbeddingCode",
            "chat_id": chat_id,
            "message_id": message_id,
            "for_album": for_album,
        }

        return await self.invoke(data)

    async def getMessageLinkInfo(self, url: str) -> Result:
        """Returns information about a public or private message link\. Can be called for any internal link of the type internalLinkTypeMessage

        Args:
            url (``str``):
                The message link


        Returns:
            :class:`~pytdbot.types.Result` (``MessageLinkInfo``)
        """

        data = {
            "@type": "getMessageLinkInfo",
            "url": url,
        }

        return await self.invoke(data)

    async def translateText(self, text: dict, to_language_code: str) -> Result:
        """Translates a text to the given language\. If the current user is a Telegram Premium user, then text formatting is preserved

        Args:
            text (``formattedText``):
                Text to translate

            to_language_code (``str``):
                Language code of the language to which the message is translated\. Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh\-CN", "zh", "zh\-Hans", "zh\-TW", "zh\-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"


        Returns:
            :class:`~pytdbot.types.Result` (``FormattedText``)
        """

        data = {
            "@type": "translateText",
            "text": text,
            "to_language_code": to_language_code,
        }

        return await self.invoke(data)

    async def translateMessageText(
        self, chat_id: int, message_id: int, to_language_code: str
    ) -> Result:
        """Extracts text or caption of the given message and translates it to the given language\. If the current user is a Telegram Premium user, then text formatting is preserved

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            to_language_code (``str``):
                Language code of the language to which the message is translated\. Must be one of "af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh\-CN", "zh", "zh\-Hans", "zh\-TW", "zh\-Hant", "co", "hr", "cs", "da", "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "iw", "hi", "hmn", "hu", "is", "ig", "id", "in", "ga", "it", "ja", "jv", "kn", "kk", "km", "rw", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml", "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st", "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tl", "tg", "ta", "tt", "te", "th", "tr", "tk", "uk", "ur", "ug", "uz", "vi", "cy", "xh", "yi", "ji", "yo", "zu"


        Returns:
            :class:`~pytdbot.types.Result` (``FormattedText``)
        """

        data = {
            "@type": "translateMessageText",
            "chat_id": chat_id,
            "message_id": message_id,
            "to_language_code": to_language_code,
        }

        return await self.invoke(data)

    async def recognizeSpeech(self, chat_id: int, message_id: int) -> Result:
        """Recognizes speech in a video note or a voice note message\. The message must be successfully sent, must not be scheduled, and must be from a non\-secret chat

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "recognizeSpeech",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def rateSpeechRecognition(
        self, chat_id: int, message_id: int, is_good: bool
    ) -> Result:
        """Rates recognized speech in a video note or a voice note message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            is_good (``bool``):
                Pass true if the speech recognition is good


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "rateSpeechRecognition",
            "chat_id": chat_id,
            "message_id": message_id,
            "is_good": is_good,
        }

        return await self.invoke(data)

    async def getChatAvailableMessageSenders(self, chat_id: int) -> Result:
        """Returns list of message sender identifiers, which can be used to send messages in a chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatMessageSenders``)
        """

        data = {
            "@type": "getChatAvailableMessageSenders",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def setChatMessageSender(
        self, chat_id: int, message_sender_id: dict
    ) -> Result:
        """Selects a message sender to send messages in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_sender_id (``MessageSender``):
                New message sender for the chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatMessageSender",
            "chat_id": chat_id,
            "message_sender_id": message_sender_id,
        }

        return await self.invoke(data)

    async def sendMessage(
        self,
        chat_id: int,
        message_thread_id: int,
        input_message_content: dict,
        reply_to: dict = None,
        options: dict = None,
        reply_markup: dict = None,
    ) -> Result:
        """Sends a message\. Returns the sent message

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent

            input_message_content (``InputMessageContent``):
                The content of the message to be sent

            reply_to (``InputMessageReplyTo``, *optional*):
                Information about the message or story to be replied; pass null if none

            options (``messageSendOptions``, *optional*):
                Options to be used to send the message; pass null to use default options

            reply_markup (``ReplyMarkup``, *optional*):
                Markup for replying to the message; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to": reply_to,
            "options": options,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def sendMessageAlbum(
        self,
        chat_id: int,
        message_thread_id: int,
        input_message_contents: list,
        reply_to: dict = None,
        options: dict = None,
    ) -> Result:
        """Sends 2\-10 messages grouped together into an album\. Currently, only audio, document, photo and video messages can be grouped into an album\. Documents and audio files can be only grouped in an album with messages of the same type\. Returns sent messages

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the messages will be sent

            input_message_contents (``list``):
                Contents of messages to be sent\. At most 10 messages can be added to an album

            reply_to (``InputMessageReplyTo``, *optional*):
                Information about the message or story to be replied; pass null if none

            options (``messageSendOptions``, *optional*):
                Options to be used to send the messages; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "sendMessageAlbum",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to": reply_to,
            "options": options,
            "input_message_contents": input_message_contents,
        }

        return await self.invoke(data)

    async def sendBotStartMessage(
        self, bot_user_id: int, chat_id: int, parameter: str
    ) -> Result:
        """Invites a bot to a chat \(if it is not yet a member\) and sends it the /start command\. Bots can't be invited to a private chat other than the chat with the bot\. Bots can't be invited to channels \(although they can be added as admins\) and secret chats\. Returns the sent message

        Args:
            bot_user_id (``int``):
                Identifier of the bot

            chat_id (``int``):
                Identifier of the target chat

            parameter (``str``):
                A hidden parameter sent to the bot for deep linking purposes \(https://core\.telegram\.org/bots\#deep\-linking\)


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "sendBotStartMessage",
            "bot_user_id": bot_user_id,
            "chat_id": chat_id,
            "parameter": parameter,
        }

        return await self.invoke(data)

    async def sendInlineQueryResultMessage(
        self,
        chat_id: int,
        message_thread_id: int,
        query_id: int,
        result_id: str,
        hide_via_bot: bool,
        reply_to: dict = None,
        options: dict = None,
    ) -> Result:
        """Sends the result of an inline query as a message\. Returns the sent message\. Always clears a chat draft message

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent

            query_id (``int``):
                Identifier of the inline query

            result_id (``str``):
                Identifier of the inline query result

            hide_via_bot (``bool``):
                Pass true to hide the bot, via which the message is sent\. Can be used only for bots getOption\("animation\_search\_bot\_username"\), getOption\("photo\_search\_bot\_username"\), and getOption\("venue\_search\_bot\_username"\)

            reply_to (``InputMessageReplyTo``, *optional*):
                Information about the message or story to be replied; pass null if none

            options (``messageSendOptions``, *optional*):
                Options to be used to send the message; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "sendInlineQueryResultMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to": reply_to,
            "options": options,
            "query_id": query_id,
            "result_id": result_id,
            "hide_via_bot": hide_via_bot,
        }

        return await self.invoke(data)

    async def forwardMessages(
        self,
        chat_id: int,
        message_thread_id: int,
        from_chat_id: int,
        message_ids: list,
        send_copy: bool,
        remove_caption: bool,
        options: dict = None,
    ) -> Result:
        """Forwards previously sent messages\. Returns the forwarded messages in the same order as the message identifiers passed in message\_ids\. If a message can't be forwarded, null will be returned instead of the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which to forward messages

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent; for forum threads only

            from_chat_id (``int``):
                Identifier of the chat from which to forward messages

            message_ids (``list``):
                Identifiers of the messages to forward\. Message identifiers must be in a strictly increasing order\. At most 100 messages can be forwarded simultaneously\. A message can be forwarded only if message\.can\_be\_forwarded

            send_copy (``bool``):
                Pass true to copy content of the messages without reference to the original sender\. Always true if the messages are forwarded to a secret chat or are local

            remove_caption (``bool``):
                Pass true to remove media captions of message copies\. Ignored if send\_copy is false

            options (``messageSendOptions``, *optional*):
                Options to be used to send the messages; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "forwardMessages",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "options": options,
            "send_copy": send_copy,
            "remove_caption": remove_caption,
        }

        return await self.invoke(data)

    async def resendMessages(
        self, chat_id: int, message_ids: list, quote: dict = None
    ) -> Result:
        """Resends messages which failed to send\. Can be called only for messages for which messageSendingStateFailed\.can\_retry is true and after specified in messageSendingStateFailed\.retry\_after time passed\. If a message is re\-sent, the corresponding failed to send message is deleted\. Returns the sent messages in the same order as the message identifiers passed in message\_ids\. If a message can't be re\-sent, null will be returned instead of the message

        Args:
            chat_id (``int``):
                Identifier of the chat to send messages

            message_ids (``list``):
                Identifiers of the messages to resend\. Message identifiers must be in a strictly increasing order

            quote (``inputTextQuote``, *optional*):
                New manually chosen quote from the message to be replied; pass null if none\. Ignored if more than one message is re\-sent, or if messageSendingStateFailed\.need\_another\_reply\_quote \=\= false


        Returns:
            :class:`~pytdbot.types.Result` (``Messages``)
        """

        data = {
            "@type": "resendMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "quote": quote,
        }

        return await self.invoke(data)

    async def addLocalMessage(
        self,
        chat_id: int,
        sender_id: dict,
        disable_notification: bool,
        input_message_content: dict,
        reply_to: dict = None,
    ) -> Result:
        """Adds a local message to a chat\. The message is persistent across application restarts only if the message database is used\. Returns the added message

        Args:
            chat_id (``int``):
                Target chat

            sender_id (``MessageSender``):
                Identifier of the sender of the message

            disable_notification (``bool``):
                Pass true to disable notification for the message

            input_message_content (``InputMessageContent``):
                The content of the message to be added

            reply_to (``InputMessageReplyTo``, *optional*):
                Information about the message or story to be replied; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "addLocalMessage",
            "chat_id": chat_id,
            "sender_id": sender_id,
            "reply_to": reply_to,
            "disable_notification": disable_notification,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def deleteMessages(
        self, chat_id: int, message_ids: list, revoke: bool
    ) -> Result:
        """Deletes messages

        Args:
            chat_id (``int``):
                Chat identifier

            message_ids (``list``):
                Identifiers of the messages to be deleted

            revoke (``bool``):
                Pass true to delete messages for all chat members\. Always true for supergroups, channels and secret chats


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "revoke": revoke,
        }

        return await self.invoke(data)

    async def deleteChatMessagesBySender(self, chat_id: int, sender_id: dict) -> Result:
        """Deletes all messages sent by the specified message sender in a chat\. Supported only for supergroups; requires can\_delete\_messages administrator privileges

        Args:
            chat_id (``int``):
                Chat identifier

            sender_id (``MessageSender``):
                Identifier of the sender of messages to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatMessagesBySender",
            "chat_id": chat_id,
            "sender_id": sender_id,
        }

        return await self.invoke(data)

    async def deleteChatMessagesByDate(
        self, chat_id: int, min_date: int, max_date: int, revoke: bool
    ) -> Result:
        """Deletes all messages between the specified dates in a chat\. Supported only for private chats and basic groups\. Messages sent in the last 30 seconds will not be deleted

        Args:
            chat_id (``int``):
                Chat identifier

            min_date (``int``):
                The minimum date of the messages to delete

            max_date (``int``):
                The maximum date of the messages to delete

            revoke (``bool``):
                Pass true to delete chat messages for all users; private chats only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatMessagesByDate",
            "chat_id": chat_id,
            "min_date": min_date,
            "max_date": max_date,
            "revoke": revoke,
        }

        return await self.invoke(data)

    async def editMessageText(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: dict,
        reply_markup: dict = None,
    ) -> Result:
        """Edits the text of a message \(or a text of a game message\)\. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            input_message_content (``InputMessageContent``):
                New text content of the message\. Must be of type inputMessageText

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "editMessageText",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def editMessageLiveLocation(
        self,
        chat_id: int,
        message_id: int,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: dict = None,
        location: dict = None,
    ) -> Result:
        """Edits the message content of a live location\. Messages can be edited for a limited period of time specified in the live location\. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            heading (``int``):
                The new direction in which the location moves, in degrees; 1\-360\. Pass 0 if unknown

            proximity_alert_radius (``int``):
                The new maximum distance for proximity alerts, in meters \(0\-100000\)\. Pass 0 if the notification is disabled

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only

            location (``location``, *optional*):
                New location content of the message; pass null to stop sharing the live location


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "editMessageLiveLocation",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "location": location,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
        }

        return await self.invoke(data)

    async def editMessageMedia(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: dict,
        reply_markup: dict = None,
    ) -> Result:
        """Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption\. If only the caption needs to be edited, use editMessageCaption instead\. The media can't be edited if the message was set to self\-destruct or to a self\-destructing media\. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa\. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            input_message_content (``InputMessageContent``):
                New content of the message\. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "editMessageMedia",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def editMessageCaption(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: dict = None,
        caption: dict = None,
    ) -> Result:
        """Edits the message content caption\. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only

            caption (``formattedText``, *optional*):
                New message content caption; 0\-getOption\("message\_caption\_length\_max"\) characters; pass null to remove caption


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "editMessageCaption",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "caption": caption,
        }

        return await self.invoke(data)

    async def editMessageReplyMarkup(
        self, chat_id: int, message_id: int, reply_markup: dict = None
    ) -> Result:
        """Edits the message reply markup; for bots only\. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "editMessageReplyMarkup",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data)

    async def editInlineMessageText(
        self,
        inline_message_id: str,
        input_message_content: dict,
        reply_markup: dict = None,
    ) -> Result:
        """Edits the text of an inline text or game message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            input_message_content (``InputMessageContent``):
                New text content of the message\. Must be of type inputMessageText

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editInlineMessageText",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def editInlineMessageLiveLocation(
        self,
        inline_message_id: str,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: dict = None,
        location: dict = None,
    ) -> Result:
        """Edits the content of a live location in an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            heading (``int``):
                The new direction in which the location moves, in degrees; 1\-360\. Pass 0 if unknown

            proximity_alert_radius (``int``):
                The new maximum distance for proximity alerts, in meters \(0\-100000\)\. Pass 0 if the notification is disabled

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none

            location (``location``, *optional*):
                New location content of the message; pass null to stop sharing the live location


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editInlineMessageLiveLocation",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "location": location,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
        }

        return await self.invoke(data)

    async def editInlineMessageMedia(
        self,
        inline_message_id: str,
        input_message_content: dict,
        reply_markup: dict = None,
    ) -> Result:
        """Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            input_message_content (``InputMessageContent``):
                New content of the message\. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editInlineMessageMedia",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data)

    async def editInlineMessageCaption(
        self, inline_message_id: str, reply_markup: dict = None, caption: dict = None
    ) -> Result:
        """Edits the caption of an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none

            caption (``formattedText``, *optional*):
                New message content caption; pass null to remove caption; 0\-getOption\("message\_caption\_length\_max"\) characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editInlineMessageCaption",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "caption": caption,
        }

        return await self.invoke(data)

    async def editInlineMessageReplyMarkup(
        self, inline_message_id: str, reply_markup: dict = None
    ) -> Result:
        """Edits the reply markup of an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editInlineMessageReplyMarkup",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data)

    async def editMessageSchedulingState(
        self, chat_id: int, message_id: int, scheduling_state: dict = None
    ) -> Result:
        """Edits the time when a scheduled message will be sent\. Scheduling state of all messages in the same album or forwarded together with the message will be also changed

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            scheduling_state (``MessageSchedulingState``, *optional*):
                The new message scheduling state; pass null to send the message immediately


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editMessageSchedulingState",
            "chat_id": chat_id,
            "message_id": message_id,
            "scheduling_state": scheduling_state,
        }

        return await self.invoke(data)

    async def getForumTopicDefaultIcons(self) -> Result:
        """Returns list of custom emojis, which can be used as forum topic icon by all users


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getForumTopicDefaultIcons",
        }

        return await self.invoke(data)

    async def createForumTopic(self, chat_id: int, name: str, icon: dict) -> Result:
        """Creates a topic in a forum supergroup chat; requires can\_manage\_topics rights in the supergroup

        Args:
            chat_id (``int``):
                Identifier of the chat

            name (``str``):
                Name of the topic; 1\-128 characters

            icon (``forumTopicIcon``):
                Icon of the topic\. Icon color must be one of 0x6FB9F0, 0xFFD67E, 0xCB86DB, 0x8EEE98, 0xFF93B2, or 0xFB6F5F\. Telegram Premium users can use any custom emoji as topic icon, other users can use only a custom emoji returned by getForumTopicDefaultIcons


        Returns:
            :class:`~pytdbot.types.Result` (``ForumTopicInfo``)
        """

        data = {
            "@type": "createForumTopic",
            "chat_id": chat_id,
            "name": name,
            "icon": icon,
        }

        return await self.invoke(data)

    async def editForumTopic(
        self,
        chat_id: int,
        message_thread_id: int,
        name: str,
        edit_icon_custom_emoji: bool,
        icon_custom_emoji_id: int,
    ) -> Result:
        """Edits title and icon of a topic in a forum supergroup chat; requires can\_manage\_topics administrator right in the supergroup unless the user is creator of the topic

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier of the forum topic

            name (``str``):
                New name of the topic; 0\-128 characters\. If empty, the previous topic name is kept

            edit_icon_custom_emoji (``bool``):
                Pass true to edit the icon of the topic\. Icon of the General topic can't be edited

            icon_custom_emoji_id (``int``):
                Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji\. Ignored if edit\_icon\_custom\_emoji is false\. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editForumTopic",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "name": name,
            "edit_icon_custom_emoji": edit_icon_custom_emoji,
            "icon_custom_emoji_id": icon_custom_emoji_id,
        }

        return await self.invoke(data)

    async def getForumTopic(self, chat_id: int, message_thread_id: int) -> Result:
        """Returns information about a forum topic

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier of the forum topic


        Returns:
            :class:`~pytdbot.types.Result` (``ForumTopic``)
        """

        data = {
            "@type": "getForumTopic",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def getForumTopicLink(self, chat_id: int, message_thread_id: int) -> Result:
        """Returns an HTTPS link to a topic in a forum chat\. This is an offline request

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier of the forum topic


        Returns:
            :class:`~pytdbot.types.Result` (``MessageLink``)
        """

        data = {
            "@type": "getForumTopicLink",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def getForumTopics(
        self,
        chat_id: int,
        query: str,
        offset_date: int,
        offset_message_id: int,
        offset_message_thread_id: int,
        limit: int,
    ) -> Result:
        """Returns found forum topics in a forum chat\. This is a temporary method for getting information about topic list from the server

        Args:
            chat_id (``int``):
                Identifier of the forum chat

            query (``str``):
                Query to search for in the forum topic's name

            offset_date (``int``):
                The date starting from which the results need to be fetched\. Use 0 or any date in the future to get results from the last topic

            offset_message_id (``int``):
                The message identifier of the last message in the last found topic, or 0 for the first request

            offset_message_thread_id (``int``):
                The message thread identifier of the last found topic, or 0 for the first request

            limit (``int``):
                The maximum number of forum topics to be returned; up to 100\. For optimal performance, the number of returned forum topics is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``ForumTopics``)
        """

        data = {
            "@type": "getForumTopics",
            "chat_id": chat_id,
            "query": query,
            "offset_date": offset_date,
            "offset_message_id": offset_message_id,
            "offset_message_thread_id": offset_message_thread_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def setForumTopicNotificationSettings(
        self, chat_id: int, message_thread_id: int, notification_settings: dict
    ) -> Result:
        """Changes the notification settings of a forum topic

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                Message thread identifier of the forum topic

            notification_settings (``chatNotificationSettings``):
                New notification settings for the forum topic\. If the topic is muted for more than 366 days, it is considered to be muted forever


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setForumTopicNotificationSettings",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "notification_settings": notification_settings,
        }

        return await self.invoke(data)

    async def toggleForumTopicIsClosed(
        self, chat_id: int, message_thread_id: int, is_closed: bool
    ) -> Result:
        """Toggles whether a topic is closed in a forum supergroup chat; requires can\_manage\_topics administrator right in the supergroup unless the user is creator of the topic

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier of the forum topic

            is_closed (``bool``):
                Pass true to close the topic; pass false to reopen it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleForumTopicIsClosed",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "is_closed": is_closed,
        }

        return await self.invoke(data)

    async def toggleGeneralForumTopicIsHidden(
        self, chat_id: int, is_hidden: bool
    ) -> Result:
        """Toggles whether a General topic is hidden in a forum supergroup chat; requires can\_manage\_topics administrator right in the supergroup

        Args:
            chat_id (``int``):
                Identifier of the chat

            is_hidden (``bool``):
                Pass true to hide and close the General topic; pass false to unhide it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGeneralForumTopicIsHidden",
            "chat_id": chat_id,
            "is_hidden": is_hidden,
        }

        return await self.invoke(data)

    async def toggleForumTopicIsPinned(
        self, chat_id: int, message_thread_id: int, is_pinned: bool
    ) -> Result:
        """Changes the pinned state of a forum topic; requires can\_manage\_topics administrator right in the supergroup\. There can be up to getOption\("pinned\_forum\_topic\_count\_max"\) pinned forum topics

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                Message thread identifier of the forum topic

            is_pinned (``bool``):
                Pass true to pin the topic; pass false to unpin it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleForumTopicIsPinned",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "is_pinned": is_pinned,
        }

        return await self.invoke(data)

    async def setPinnedForumTopics(
        self, chat_id: int, message_thread_ids: list
    ) -> Result:
        """Changes the order of pinned forum topics

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_ids (``list``):
                The new list of pinned forum topics


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setPinnedForumTopics",
            "chat_id": chat_id,
            "message_thread_ids": message_thread_ids,
        }

        return await self.invoke(data)

    async def deleteForumTopic(self, chat_id: int, message_thread_id: int) -> Result:
        """Deletes all messages in a forum topic; requires can\_delete\_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier of the forum topic


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteForumTopic",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def getEmojiReaction(self, emoji: str) -> Result:
        """Returns information about a emoji reaction\. Returns a 404 error if the reaction is not found

        Args:
            emoji (``str``):
                Text representation of the reaction


        Returns:
            :class:`~pytdbot.types.Result` (``EmojiReaction``)
        """

        data = {
            "@type": "getEmojiReaction",
            "emoji": emoji,
        }

        return await self.invoke(data)

    async def getCustomEmojiReactionAnimations(self) -> Result:
        """Returns TGS stickers with generic animations for custom emoji reactions


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getCustomEmojiReactionAnimations",
        }

        return await self.invoke(data)

    async def getMessageAvailableReactions(
        self, chat_id: int, message_id: int, row_size: int
    ) -> Result:
        """Returns reactions, which can be added to a message\. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            row_size (``int``):
                Number of reaction per row, 5\-25


        Returns:
            :class:`~pytdbot.types.Result` (``AvailableReactions``)
        """

        data = {
            "@type": "getMessageAvailableReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "row_size": row_size,
        }

        return await self.invoke(data)

    async def clearRecentReactions(self) -> Result:
        """Clears the list of recently used reactions


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearRecentReactions",
        }

        return await self.invoke(data)

    async def addMessageReaction(
        self,
        chat_id: int,
        message_id: int,
        reaction_type: dict,
        is_big: bool,
        update_recent_reactions: bool,
    ) -> Result:
        """Adds a reaction to a message\. Use getMessageAvailableReactions to receive the list of available reactions for the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            reaction_type (``ReactionType``):
                Type of the reaction to add

            is_big (``bool``):
                Pass true if the reaction is added with a big animation

            update_recent_reactions (``bool``):
                Pass true if the reaction needs to be added to recent reactions


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addMessageReaction",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
            "is_big": is_big,
            "update_recent_reactions": update_recent_reactions,
        }

        return await self.invoke(data)

    async def removeMessageReaction(
        self, chat_id: int, message_id: int, reaction_type: dict
    ) -> Result:
        """Removes a reaction from a message\. A chosen reaction can always be removed

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            reaction_type (``ReactionType``):
                Type of the reaction to remove


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeMessageReaction",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
        }

        return await self.invoke(data)

    async def getMessageAddedReactions(
        self,
        chat_id: int,
        message_id: int,
        offset: str,
        limit: int,
        reaction_type: dict = None,
    ) -> Result:
        """Returns reactions added for a message, along with their sender

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of reactions to be returned; must be positive and can't be greater than 100

            reaction_type (``ReactionType``, *optional*):
                Type of the reactions to return; pass null to return all added reactions


        Returns:
            :class:`~pytdbot.types.Result` (``AddedReactions``)
        """

        data = {
            "@type": "getMessageAddedReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def setDefaultReactionType(self, reaction_type: dict) -> Result:
        """Changes type of default reaction for the current user

        Args:
            reaction_type (``ReactionType``):
                New type of the default reaction


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setDefaultReactionType",
            "reaction_type": reaction_type,
        }

        return await self.invoke(data)

    async def searchQuote(self, text: dict, quote: dict, quote_position: int) -> Result:
        """Searches for a given quote in a text\. Returns found quote start position in UTF\-16 code units\. Returns a 404 error if the quote is not found\. Can be called synchronously

        Args:
            text (``formattedText``):
                Text in which to search for the quote

            quote (``formattedText``):
                Quote to search for

            quote_position (``int``):
                Approximate quote position in UTF\-16 code units


        Returns:
            :class:`~pytdbot.types.Result` (``FoundPosition``)
        """

        data = {
            "@type": "searchQuote",
            "text": text,
            "quote": quote,
            "quote_position": quote_position,
        }

        return await self.invoke(data)

    async def getTextEntities(self, text: str) -> Result:
        """Returns all entities \(mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses\) found in the text\. Can be called synchronously

        Args:
            text (``str``):
                The text in which to look for entities


        Returns:
            :class:`~pytdbot.types.Result` (``TextEntities``)
        """

        data = {
            "@type": "getTextEntities",
            "text": text,
        }

        return await self.invoke(data)

    async def parseTextEntities(self, text: str, parse_mode: dict) -> Result:
        """Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, BlockQuote, Code, Pre, PreCode, TextUrl and MentionName entities from a marked\-up text\. Can be called synchronously

        Args:
            text (``str``):
                The text to parse

            parse_mode (``TextParseMode``):
                Text parse mode


        Returns:
            :class:`~pytdbot.types.Result` (``FormattedText``)
        """

        data = {
            "@type": "parseTextEntities",
            "text": text,
            "parse_mode": parse_mode,
        }

        return await self.invoke(data)

    async def parseMarkdown(self, text: dict) -> Result:
        """Parses Markdown entities in a human\-friendly format, ignoring markup errors\. Can be called synchronously

        Args:
            text (``formattedText``):
                The text to parse\. For example, "\_\_italic\_\_ \~\~strikethrough\~\~ \|\|spoiler\|\| \*\*bold\*\* \`code\` \`\`\`pre\`\`\` \_\_\[italic\_\_ text\_url\]\(telegram\.org\) \_\_italic\*\*bold italic\_\_bold\*\*"


        Returns:
            :class:`~pytdbot.types.Result` (``FormattedText``)
        """

        data = {
            "@type": "parseMarkdown",
            "text": text,
        }

        return await self.invoke(data)

    async def getMarkdownText(self, text: dict) -> Result:
        """Replaces text entities with Markdown formatting in a human\-friendly format\. Entities that can't be represented in Markdown unambiguously are kept as is\. Can be called synchronously

        Args:
            text (``formattedText``):
                The text


        Returns:
            :class:`~pytdbot.types.Result` (``FormattedText``)
        """

        data = {
            "@type": "getMarkdownText",
            "text": text,
        }

        return await self.invoke(data)

    async def getFileMimeType(self, file_name: str) -> Result:
        """Returns the MIME type of a file, guessed by its extension\. Returns an empty string on failure\. Can be called synchronously

        Args:
            file_name (``str``):
                The name of the file or path to the file


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getFileMimeType",
            "file_name": file_name,
        }

        return await self.invoke(data)

    async def getFileExtension(self, mime_type: str) -> Result:
        """Returns the extension of a file, guessed by its MIME type\. Returns an empty string on failure\. Can be called synchronously

        Args:
            mime_type (``str``):
                The MIME type of the file


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getFileExtension",
            "mime_type": mime_type,
        }

        return await self.invoke(data)

    async def cleanFileName(self, file_name: str) -> Result:
        """Removes potentially dangerous characters from the name of a file\. The encoding of the file name is supposed to be UTF\-8\. Returns an empty string on failure\. Can be called synchronously

        Args:
            file_name (``str``):
                File name or path to the file


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "cleanFileName",
            "file_name": file_name,
        }

        return await self.invoke(data)

    async def getLanguagePackString(
        self,
        language_pack_database_path: str,
        localization_target: str,
        language_pack_id: str,
        key: str,
    ) -> Result:
        """Returns a string stored in the local database from the specified localization target and language pack by its key\. Returns a 404 error if the string is not found\. Can be called synchronously

        Args:
            language_pack_database_path (``str``):
                Path to the language pack database in which strings are stored

            localization_target (``str``):
                Localization target to which the language pack belongs

            language_pack_id (``str``):
                Language pack identifier

            key (``str``):
                Language pack key of the string to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``LanguagePackStringValue``)
        """

        data = {
            "@type": "getLanguagePackString",
            "language_pack_database_path": language_pack_database_path,
            "localization_target": localization_target,
            "language_pack_id": language_pack_id,
            "key": key,
        }

        return await self.invoke(data)

    async def getJsonValue(self, json: str) -> Result:
        """Converts a JSON\-serialized string to corresponding JsonValue object\. Can be called synchronously

        Args:
            json (``str``):
                The JSON\-serialized string


        Returns:
            :class:`~pytdbot.types.Result` (``JsonValue``)
        """

        data = {
            "@type": "getJsonValue",
            "json": json,
        }

        return await self.invoke(data)

    async def getJsonString(self, json_value: dict) -> Result:
        """Converts a JsonValue object to corresponding JSON\-serialized string\. Can be called synchronously

        Args:
            json_value (``JsonValue``):
                The JsonValue object


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getJsonString",
            "json_value": json_value,
        }

        return await self.invoke(data)

    async def getThemeParametersJsonString(self, theme: dict) -> Result:
        """Converts a themeParameters object to corresponding JSON\-serialized string\. Can be called synchronously

        Args:
            theme (``themeParameters``):
                Theme parameters to convert to JSON


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getThemeParametersJsonString",
            "theme": theme,
        }

        return await self.invoke(data)

    async def setPollAnswer(
        self, chat_id: int, message_id: int, option_ids: list
    ) -> Result:
        """Changes the user answer to a poll\. A poll in quiz mode can be answered only once

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            option_ids (``list``):
                0\-based identifiers of answer options, chosen by the user\. User can choose more than 1 answer option only is the poll allows multiple answers


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setPollAnswer",
            "chat_id": chat_id,
            "message_id": message_id,
            "option_ids": option_ids,
        }

        return await self.invoke(data)

    async def getPollVoters(
        self, chat_id: int, message_id: int, option_id: int, offset: int, limit: int
    ) -> Result:
        """Returns message senders voted for the specified option in a non\-anonymous polls\. For optimal performance, the number of returned users is chosen by TDLib

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            option_id (``int``):
                0\-based identifier of the answer option

            offset (``int``):
                Number of voters to skip in the result; must be non\-negative

            limit (``int``):
                The maximum number of voters to be returned; must be positive and can't be greater than 50\. For optimal performance, the number of returned voters is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached


        Returns:
            :class:`~pytdbot.types.Result` (``MessageSenders``)
        """

        data = {
            "@type": "getPollVoters",
            "chat_id": chat_id,
            "message_id": message_id,
            "option_id": option_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def stopPoll(
        self, chat_id: int, message_id: int, reply_markup: dict = None
    ) -> Result:
        """Stops a poll\. A poll in a message can be stopped when the message has can\_be\_edited flag is set

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            reply_markup (``ReplyMarkup``, *optional*):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "stopPoll",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data)

    async def hideSuggestedAction(self, action: dict) -> Result:
        """Hides a suggested action

        Args:
            action (``SuggestedAction``):
                Suggested action to hide


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "hideSuggestedAction",
            "action": action,
        }

        return await self.invoke(data)

    async def getLoginUrlInfo(
        self, chat_id: int, message_id: int, button_id: int
    ) -> Result:
        """Returns information about a button of type inlineKeyboardButtonTypeLoginUrl\. The method needs to be called when the user presses the button

        Args:
            chat_id (``int``):
                Chat identifier of the message with the button

            message_id (``int``):
                Message identifier of the message with the button

            button_id (``int``):
                Button identifier


        Returns:
            :class:`~pytdbot.types.Result` (``LoginUrlInfo``)
        """

        data = {
            "@type": "getLoginUrlInfo",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
        }

        return await self.invoke(data)

    async def getLoginUrl(
        self, chat_id: int, message_id: int, button_id: int, allow_write_access: bool
    ) -> Result:
        """Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl\. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed\. If an error is returned, then the button must be handled as an ordinary URL button

        Args:
            chat_id (``int``):
                Chat identifier of the message with the button

            message_id (``int``):
                Message identifier of the message with the button

            button_id (``int``):
                Button identifier

            allow_write_access (``bool``):
                Pass true to allow the bot to send messages to the current user


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getLoginUrl",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data)

    async def shareUserWithBot(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        shared_user_id: int,
        only_check: bool,
    ) -> Result:
        """Shares a user after pressing a keyboardButtonTypeRequestUser button with the bot

        Args:
            chat_id (``int``):
                Identifier of the chat with the bot

            message_id (``int``):
                Identifier of the message with the button

            button_id (``int``):
                Identifier of the button

            shared_user_id (``int``):
                Identifier of the shared user

            only_check (``bool``):
                Pass true to check that the user can be shared by the button instead of actually sharing them


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "shareUserWithBot",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
            "shared_user_id": shared_user_id,
            "only_check": only_check,
        }

        return await self.invoke(data)

    async def shareChatWithBot(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        shared_chat_id: int,
        only_check: bool,
    ) -> Result:
        """Shares a chat after pressing a keyboardButtonTypeRequestChat button with the bot

        Args:
            chat_id (``int``):
                Identifier of the chat with the bot

            message_id (``int``):
                Identifier of the message with the button

            button_id (``int``):
                Identifier of the button

            shared_chat_id (``int``):
                Identifier of the shared chat

            only_check (``bool``):
                Pass true to check that the chat can be shared by the button instead of actually sharing it\. Doesn't check bot\_is\_member and bot\_administrator\_rights restrictions\. If the bot must be a member, then all chats from getGroupsInCommon and all chats, where the user can add the bot, are suitable\. In the latter case the bot will be automatically added to the chat\. If the bot must be an administrator, then all chats, where the bot already has requested rights or can be added to administrators by the user, are suitable\. In the latter case the bot will be automatically granted requested rights


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "shareChatWithBot",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
            "shared_chat_id": shared_chat_id,
            "only_check": only_check,
        }

        return await self.invoke(data)

    async def getInlineQueryResults(
        self,
        bot_user_id: int,
        chat_id: int,
        query: str,
        offset: str,
        user_location: dict = None,
    ) -> Result:
        """Sends an inline query to a bot and returns its results\. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            chat_id (``int``):
                Identifier of the chat where the query was sent

            query (``str``):
                Text of the query

            offset (``str``):
                Offset of the first entry to return; use empty string to get the first chunk of results

            user_location (``location``, *optional*):
                Location of the user; pass null if unknown or the bot doesn't need user's location


        Returns:
            :class:`~pytdbot.types.Result` (``InlineQueryResults``)
        """

        data = {
            "@type": "getInlineQueryResults",
            "bot_user_id": bot_user_id,
            "chat_id": chat_id,
            "user_location": user_location,
            "query": query,
            "offset": offset,
        }

        return await self.invoke(data)

    async def answerInlineQuery(
        self,
        inline_query_id: int,
        is_personal: bool,
        results: list,
        cache_time: int,
        next_offset: str,
        button: dict = None,
    ) -> Result:
        """Sets the result of an inline query; for bots only

        Args:
            inline_query_id (``int``):
                Identifier of the inline query

            is_personal (``bool``):
                Pass true if results may be cached and returned only for the user that sent the query\. By default, results may be returned to any user who sends the same query

            results (``list``):
                The results of the query

            cache_time (``int``):
                Allowed time to cache the results of the query, in seconds

            next_offset (``str``):
                Offset for the next inline query; pass an empty string if there are no more results

            button (``inlineQueryResultsButton``, *optional*):
                Button to be shown above inline query results; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "answerInlineQuery",
            "inline_query_id": inline_query_id,
            "is_personal": is_personal,
            "button": button,
            "results": results,
            "cache_time": cache_time,
            "next_offset": next_offset,
        }

        return await self.invoke(data)

    async def searchWebApp(self, bot_user_id: int, web_app_short_name: str) -> Result:
        """Returns information about a Web App by its short name\. Returns a 404 error if the Web App is not found

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            web_app_short_name (``str``):
                Short name of the Web App


        Returns:
            :class:`~pytdbot.types.Result` (``FoundWebApp``)
        """

        data = {
            "@type": "searchWebApp",
            "bot_user_id": bot_user_id,
            "web_app_short_name": web_app_short_name,
        }

        return await self.invoke(data)

    async def getWebAppLinkUrl(
        self,
        chat_id: int,
        bot_user_id: int,
        web_app_short_name: str,
        start_parameter: str,
        application_name: str,
        allow_write_access: bool,
        theme: dict = None,
    ) -> Result:
        """Returns an HTTPS URL of a Web App to open after a link of the type internalLinkTypeWebApp is clicked

        Args:
            chat_id (``int``):
                Identifier of the chat in which the link was clicked; pass 0 if none

            bot_user_id (``int``):
                Identifier of the target bot

            web_app_short_name (``str``):
                Short name of the Web App

            start_parameter (``str``):
                Start parameter from internalLinkTypeWebApp

            application_name (``str``):
                Short name of the application; 0\-64 English letters, digits, and underscores

            allow_write_access (``bool``):
                Pass true if the current user allowed the bot to send them messages

            theme (``themeParameters``, *optional*):
                Preferred Web App theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getWebAppLinkUrl",
            "chat_id": chat_id,
            "bot_user_id": bot_user_id,
            "web_app_short_name": web_app_short_name,
            "start_parameter": start_parameter,
            "theme": theme,
            "application_name": application_name,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data)

    async def getWebAppUrl(
        self, bot_user_id: int, url: str, application_name: str, theme: dict = None
    ) -> Result:
        """Returns an HTTPS URL of a Web App to open from the side menu, a keyboardButtonTypeWebApp button, an inlineQueryResultsButtonTypeWebApp button, or an internalLinkTypeSideMenuBot link

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            url (``str``):
                The URL from a keyboardButtonTypeWebApp button, inlineQueryResultsButtonTypeWebApp button, an internalLinkTypeSideMenuBot link, or an empty when the bot is opened from the side menu

            application_name (``str``):
                Short name of the application; 0\-64 English letters, digits, and underscores

            theme (``themeParameters``, *optional*):
                Preferred Web App theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getWebAppUrl",
            "bot_user_id": bot_user_id,
            "url": url,
            "theme": theme,
            "application_name": application_name,
        }

        return await self.invoke(data)

    async def sendWebAppData(
        self, bot_user_id: int, button_text: str, data: str
    ) -> Result:
        """Sends data received from a keyboardButtonTypeWebApp Web App to a bot

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            button_text (``str``):
                Text of the keyboardButtonTypeWebApp button, which opened the Web App

            data (``str``):
                The data


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendWebAppData",
            "bot_user_id": bot_user_id,
            "button_text": button_text,
            "data": data,
        }

        return await self.invoke(data)

    async def openWebApp(
        self,
        chat_id: int,
        bot_user_id: int,
        url: str,
        application_name: str,
        message_thread_id: int,
        theme: dict = None,
        reply_to: dict = None,
    ) -> Result:
        """Informs TDLib that a Web App is being opened from the attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button\. For each bot, a confirmation alert about data sent to the bot must be shown once

        Args:
            chat_id (``int``):
                Identifier of the chat in which the Web App is opened\. The Web App can't be opened in secret chats

            bot_user_id (``int``):
                Identifier of the bot, providing the Web App

            url (``str``):
                The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise

            application_name (``str``):
                Short name of the application; 0\-64 English letters, digits, and underscores

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent

            theme (``themeParameters``, *optional*):
                Preferred Web App theme; pass null to use the default theme

            reply_to (``InputMessageReplyTo``, *optional*):
                Information about the message or story to be replied in the message sent by the Web App; pass null if none


        Returns:
            :class:`~pytdbot.types.Result` (``WebAppInfo``)
        """

        data = {
            "@type": "openWebApp",
            "chat_id": chat_id,
            "bot_user_id": bot_user_id,
            "url": url,
            "theme": theme,
            "application_name": application_name,
            "message_thread_id": message_thread_id,
            "reply_to": reply_to,
        }

        return await self.invoke(data)

    async def closeWebApp(self, web_app_launch_id: int) -> Result:
        """Informs TDLib that a previously opened Web App was closed

        Args:
            web_app_launch_id (``int``):
                Identifier of Web App launch, received from openWebApp


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "closeWebApp",
            "web_app_launch_id": web_app_launch_id,
        }

        return await self.invoke(data)

    async def answerWebAppQuery(self, web_app_query_id: str, result: dict) -> Result:
        """Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

        Args:
            web_app_query_id (``str``):
                Identifier of the Web App query

            result (``InputInlineQueryResult``):
                The result of the query


        Returns:
            :class:`~pytdbot.types.Result` (``SentWebAppMessage``)
        """

        data = {
            "@type": "answerWebAppQuery",
            "web_app_query_id": web_app_query_id,
            "result": result,
        }

        return await self.invoke(data)

    async def getCallbackQueryAnswer(
        self, chat_id: int, message_id: int, payload: dict
    ) -> Result:
        """Sends a callback query to a bot and returns an answer\. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Args:
            chat_id (``int``):
                Identifier of the chat with the message

            message_id (``int``):
                Identifier of the message from which the query originated

            payload (``CallbackQueryPayload``):
                Query payload


        Returns:
            :class:`~pytdbot.types.Result` (``CallbackQueryAnswer``)
        """

        data = {
            "@type": "getCallbackQueryAnswer",
            "chat_id": chat_id,
            "message_id": message_id,
            "payload": payload,
        }

        return await self.invoke(data)

    async def answerCallbackQuery(
        self,
        callback_query_id: int,
        text: str,
        show_alert: bool,
        url: str,
        cache_time: int,
    ) -> Result:
        """Sets the result of a callback query; for bots only

        Args:
            callback_query_id (``int``):
                Identifier of the callback query

            text (``str``):
                Text of the answer

            show_alert (``bool``):
                Pass true to show an alert to the user instead of a toast notification

            url (``str``):
                URL to be opened

            cache_time (``int``):
                Time during which the result of the query can be cached, in seconds


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "answerCallbackQuery",
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": show_alert,
            "url": url,
            "cache_time": cache_time,
        }

        return await self.invoke(data)

    async def answerShippingQuery(
        self, shipping_query_id: int, shipping_options: list, error_message: str
    ) -> Result:
        """Sets the result of a shipping query; for bots only

        Args:
            shipping_query_id (``int``):
                Identifier of the shipping query

            shipping_options (``list``):
                Available shipping options

            error_message (``str``):
                An error message, empty on success


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "answerShippingQuery",
            "shipping_query_id": shipping_query_id,
            "shipping_options": shipping_options,
            "error_message": error_message,
        }

        return await self.invoke(data)

    async def answerPreCheckoutQuery(
        self, pre_checkout_query_id: int, error_message: str
    ) -> Result:
        """Sets the result of a pre\-checkout query; for bots only

        Args:
            pre_checkout_query_id (``int``):
                Identifier of the pre\-checkout query

            error_message (``str``):
                An error message, empty on success


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "answerPreCheckoutQuery",
            "pre_checkout_query_id": pre_checkout_query_id,
            "error_message": error_message,
        }

        return await self.invoke(data)

    async def setGameScore(
        self,
        chat_id: int,
        message_id: int,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
    ) -> Result:
        """Updates the game score of the specified user in the game; for bots only

        Args:
            chat_id (``int``):
                The chat to which the message with the game belongs

            message_id (``int``):
                Identifier of the message

            edit_message (``bool``):
                Pass true to edit the game message to include the current scoreboard

            user_id (``int``):
                User identifier

            score (``int``):
                The new score

            force (``bool``):
                Pass true to update the score even if it decreases\. If the score is 0, the user will be deleted from the high score table


        Returns:
            :class:`~pytdbot.types.Result` (``Message``)
        """

        data = {
            "@type": "setGameScore",
            "chat_id": chat_id,
            "message_id": message_id,
            "edit_message": edit_message,
            "user_id": user_id,
            "score": score,
            "force": force,
        }

        return await self.invoke(data)

    async def setInlineGameScore(
        self,
        inline_message_id: str,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
    ) -> Result:
        """Updates the game score of the specified user in a game; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            edit_message (``bool``):
                Pass true to edit the game message to include the current scoreboard

            user_id (``int``):
                User identifier

            score (``int``):
                The new score

            force (``bool``):
                Pass true to update the score even if it decreases\. If the score is 0, the user will be deleted from the high score table


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setInlineGameScore",
            "inline_message_id": inline_message_id,
            "edit_message": edit_message,
            "user_id": user_id,
            "score": score,
            "force": force,
        }

        return await self.invoke(data)

    async def getGameHighScores(
        self, chat_id: int, message_id: int, user_id: int
    ) -> Result:
        """Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only

        Args:
            chat_id (``int``):
                The chat that contains the message with the game

            message_id (``int``):
                Identifier of the message

            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Result` (``GameHighScores``)
        """

        data = {
            "@type": "getGameHighScores",
            "chat_id": chat_id,
            "message_id": message_id,
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def getInlineGameHighScores(
        self, inline_message_id: str, user_id: int
    ) -> Result:
        """Returns game high scores and some part of the high score table in the range of the specified user; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Result` (``GameHighScores``)
        """

        data = {
            "@type": "getInlineGameHighScores",
            "inline_message_id": inline_message_id,
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def deleteChatReplyMarkup(self, chat_id: int, message_id: int) -> Result:
        """Deletes the default reply markup from a chat\. Must be called after a one\-time keyboard or a replyMarkupForceReply reply markup has been used\. An updateChatReplyMarkup update will be sent if the reply markup is changed

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                The message identifier of the used keyboard


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatReplyMarkup",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def sendChatAction(
        self, chat_id: int, message_thread_id: int, action: dict = None
    ) -> Result:
        """Sends a notification about user activity in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the action was performed

            action (``ChatAction``, *optional*):
                The action description; pass null to cancel the currently active action


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendChatAction",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "action": action,
        }

        return await self.invoke(data)

    async def openChat(self, chat_id: int) -> Result:
        """Informs TDLib that the chat is opened by the user\. Many useful activities depend on the chat being opened or closed \(e\.g\., in supergroups and channels all updates are received only for opened chats\)

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "openChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def closeChat(self, chat_id: int) -> Result:
        """Informs TDLib that the chat is closed by the user\. Many useful activities depend on the chat being opened or closed

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "closeChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def viewMessages(
        self, chat_id: int, message_ids: list, force_read: bool, source: dict = None
    ) -> Result:
        """Informs TDLib that messages are being viewed by the user\. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen \(excluding the button\)\. Many useful activities depend on whether the messages are currently being viewed or not \(e\.g\., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels\)

        Args:
            chat_id (``int``):
                Chat identifier

            message_ids (``list``):
                The identifiers of the messages being viewed

            force_read (``bool``):
                Pass true to mark as read the specified messages even the chat is closed

            source (``MessageSource``, *optional*):
                Source of the message view; pass null to guess the source based on chat open state


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "viewMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "source": source,
            "force_read": force_read,
        }

        return await self.invoke(data)

    async def openMessageContent(self, chat_id: int, message_id: int) -> Result:
        """Informs TDLib that the message content has been opened \(e\.g\., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message\)\. An updateMessageContentOpened update will be generated if something has changed

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Identifier of the message with the opened content


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "openMessageContent",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def clickAnimatedEmojiMessage(self, chat_id: int, message_id: int) -> Result:
        """Informs TDLib that a message with an animated emoji was clicked by the user\. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Identifier of the clicked message


        Returns:
            :class:`~pytdbot.types.Result` (``Sticker``)
        """

        data = {
            "@type": "clickAnimatedEmojiMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getInternalLink(self, type: dict, is_http: bool) -> Result:
        """Returns an HTTPS or a tg: link with the given type\. Can be called before authorization

        Args:
            type (``InternalLinkType``):
                Expected type of the link

            is_http (``bool``):
                Pass true to create an HTTPS link \(only available for some link types\); pass false to create a tg: link


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getInternalLink",
            "type": type,
            "is_http": is_http,
        }

        return await self.invoke(data)

    async def getInternalLinkType(self, link: str) -> Result:
        """Returns information about the type of an internal link\. Returns a 404 error if the link is not internal\. Can be called before authorization

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Result` (``InternalLinkType``)
        """

        data = {
            "@type": "getInternalLinkType",
            "link": link,
        }

        return await self.invoke(data)

    async def getExternalLinkInfo(self, link: str) -> Result:
        """Returns information about an action to be done when the current user clicks an external link\. Don't use this method for links from secret chats if web page preview is disabled in secret chats

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Result` (``LoginUrlInfo``)
        """

        data = {
            "@type": "getExternalLinkInfo",
            "link": link,
        }

        return await self.invoke(data)

    async def getExternalLink(self, link: str, allow_write_access: bool) -> Result:
        """Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link\. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

        Args:
            link (``str``):
                The HTTP link

            allow_write_access (``bool``):
                Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getExternalLink",
            "link": link,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data)

    async def readAllChatMentions(self, chat_id: int) -> Result:
        """Marks all mentions in a chat as read

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "readAllChatMentions",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def readAllMessageThreadMentions(
        self, chat_id: int, message_thread_id: int
    ) -> Result:
        """Marks all mentions in a forum topic as read

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                Message thread identifier in which mentions are marked as read


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "readAllMessageThreadMentions",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def readAllChatReactions(self, chat_id: int) -> Result:
        """Marks all reactions in a chat or a forum topic as read

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "readAllChatReactions",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def readAllMessageThreadReactions(
        self, chat_id: int, message_thread_id: int
    ) -> Result:
        """Marks all reactions in a forum topic as read

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                Message thread identifier in which reactions are marked as read


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "readAllMessageThreadReactions",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def createPrivateChat(self, user_id: int, force: bool) -> Result:
        """Returns an existing chat corresponding to a given user

        Args:
            user_id (``int``):
                User identifier

            force (``bool``):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createPrivateChat",
            "user_id": user_id,
            "force": force,
        }

        return await self.invoke(data)

    async def createBasicGroupChat(self, basic_group_id: int, force: bool) -> Result:
        """Returns an existing chat corresponding to a known basic group

        Args:
            basic_group_id (``int``):
                Basic group identifier

            force (``bool``):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createBasicGroupChat",
            "basic_group_id": basic_group_id,
            "force": force,
        }

        return await self.invoke(data)

    async def createSupergroupChat(self, supergroup_id: int, force: bool) -> Result:
        """Returns an existing chat corresponding to a known supergroup or channel

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier

            force (``bool``):
                Pass true to create the chat without a network request\. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createSupergroupChat",
            "supergroup_id": supergroup_id,
            "force": force,
        }

        return await self.invoke(data)

    async def createSecretChat(self, secret_chat_id: int) -> Result:
        """Returns an existing chat corresponding to a known secret chat

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data)

    async def createNewBasicGroupChat(
        self, title: str, message_auto_delete_time: int, user_ids: list = None
    ) -> Result:
        """Creates a new basic group and sends a corresponding messageBasicGroupChatCreate\. Returns the newly created chat

        Args:
            title (``str``):
                Title of the new basic group; 1\-128 characters

            message_auto_delete_time (``int``):
                Message auto\-delete time value, in seconds; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

            user_ids (``list``, *optional*):
                Identifiers of users to be added to the basic group; may be empty to create a basic group without other members


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createNewBasicGroupChat",
            "user_ids": user_ids,
            "title": title,
            "message_auto_delete_time": message_auto_delete_time,
        }

        return await self.invoke(data)

    async def createNewSupergroupChat(
        self,
        title: str,
        is_forum: bool,
        is_channel: bool,
        description: str,
        message_auto_delete_time: int,
        for_import: bool,
        location: dict = None,
    ) -> Result:
        """Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate\. Returns the newly created chat

        Args:
            title (``str``):
                Title of the new chat; 1\-128 characters

            is_forum (``bool``):
                Pass true to create a forum supergroup chat

            is_channel (``bool``):
                Pass true to create a channel chat; ignored if a forum is created

            description (``str``):
                Chat description; 0\-255 characters

            message_auto_delete_time (``int``):
                Message auto\-delete time value, in seconds; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically

            for_import (``bool``):
                Pass true to create a supergroup for importing messages using importMessages

            location (``chatLocation``, *optional*):
                Chat location if a location\-based supergroup is being created; pass null to create an ordinary supergroup chat


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createNewSupergroupChat",
            "title": title,
            "is_forum": is_forum,
            "is_channel": is_channel,
            "description": description,
            "location": location,
            "message_auto_delete_time": message_auto_delete_time,
            "for_import": for_import,
        }

        return await self.invoke(data)

    async def createNewSecretChat(self, user_id: int) -> Result:
        """Creates a new secret chat\. Returns the newly created chat

        Args:
            user_id (``int``):
                Identifier of the target user


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "createNewSecretChat",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def upgradeBasicGroupChatToSupergroupChat(self, chat_id: int) -> Result:
        """Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges\. Deactivates the original basic group

        Args:
            chat_id (``int``):
                Identifier of the chat to upgrade


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "upgradeBasicGroupChatToSupergroupChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatListsToAddChat(self, chat_id: int) -> Result:
        """Returns chat lists to which the chat can be added\. This is an offline request

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatLists``)
        """

        data = {
            "@type": "getChatListsToAddChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def addChatToList(self, chat_id: int, chat_list: dict) -> Result:
        """Adds a chat to a chat list\. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

        Args:
            chat_id (``int``):
                Chat identifier

            chat_list (``ChatList``):
                The chat list\. Use getChatListsToAddChat to get suitable chat lists


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addChatToList",
            "chat_id": chat_id,
            "chat_list": chat_list,
        }

        return await self.invoke(data)

    async def getChatFolder(self, chat_folder_id: int) -> Result:
        """Returns information about a chat folder by its identifier

        Args:
            chat_folder_id (``int``):
                Chat folder identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolder``)
        """

        data = {
            "@type": "getChatFolder",
            "chat_folder_id": chat_folder_id,
        }

        return await self.invoke(data)

    async def createChatFolder(self, folder: dict) -> Result:
        """Creates new chat folder\. Returns information about the created chat folder\. There can be up to getOption\("chat\_folder\_count\_max"\) chat folders, but the limit can be increased with Telegram Premium

        Args:
            folder (``chatFolder``):
                The new chat folder


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInfo``)
        """

        data = {
            "@type": "createChatFolder",
            "folder": folder,
        }

        return await self.invoke(data)

    async def editChatFolder(self, chat_folder_id: int, folder: dict) -> Result:
        """Edits existing chat folder\. Returns information about the edited chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            folder (``chatFolder``):
                The edited chat folder


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInfo``)
        """

        data = {
            "@type": "editChatFolder",
            "chat_folder_id": chat_folder_id,
            "folder": folder,
        }

        return await self.invoke(data)

    async def deleteChatFolder(
        self, chat_folder_id: int, leave_chat_ids: list
    ) -> Result:
        """Deletes existing chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            leave_chat_ids (``list``):
                Identifiers of the chats to leave\. The chats must be pinned or always included in the folder


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatFolder",
            "chat_folder_id": chat_folder_id,
            "leave_chat_ids": leave_chat_ids,
        }

        return await self.invoke(data)

    async def getChatFolderChatsToLeave(self, chat_folder_id: int) -> Result:
        """Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted

        Args:
            chat_folder_id (``int``):
                Chat folder identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatFolderChatsToLeave",
            "chat_folder_id": chat_folder_id,
        }

        return await self.invoke(data)

    async def getChatFolderChatCount(self, folder: dict) -> Result:
        """Returns approximate number of chats in a being created chat folder\. Main and archive chat lists must be fully preloaded for this function to work correctly

        Args:
            folder (``chatFolder``):
                The new chat folder


        Returns:
            :class:`~pytdbot.types.Result` (``Count``)
        """

        data = {
            "@type": "getChatFolderChatCount",
            "folder": folder,
        }

        return await self.invoke(data)

    async def reorderChatFolders(
        self, chat_folder_ids: list, main_chat_list_position: int
    ) -> Result:
        """Changes the order of chat folders

        Args:
            chat_folder_ids (``list``):
                Identifiers of chat folders in the new correct order

            main_chat_list_position (``int``):
                Position of the main chat list among chat folders, 0\-based\. Can be non\-zero only for Premium users


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reorderChatFolders",
            "chat_folder_ids": chat_folder_ids,
            "main_chat_list_position": main_chat_list_position,
        }

        return await self.invoke(data)

    async def getRecommendedChatFolders(self) -> Result:
        """Returns recommended chat folders for the current user


        Returns:
            :class:`~pytdbot.types.Result` (``RecommendedChatFolders``)
        """

        data = {
            "@type": "getRecommendedChatFolders",
        }

        return await self.invoke(data)

    async def getChatFolderDefaultIconName(self, folder: dict) -> Result:
        """Returns default icon name for a folder\. Can be called synchronously

        Args:
            folder (``chatFolder``):
                Chat folder


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderIcon``)
        """

        data = {
            "@type": "getChatFolderDefaultIconName",
            "folder": folder,
        }

        return await self.invoke(data)

    async def getChatsForChatFolderInviteLink(self, chat_folder_id: int) -> Result:
        """Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link

        Args:
            chat_folder_id (``int``):
                Chat folder identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatsForChatFolderInviteLink",
            "chat_folder_id": chat_folder_id,
        }

        return await self.invoke(data)

    async def createChatFolderInviteLink(
        self, chat_folder_id: int, name: str, chat_ids: list
    ) -> Result:
        """Creates a new invite link for a chat folder\. A link can be created for a chat folder if it has only pinned and included chats

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            name (``str``):
                Name of the link; 0\-32 characters

            chat_ids (``list``):
                Identifiers of chats to be accessible by the invite link\. Use getChatsForChatFolderInviteLink to get suitable chats\. Basic groups will be automatically converted to supergroups before link creation


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInviteLink``)
        """

        data = {
            "@type": "createChatFolderInviteLink",
            "chat_folder_id": chat_folder_id,
            "name": name,
            "chat_ids": chat_ids,
        }

        return await self.invoke(data)

    async def getChatFolderInviteLinks(self, chat_folder_id: int) -> Result:
        """Returns invite links created by the current user for a shareable chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInviteLinks``)
        """

        data = {
            "@type": "getChatFolderInviteLinks",
            "chat_folder_id": chat_folder_id,
        }

        return await self.invoke(data)

    async def editChatFolderInviteLink(
        self, chat_folder_id: int, invite_link: str, name: str, chat_ids: list
    ) -> Result:
        """Edits an invite link for a chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            invite_link (``str``):
                Invite link to be edited

            name (``str``):
                New name of the link; 0\-32 characters

            chat_ids (``list``):
                New identifiers of chats to be accessible by the invite link\. Use getChatsForChatFolderInviteLink to get suitable chats\. Basic groups will be automatically converted to supergroups before link editing


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInviteLink``)
        """

        data = {
            "@type": "editChatFolderInviteLink",
            "chat_folder_id": chat_folder_id,
            "invite_link": invite_link,
            "name": name,
            "chat_ids": chat_ids,
        }

        return await self.invoke(data)

    async def deleteChatFolderInviteLink(
        self, chat_folder_id: int, invite_link: str
    ) -> Result:
        """Deletes an invite link for a chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            invite_link (``str``):
                Invite link to be deleted


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatFolderInviteLink",
            "chat_folder_id": chat_folder_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def checkChatFolderInviteLink(self, invite_link: str) -> Result:
        """Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder

        Args:
            invite_link (``str``):
                Invite link to be checked


        Returns:
            :class:`~pytdbot.types.Result` (``ChatFolderInviteLinkInfo``)
        """

        data = {
            "@type": "checkChatFolderInviteLink",
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def addChatFolderByInviteLink(
        self, invite_link: str, chat_ids: list
    ) -> Result:
        """Adds a chat folder by an invite link

        Args:
            invite_link (``str``):
                Invite link for the chat folder

            chat_ids (``list``):
                Identifiers of the chats added to the chat folder\. The chats are automatically joined if they aren't joined yet


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addChatFolderByInviteLink",
            "invite_link": invite_link,
            "chat_ids": chat_ids,
        }

        return await self.invoke(data)

    async def getChatFolderNewChats(self, chat_folder_id: int) -> Result:
        """Returns new chats added to a shareable chat folder by its owner\. The method must be called at most once in getOption\("chat\_folder\_new\_chats\_update\_period"\) for the given chat folder

        Args:
            chat_folder_id (``int``):
                Chat folder identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatFolderNewChats",
            "chat_folder_id": chat_folder_id,
        }

        return await self.invoke(data)

    async def processChatFolderNewChats(
        self, chat_folder_id: int, added_chat_ids: list
    ) -> Result:
        """Process new chats added to a shareable chat folder by its owner

        Args:
            chat_folder_id (``int``):
                Chat folder identifier

            added_chat_ids (``list``):
                Identifiers of the new chats, which are added to the chat folder\. The chats are automatically joined if they aren't joined yet


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "processChatFolderNewChats",
            "chat_folder_id": chat_folder_id,
            "added_chat_ids": added_chat_ids,
        }

        return await self.invoke(data)

    async def getArchiveChatListSettings(self) -> Result:
        """Returns settings for automatic moving of chats to and from the Archive chat lists


        Returns:
            :class:`~pytdbot.types.Result` (``ArchiveChatListSettings``)
        """

        data = {
            "@type": "getArchiveChatListSettings",
        }

        return await self.invoke(data)

    async def setArchiveChatListSettings(self, settings: dict) -> Result:
        """Changes settings for automatic moving of chats to and from the Archive chat lists

        Args:
            settings (``archiveChatListSettings``):
                New settings


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setArchiveChatListSettings",
            "settings": settings,
        }

        return await self.invoke(data)

    async def setChatTitle(self, chat_id: int, title: str) -> Result:
        """Changes the chat title\. Supported only for basic groups, supergroups and channels\. Requires can\_change\_info administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            title (``str``):
                New title of the chat; 1\-128 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatTitle",
            "chat_id": chat_id,
            "title": title,
        }

        return await self.invoke(data)

    async def setChatPhoto(self, chat_id: int, photo: dict = None) -> Result:
        """Changes the photo of a chat\. Supported only for basic groups, supergroups and channels\. Requires can\_change\_info administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            photo (``InputChatPhoto``, *optional*):
                New chat photo; pass null to delete the chat photo


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatPhoto",
            "chat_id": chat_id,
            "photo": photo,
        }

        return await self.invoke(data)

    async def setChatAccentColor(
        self, chat_id: int, accent_color_id: int, background_custom_emoji_id: int
    ) -> Result:
        """Changes accent color and background custom emoji of a chat\. Supported only for channels with getOption\("channel\_custom\_accent\_color\_boost\_level\_min"\) boost level\. Requires can\_change\_info administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            accent_color_id (``int``):
                Identifier of the accent color to use

            background_custom_emoji_id (``int``):
                Identifier of a custom emoji to be shown on the reply header background; 0 if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatAccentColor",
            "chat_id": chat_id,
            "accent_color_id": accent_color_id,
            "background_custom_emoji_id": background_custom_emoji_id,
        }

        return await self.invoke(data)

    async def setChatMessageAutoDeleteTime(
        self, chat_id: int, message_auto_delete_time: int
    ) -> Result:
        """Changes the message auto\-delete or self\-destruct \(for secret chats\) time in a chat\. Requires change\_info administrator right in basic groups, supergroups and channels Message auto\-delete time can't be changed in a chat with the current user \(Saved Messages\) and the chat 777000 \(Telegram\)\.

        Args:
            chat_id (``int``):
                Chat identifier

            message_auto_delete_time (``int``):
                New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatMessageAutoDeleteTime",
            "chat_id": chat_id,
            "message_auto_delete_time": message_auto_delete_time,
        }

        return await self.invoke(data)

    async def setChatPermissions(self, chat_id: int, permissions: dict) -> Result:
        """Changes the chat members permissions\. Supported only for basic groups and supergroups\. Requires can\_restrict\_members administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            permissions (``chatPermissions``):
                New non\-administrator members permissions in the chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatPermissions",
            "chat_id": chat_id,
            "permissions": permissions,
        }

        return await self.invoke(data)

    async def setChatBackground(
        self,
        chat_id: int,
        dark_theme_dimming: int,
        only_for_self: bool,
        background: dict = None,
        type: dict = None,
    ) -> Result:
        """Sets the background in a specific chat\. Supported only in private and secret chats with non\-deleted users

        Args:
            chat_id (``int``):
                Chat identifier

            dark_theme_dimming (``int``):
                Dimming of the background in dark themes, as a percentage; 0\-100

            only_for_self (``bool``):
                Pass true to set background only for self; pass false to set background for both chat users\. Background can be set for both users only by Telegram Premium users and if set background isn't of the type inputBackgroundPrevious

            background (``InputBackground``, *optional*):
                The input background to use; pass null to create a new filled background

            type (``BackgroundType``, *optional*):
                Background type; pass null to use default background type for the chosen background


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatBackground",
            "chat_id": chat_id,
            "background": background,
            "type": type,
            "dark_theme_dimming": dark_theme_dimming,
            "only_for_self": only_for_self,
        }

        return await self.invoke(data)

    async def deleteChatBackground(
        self, chat_id: int, restore_previous: bool
    ) -> Result:
        """Deletes background in a specific chat

        Args:
            chat_id (``int``):
                Chat identifier

            restore_previous (``bool``):
                Pass true to restore previously set background\. Can be used only in private and secret chats with non\-deleted users if userFullInfo\.set\_chat\_background \=\= true\. Supposed to be used from messageChatSetBackground messages with the currently set background that was set for both sides by the other user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteChatBackground",
            "chat_id": chat_id,
            "restore_previous": restore_previous,
        }

        return await self.invoke(data)

    async def setChatTheme(self, chat_id: int, theme_name: str) -> Result:
        """Changes the chat theme\. Supported only in private and secret chats

        Args:
            chat_id (``int``):
                Chat identifier

            theme_name (``str``):
                Name of the new chat theme; pass an empty string to return the default theme


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatTheme",
            "chat_id": chat_id,
            "theme_name": theme_name,
        }

        return await self.invoke(data)

    async def setChatDraftMessage(
        self, chat_id: int, message_thread_id: int, draft_message: dict = None
    ) -> Result:
        """Changes the draft message in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the draft was changed

            draft_message (``draftMessage``, *optional*):
                New draft message; pass null to remove the draft


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatDraftMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "draft_message": draft_message,
        }

        return await self.invoke(data)

    async def setChatNotificationSettings(
        self, chat_id: int, notification_settings: dict
    ) -> Result:
        """Changes the notification settings of a chat\. Notification settings of a chat with the current user \(Saved Messages\) can't be changed

        Args:
            chat_id (``int``):
                Chat identifier

            notification_settings (``chatNotificationSettings``):
                New notification settings for the chat\. If the chat is muted for more than 366 days, it is considered to be muted forever


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatNotificationSettings",
            "chat_id": chat_id,
            "notification_settings": notification_settings,
        }

        return await self.invoke(data)

    async def toggleChatHasProtectedContent(
        self, chat_id: int, has_protected_content: bool
    ) -> Result:
        """Changes the ability of users to save, forward, or copy chat content\. Supported only for basic groups, supergroups and channels\. Requires owner privileges

        Args:
            chat_id (``int``):
                Chat identifier

            has_protected_content (``bool``):
                New value of has\_protected\_content


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatHasProtectedContent",
            "chat_id": chat_id,
            "has_protected_content": has_protected_content,
        }

        return await self.invoke(data)

    async def toggleChatViewAsTopics(
        self, chat_id: int, view_as_topics: bool
    ) -> Result:
        """Changes the view\_as\_topics setting of a forum chat

        Args:
            chat_id (``int``):
                Chat identifier

            view_as_topics (``bool``):
                New value of view\_as\_topics


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatViewAsTopics",
            "chat_id": chat_id,
            "view_as_topics": view_as_topics,
        }

        return await self.invoke(data)

    async def toggleChatIsTranslatable(
        self, chat_id: int, is_translatable: bool
    ) -> Result:
        """Changes the translatable state of a chat

        Args:
            chat_id (``int``):
                Chat identifier

            is_translatable (``bool``):
                New value of is\_translatable


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatIsTranslatable",
            "chat_id": chat_id,
            "is_translatable": is_translatable,
        }

        return await self.invoke(data)

    async def toggleChatIsMarkedAsUnread(
        self, chat_id: int, is_marked_as_unread: bool
    ) -> Result:
        """Changes the marked as unread state of a chat

        Args:
            chat_id (``int``):
                Chat identifier

            is_marked_as_unread (``bool``):
                New value of is\_marked\_as\_unread


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatIsMarkedAsUnread",
            "chat_id": chat_id,
            "is_marked_as_unread": is_marked_as_unread,
        }

        return await self.invoke(data)

    async def toggleChatDefaultDisableNotification(
        self, chat_id: int, default_disable_notification: bool
    ) -> Result:
        """Changes the value of the default disable\_notification parameter, used when a message is sent to a chat

        Args:
            chat_id (``int``):
                Chat identifier

            default_disable_notification (``bool``):
                New value of default\_disable\_notification


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatDefaultDisableNotification",
            "chat_id": chat_id,
            "default_disable_notification": default_disable_notification,
        }

        return await self.invoke(data)

    async def setChatAvailableReactions(
        self, chat_id: int, available_reactions: dict
    ) -> Result:
        """Changes reactions, available in a chat\. Available for basic groups, supergroups, and channels\. Requires can\_change\_info administrator right

        Args:
            chat_id (``int``):
                Identifier of the chat

            available_reactions (``ChatAvailableReactions``):
                Reactions available in the chat\. All explicitly specified emoji reactions must be active\. Up to the chat's boost level custom emoji reactions can be explicitly specified


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatAvailableReactions",
            "chat_id": chat_id,
            "available_reactions": available_reactions,
        }

        return await self.invoke(data)

    async def setChatClientData(self, chat_id: int, client_data: str) -> Result:
        """Changes application\-specific data associated with a chat

        Args:
            chat_id (``int``):
                Chat identifier

            client_data (``str``):
                New value of client\_data


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatClientData",
            "chat_id": chat_id,
            "client_data": client_data,
        }

        return await self.invoke(data)

    async def setChatDescription(self, chat_id: int, description: str) -> Result:
        """Changes information about a chat\. Available for basic groups, supergroups, and channels\. Requires can\_change\_info administrator right

        Args:
            chat_id (``int``):
                Identifier of the chat

            description (``str``):
                New chat description; 0\-255 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatDescription",
            "chat_id": chat_id,
            "description": description,
        }

        return await self.invoke(data)

    async def setChatDiscussionGroup(
        self, chat_id: int, discussion_chat_id: int
    ) -> Result:
        """Changes the discussion group of a channel chat; requires can\_change\_info administrator right in the channel if it is specified

        Args:
            chat_id (``int``):
                Identifier of the channel chat\. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat \(requires can\_pin\_messages rights in the supergroup\)

            discussion_chat_id (``int``):
                Identifier of a new channel's discussion group\. Use 0 to remove the discussion group\. Use the method getSuitableDiscussionChats to find all suitable groups\. Basic group chats must be first upgraded to supergroup chats\. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatDiscussionGroup",
            "chat_id": chat_id,
            "discussion_chat_id": discussion_chat_id,
        }

        return await self.invoke(data)

    async def setChatLocation(self, chat_id: int, location: dict) -> Result:
        """Changes the location of a chat\. Available only for some location\-based supergroups, use supergroupFullInfo\.can\_set\_location to check whether the method is allowed to use

        Args:
            chat_id (``int``):
                Chat identifier

            location (``chatLocation``):
                New location for the chat; must be valid and not null


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatLocation",
            "chat_id": chat_id,
            "location": location,
        }

        return await self.invoke(data)

    async def setChatSlowModeDelay(self, chat_id: int, slow_mode_delay: int) -> Result:
        """Changes the slow mode delay of a chat\. Available only for supergroups; requires can\_restrict\_members rights

        Args:
            chat_id (``int``):
                Chat identifier

            slow_mode_delay (``int``):
                New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatSlowModeDelay",
            "chat_id": chat_id,
            "slow_mode_delay": slow_mode_delay,
        }

        return await self.invoke(data)

    async def pinChatMessage(
        self,
        chat_id: int,
        message_id: int,
        disable_notification: bool,
        only_for_self: bool,
    ) -> Result:
        """Pins a message in a chat; requires can\_pin\_messages rights or can\_edit\_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_id (``int``):
                Identifier of the new pinned message

            disable_notification (``bool``):
                Pass true to disable notification about the pinned message\. Notifications are always disabled in channels and private chats

            only_for_self (``bool``):
                Pass true to pin the message only for self; private chats only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "pinChatMessage",
            "chat_id": chat_id,
            "message_id": message_id,
            "disable_notification": disable_notification,
            "only_for_self": only_for_self,
        }

        return await self.invoke(data)

    async def unpinChatMessage(self, chat_id: int, message_id: int) -> Result:
        """Removes a pinned message from a chat; requires can\_pin\_messages rights in the group or can\_edit\_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_id (``int``):
                Identifier of the removed pinned message


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "unpinChatMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def unpinAllChatMessages(self, chat_id: int) -> Result:
        """Removes all pinned messages from a chat; requires can\_pin\_messages rights in the group or can\_edit\_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "unpinAllChatMessages",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def unpinAllMessageThreadMessages(
        self, chat_id: int, message_thread_id: int
    ) -> Result:
        """Removes all pinned messages from a forum topic; requires can\_pin\_messages rights in the supergroup

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_thread_id (``int``):
                Message thread identifier in which messages will be unpinned


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "unpinAllMessageThreadMessages",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data)

    async def joinChat(self, chat_id: int) -> Result:
        """Adds the current user as a new member to a chat\. Private and secret chats can't be joined using this method\. May return an error with a message "INVITE\_REQUEST\_SENT" if only a join request was created

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "joinChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def leaveChat(self, chat_id: int) -> Result:
        """Removes the current user from chat members\. Private and secret chats can't be left using this method

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "leaveChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def addChatMember(
        self, chat_id: int, user_id: int, forward_limit: int
    ) -> Result:
        """Adds a new member to a chat\. Members can't be added to private or secret chats

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user

            forward_limit (``int``):
                The number of earlier messages from the chat to be forwarded to the new member; up to 100\. Ignored for supergroups and channels, or if the added user is a bot


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addChatMember",
            "chat_id": chat_id,
            "user_id": user_id,
            "forward_limit": forward_limit,
        }

        return await self.invoke(data)

    async def addChatMembers(self, chat_id: int, user_ids: list) -> Result:
        """Adds multiple new members to a chat\. Currently, this method is only available for supergroups and channels\. This method can't be used to join a chat\. Members can't be added to a channel if it has more than 200 members

        Args:
            chat_id (``int``):
                Chat identifier

            user_ids (``list``):
                Identifiers of the users to be added to the chat\. The maximum number of added users is 20 for supergroups and 100 for channels


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addChatMembers",
            "chat_id": chat_id,
            "user_ids": user_ids,
        }

        return await self.invoke(data)

    async def setChatMemberStatus(
        self, chat_id: int, member_id: dict, status: dict
    ) -> Result:
        """Changes the status of a chat member, needs appropriate privileges\. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead\. Use addChatMember or banChatMember if some additional parameters needs to be passed

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``MessageSender``):
                Member identifier\. Chats can be only banned and unbanned in supergroups and channels

            status (``ChatMemberStatus``):
                The new status of the member in the chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatMemberStatus",
            "chat_id": chat_id,
            "member_id": member_id,
            "status": status,
        }

        return await self.invoke(data)

    async def banChatMember(
        self,
        chat_id: int,
        member_id: dict,
        banned_until_date: int,
        revoke_messages: bool,
    ) -> Result:
        """Bans a member in a chat\. Members can't be banned in private or secret chats\. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc\., unless unbanned first

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``MessageSender``):
                Member identifier

            banned_until_date (``int``):
                Point in time \(Unix timestamp\) when the user will be unbanned; 0 if never\. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever\. Ignored in basic groups and if a chat is banned

            revoke_messages (``bool``):
                Pass true to delete all messages in the chat for the user that is being removed\. Always true for supergroups and channels


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "banChatMember",
            "chat_id": chat_id,
            "member_id": member_id,
            "banned_until_date": banned_until_date,
            "revoke_messages": revoke_messages,
        }

        return await self.invoke(data)

    async def canTransferOwnership(self) -> Result:
        """Checks whether the current session can be used to transfer a chat ownership to another user


        Returns:
            :class:`~pytdbot.types.Result` (``CanTransferOwnershipResult``)
        """

        data = {
            "@type": "canTransferOwnership",
        }

        return await self.invoke(data)

    async def transferChatOwnership(
        self, chat_id: int, user_id: int, password: str
    ) -> Result:
        """Changes the owner of a chat\. The current user must be a current owner of the chat\. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session\. Available only for supergroups and channel chats

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user to which transfer the ownership\. The ownership can't be transferred to a bot or to a deleted user

            password (``str``):
                The 2\-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "transferChatOwnership",
            "chat_id": chat_id,
            "user_id": user_id,
            "password": password,
        }

        return await self.invoke(data)

    async def getChatMember(self, chat_id: int, member_id: dict) -> Result:
        """Returns information about a single member of a chat

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``MessageSender``):
                Member identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatMember``)
        """

        data = {
            "@type": "getChatMember",
            "chat_id": chat_id,
            "member_id": member_id,
        }

        return await self.invoke(data)

    async def searchChatMembers(
        self, chat_id: int, query: str, limit: int, filter: dict = None
    ) -> Result:
        """Searches for a specified query in the first name, last name and usernames of the members of a specified chat\. Requires administrator rights in channels

        Args:
            chat_id (``int``):
                Chat identifier

            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of users to be returned; up to 200

            filter (``ChatMembersFilter``, *optional*):
                The type of users to search for; pass null to search among all chat members


        Returns:
            :class:`~pytdbot.types.Result` (``ChatMembers``)
        """

        data = {
            "@type": "searchChatMembers",
            "chat_id": chat_id,
            "query": query,
            "limit": limit,
            "filter": filter,
        }

        return await self.invoke(data)

    async def getChatAdministrators(self, chat_id: int) -> Result:
        """Returns a list of administrators of the chat with their custom titles

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatAdministrators``)
        """

        data = {
            "@type": "getChatAdministrators",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def clearAllDraftMessages(self, exclude_secret_chats: bool) -> Result:
        """Clears message drafts in all chats

        Args:
            exclude_secret_chats (``bool``):
                Pass true to keep local message drafts in secret chats


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearAllDraftMessages",
            "exclude_secret_chats": exclude_secret_chats,
        }

        return await self.invoke(data)

    async def getSavedNotificationSound(self, notification_sound_id: int) -> Result:
        """Returns saved notification sound by its identifier\. Returns a 404 error if there is no saved notification sound with the specified identifier

        Args:
            notification_sound_id (``int``):
                Identifier of the notification sound


        Returns:
            :class:`~pytdbot.types.Result` (``NotificationSounds``)
        """

        data = {
            "@type": "getSavedNotificationSound",
            "notification_sound_id": notification_sound_id,
        }

        return await self.invoke(data)

    async def getSavedNotificationSounds(self) -> Result:
        """Returns list of saved notification sounds\. If a sound isn't in the list, then default sound needs to be used


        Returns:
            :class:`~pytdbot.types.Result` (``NotificationSounds``)
        """

        data = {
            "@type": "getSavedNotificationSounds",
        }

        return await self.invoke(data)

    async def addSavedNotificationSound(self, sound: dict) -> Result:
        """Adds a new notification sound to the list of saved notification sounds\. The new notification sound is added to the top of the list\. If it is already in the list, its position isn't changed

        Args:
            sound (``InputFile``):
                Notification sound file to add


        Returns:
            :class:`~pytdbot.types.Result` (``NotificationSound``)
        """

        data = {
            "@type": "addSavedNotificationSound",
            "sound": sound,
        }

        return await self.invoke(data)

    async def removeSavedNotificationSound(self, notification_sound_id: int) -> Result:
        """Removes a notification sound from the list of saved notification sounds

        Args:
            notification_sound_id (``int``):
                Identifier of the notification sound


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeSavedNotificationSound",
            "notification_sound_id": notification_sound_id,
        }

        return await self.invoke(data)

    async def getChatNotificationSettingsExceptions(
        self, compare_sound: bool, scope: dict = None
    ) -> Result:
        """Returns list of chats with non\-default notification settings for new messages

        Args:
            compare_sound (``bool``):
                Pass true to include in the response chats with only non\-default sound

            scope (``NotificationSettingsScope``, *optional*):
                If specified, only chats from the scope will be returned; pass null to return chats from all scopes


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatNotificationSettingsExceptions",
            "scope": scope,
            "compare_sound": compare_sound,
        }

        return await self.invoke(data)

    async def getScopeNotificationSettings(self, scope: dict) -> Result:
        """Returns the notification settings for chats of a given type

        Args:
            scope (``NotificationSettingsScope``):
                Types of chats for which to return the notification settings information


        Returns:
            :class:`~pytdbot.types.Result` (``ScopeNotificationSettings``)
        """

        data = {
            "@type": "getScopeNotificationSettings",
            "scope": scope,
        }

        return await self.invoke(data)

    async def setScopeNotificationSettings(
        self, scope: dict, notification_settings: dict
    ) -> Result:
        """Changes notification settings for chats of a given type

        Args:
            scope (``NotificationSettingsScope``):
                Types of chats for which to change the notification settings

            notification_settings (``scopeNotificationSettings``):
                The new notification settings for the given scope


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setScopeNotificationSettings",
            "scope": scope,
            "notification_settings": notification_settings,
        }

        return await self.invoke(data)

    async def resetAllNotificationSettings(self) -> Result:
        """Resets all notification settings to their default values\. By default, all chats are unmuted and message previews are shown


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "resetAllNotificationSettings",
        }

        return await self.invoke(data)

    async def toggleChatIsPinned(
        self, chat_list: dict, chat_id: int, is_pinned: bool
    ) -> Result:
        """Changes the pinned state of a chat\. There can be up to getOption\("pinned\_chat\_count\_max"\)/getOption\("pinned\_archived\_chat\_count\_max"\) pinned non\-secret chats and the same number of secret chats in the main/archive chat list\. The limit can be increased with Telegram Premium

        Args:
            chat_list (``ChatList``):
                Chat list in which to change the pinned state of the chat

            chat_id (``int``):
                Chat identifier

            is_pinned (``bool``):
                Pass true to pin the chat; pass false to unpin it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleChatIsPinned",
            "chat_list": chat_list,
            "chat_id": chat_id,
            "is_pinned": is_pinned,
        }

        return await self.invoke(data)

    async def setPinnedChats(self, chat_list: dict, chat_ids: list) -> Result:
        """Changes the order of pinned chats

        Args:
            chat_list (``ChatList``):
                Chat list in which to change the order of pinned chats

            chat_ids (``list``):
                The new list of pinned chats


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setPinnedChats",
            "chat_list": chat_list,
            "chat_ids": chat_ids,
        }

        return await self.invoke(data)

    async def readChatList(self, chat_list: dict) -> Result:
        """Traverse all chats in a chat list and marks all messages in the chats as read

        Args:
            chat_list (``ChatList``):
                Chat list in which to mark all chats as read


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "readChatList",
            "chat_list": chat_list,
        }

        return await self.invoke(data)

    async def getStory(
        self, story_sender_chat_id: int, story_id: int, only_local: bool
    ) -> Result:
        """Returns a story

        Args:
            story_sender_chat_id (``int``):
                Identifier of the chat that posted the story

            story_id (``int``):
                Story identifier

            only_local (``bool``):
                Pass true to get only locally available information without sending network requests


        Returns:
            :class:`~pytdbot.types.Result` (``Story``)
        """

        data = {
            "@type": "getStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "only_local": only_local,
        }

        return await self.invoke(data)

    async def getChatsToSendStories(self) -> Result:
        """Returns channel chats in which the current user has the right to post stories\. The chats must be rechecked with canSendStory before actually trying to post a story there


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getChatsToSendStories",
        }

        return await self.invoke(data)

    async def canSendStory(self, chat_id: int) -> Result:
        """Checks whether the current user can send a story on behalf of a chat; requires can\_post\_stories rights for channel chats

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``CanSendStoryResult``)
        """

        data = {
            "@type": "canSendStory",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def sendStory(
        self,
        chat_id: int,
        content: dict,
        privacy_settings: dict,
        active_period: int,
        from_story_full_id: dict,
        is_pinned: bool,
        protect_content: bool,
        areas: dict = None,
        caption: dict = None,
    ) -> Result:
        """Sends a new story to a chat; requires can\_post\_stories rights for channel chats\. Returns a temporary story

        Args:
            chat_id (``int``):
                Identifier of the chat that will post the story

            content (``InputStoryContent``):
                Content of the story

            privacy_settings (``StoryPrivacySettings``):
                The privacy settings for the story

            active_period (``int``):
                Period after which the story is moved to archive, in seconds; must be one of 6 \* 3600, 12 \* 3600, 86400, or 2 \* 86400 for Telegram Premium users, and 86400 otherwise

            from_story_full_id (``storyFullId``):
                Full identifier of the original story, which content was used to create the story

            is_pinned (``bool``):
                Pass true to keep the story accessible after expiration

            protect_content (``bool``):
                Pass true if the content of the story must be protected from forwarding and screenshotting

            areas (``inputStoryAreas``, *optional*):
                Clickable rectangle areas to be shown on the story media; pass null if none

            caption (``formattedText``, *optional*):
                Story caption; pass null to use an empty caption; 0\-getOption\("story\_caption\_length\_max"\) characters


        Returns:
            :class:`~pytdbot.types.Result` (``Story``)
        """

        data = {
            "@type": "sendStory",
            "chat_id": chat_id,
            "content": content,
            "areas": areas,
            "caption": caption,
            "privacy_settings": privacy_settings,
            "active_period": active_period,
            "from_story_full_id": from_story_full_id,
            "is_pinned": is_pinned,
            "protect_content": protect_content,
        }

        return await self.invoke(data)

    async def editStory(
        self,
        story_sender_chat_id: int,
        story_id: int,
        content: dict = None,
        areas: dict = None,
        caption: dict = None,
    ) -> Result:
        """Changes content and caption of a story\. Can be called only if story\.can\_be\_edited \=\= true

        Args:
            story_sender_chat_id (``int``):
                Identifier of the chat that posted the story

            story_id (``int``):
                Identifier of the story to edit

            content (``InputStoryContent``, *optional*):
                New content of the story; pass null to keep the current content

            areas (``inputStoryAreas``, *optional*):
                New clickable rectangle areas to be shown on the story media; pass null to keep the current areas\. Areas can't be edited if story content isn't changed

            caption (``formattedText``, *optional*):
                New story caption; pass null to keep the current caption


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "content": content,
            "areas": areas,
            "caption": caption,
        }

        return await self.invoke(data)

    async def setStoryPrivacySettings(
        self, story_sender_chat_id: int, story_id: int, privacy_settings: dict
    ) -> Result:
        """Changes privacy settings of a story\. Can be called only if story\.can\_be\_edited \=\= true

        Args:
            story_sender_chat_id (``int``):
                Identifier of the chat that posted the story

            story_id (``int``):
                Identifier of the story

            privacy_settings (``StoryPrivacySettings``):
                The new privacy settigs for the story


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStoryPrivacySettings",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "privacy_settings": privacy_settings,
        }

        return await self.invoke(data)

    async def toggleStoryIsPinned(
        self, story_sender_chat_id: int, story_id: int, is_pinned: bool
    ) -> Result:
        """Toggles whether a story is accessible after expiration\. Can be called only if story\.can\_toggle\_is\_pinned \=\= true

        Args:
            story_sender_chat_id (``int``):
                Identifier of the chat that posted the story

            story_id (``int``):
                Identifier of the story

            is_pinned (``bool``):
                Pass true to make the story accessible after expiration; pass false to make it private


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleStoryIsPinned",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "is_pinned": is_pinned,
        }

        return await self.invoke(data)

    async def deleteStory(self, story_sender_chat_id: int, story_id: int) -> Result:
        """Deletes a previously sent story\. Can be called only if story\.can\_be\_deleted \=\= true

        Args:
            story_sender_chat_id (``int``):
                Identifier of the chat that posted the story

            story_id (``int``):
                Identifier of the story to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
        }

        return await self.invoke(data)

    async def getStoryNotificationSettingsExceptions(self) -> Result:
        """Returns list of chats with non\-default notification settings for stories


        Returns:
            :class:`~pytdbot.types.Result` (``Chats``)
        """

        data = {
            "@type": "getStoryNotificationSettingsExceptions",
        }

        return await self.invoke(data)

    async def loadActiveStories(self, story_list: dict) -> Result:
        """Loads more active stories from a story list\. The loaded stories will be sent through updates\. Active stories are sorted by the pair \(active\_stories\.order, active\_stories\.story\_sender\_chat\_id\) in descending order\. Returns a 404 error if all active stories have been loaded

        Args:
            story_list (``StoryList``):
                The story list in which to load active stories


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "loadActiveStories",
            "story_list": story_list,
        }

        return await self.invoke(data)

    async def setChatActiveStoriesList(self, chat_id: int, story_list: dict) -> Result:
        """Changes story list in which stories from the chat are shown

        Args:
            chat_id (``int``):
                Identifier of the chat that posted stories

            story_list (``StoryList``):
                New list for active stories posted by the chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setChatActiveStoriesList",
            "chat_id": chat_id,
            "story_list": story_list,
        }

        return await self.invoke(data)

    async def getChatActiveStories(self, chat_id: int) -> Result:
        """Returns the list of active stories posted by the given chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatActiveStories``)
        """

        data = {
            "@type": "getChatActiveStories",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatPinnedStories(
        self, chat_id: int, from_story_id: int, limit: int
    ) -> Result:
        """Returns the list of pinned stories posted by the given chat\. The stories are returned in a reverse chronological order \(i\.e\., in order of decreasing story\_id\)\. For optimal performance, the number of returned stories is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier

            from_story_id (``int``):
                Identifier of the story starting from which stories must be returned; use 0 to get results from the last story

            limit (``int``):
                The maximum number of stories to be returned For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``Stories``)
        """

        data = {
            "@type": "getChatPinnedStories",
            "chat_id": chat_id,
            "from_story_id": from_story_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getChatArchivedStories(
        self, chat_id: int, from_story_id: int, limit: int
    ) -> Result:
        """Returns the list of all stories posted by the given chat; requires can\_edit\_stories rights for channel chats\. The stories are returned in a reverse chronological order \(i\.e\., in order of decreasing story\_id\)\. For optimal performance, the number of returned stories is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier

            from_story_id (``int``):
                Identifier of the story starting from which stories must be returned; use 0 to get results from the last story

            limit (``int``):
                The maximum number of stories to be returned For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``Stories``)
        """

        data = {
            "@type": "getChatArchivedStories",
            "chat_id": chat_id,
            "from_story_id": from_story_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def openStory(self, story_sender_chat_id: int, story_id: int) -> Result:
        """Informs TDLib that a story is opened and is being viewed by the user

        Args:
            story_sender_chat_id (``int``):
                The identifier of the sender of the opened story

            story_id (``int``):
                The identifier of the story


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "openStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
        }

        return await self.invoke(data)

    async def closeStory(self, story_sender_chat_id: int, story_id: int) -> Result:
        """Informs TDLib that a story is closed by the user

        Args:
            story_sender_chat_id (``int``):
                The identifier of the sender of the story to close

            story_id (``int``):
                The identifier of the story


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "closeStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
        }

        return await self.invoke(data)

    async def getStoryAvailableReactions(self, row_size: int) -> Result:
        """Returns reactions, which can be chosen for a story

        Args:
            row_size (``int``):
                Number of reaction per row, 5\-25


        Returns:
            :class:`~pytdbot.types.Result` (``AvailableReactions``)
        """

        data = {
            "@type": "getStoryAvailableReactions",
            "row_size": row_size,
        }

        return await self.invoke(data)

    async def setStoryReaction(
        self,
        story_sender_chat_id: int,
        story_id: int,
        update_recent_reactions: bool,
        reaction_type: dict = None,
    ) -> Result:
        """Changes chosen reaction on a story

        Args:
            story_sender_chat_id (``int``):
                The identifier of the sender of the story

            story_id (``int``):
                The identifier of the story

            update_recent_reactions (``bool``):
                Pass true if the reaction needs to be added to recent reactions

            reaction_type (``ReactionType``, *optional*):
                Type of the reaction to set; pass null to remove the reaction\. \`reactionTypeCustomEmoji\` reactions can be used only by Telegram Premium users


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStoryReaction",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "reaction_type": reaction_type,
            "update_recent_reactions": update_recent_reactions,
        }

        return await self.invoke(data)

    async def getStoryViewers(
        self,
        story_id: int,
        only_contacts: bool,
        prefer_with_reaction: bool,
        offset: str,
        limit: int,
        query: str = None,
    ) -> Result:
        """Returns viewers of a story\. The method can be called only for stories posted on behalf of the current user

        Args:
            story_id (``int``):
                Story identifier

            only_contacts (``bool``):
                Pass true to get only contacts; pass false to get all relevant viewers

            prefer_with_reaction (``bool``):
                Pass true to get viewers with reaction first; pass false to get viewers sorted just by view\_date

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of story viewers to return

            query (``str``, *optional*):
                Query to search for in names and usernames of the viewers; may be empty to get all relevant viewers


        Returns:
            :class:`~pytdbot.types.Result` (``StoryViewers``)
        """

        data = {
            "@type": "getStoryViewers",
            "story_id": story_id,
            "query": query,
            "only_contacts": only_contacts,
            "prefer_with_reaction": prefer_with_reaction,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def reportStory(
        self, story_sender_chat_id: int, story_id: int, reason: dict, text: str
    ) -> Result:
        """Reports a story to the Telegram moderators

        Args:
            story_sender_chat_id (``int``):
                The identifier of the sender of the story to report

            story_id (``int``):
                The identifier of the story to report

            reason (``ReportReason``):
                The reason for reporting the story

            text (``str``):
                Additional report details; 0\-1024 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportStory",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "reason": reason,
            "text": text,
        }

        return await self.invoke(data)

    async def activateStoryStealthMode(self) -> Result:
        """Activates stealth mode for stories, which hides all views of stories from the current user in the last "story\_stealth\_mode\_past\_period" seconds and for the next "story\_stealth\_mode\_future\_period" seconds; for Telegram Premium users only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "activateStoryStealthMode",
        }

        return await self.invoke(data)

    async def getStoryPublicForwards(
        self, story_sender_chat_id: int, story_id: int, offset: str, limit: int
    ) -> Result:
        """Returns forwards of a story as a message to public chats and reposts by public channels\. Can be used only if the story is posted on behalf of the current user or story\.can\_get\_statistics \=\= true\. For optimal performance, the number of returned messages and stories is chosen by TDLib

        Args:
            story_sender_chat_id (``int``):
                The identifier of the sender of the story

            story_id (``int``):
                The identifier of the story

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages and stories to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``StoryPublicForwards``)
        """

        data = {
            "@type": "getStoryPublicForwards",
            "story_sender_chat_id": story_sender_chat_id,
            "story_id": story_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getAvailableChatBoostSlots(self) -> Result:
        """Returns the list of available chat boost slots for the current user


        Returns:
            :class:`~pytdbot.types.Result` (``ChatBoostSlots``)
        """

        data = {
            "@type": "getAvailableChatBoostSlots",
        }

        return await self.invoke(data)

    async def getChatBoostStatus(self, chat_id: int) -> Result:
        """Returns the current boost status for a channel chat

        Args:
            chat_id (``int``):
                Identifier of the channel chat


        Returns:
            :class:`~pytdbot.types.Result` (``ChatBoostStatus``)
        """

        data = {
            "@type": "getChatBoostStatus",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def boostChat(self, chat_id: int, slot_ids: list) -> Result:
        """Boosts a chat and returns the list of available chat boost slots for the current user after the boost

        Args:
            chat_id (``int``):
                Identifier of the chat

            slot_ids (``list``):
                Identifiers of boost slots of the current user from which to apply boosts to the chat


        Returns:
            :class:`~pytdbot.types.Result` (``ChatBoostSlots``)
        """

        data = {
            "@type": "boostChat",
            "chat_id": chat_id,
            "slot_ids": slot_ids,
        }

        return await self.invoke(data)

    async def getChatBoostLink(self, chat_id: int) -> Result:
        """Returns an HTTPS link to boost the specified channel chat

        Args:
            chat_id (``int``):
                Identifier of the chat


        Returns:
            :class:`~pytdbot.types.Result` (``ChatBoostLink``)
        """

        data = {
            "@type": "getChatBoostLink",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatBoostLinkInfo(self, url: str) -> Result:
        """Returns information about a link to boost a chat\. Can be called for any internal link of the type internalLinkTypeChatBoost

        Args:
            url (``str``):
                The link to boost a chat


        Returns:
            :class:`~pytdbot.types.Result` (``ChatBoostLinkInfo``)
        """

        data = {
            "@type": "getChatBoostLinkInfo",
            "url": url,
        }

        return await self.invoke(data)

    async def getChatBoosts(
        self, chat_id: int, only_gift_codes: bool, offset: str, limit: int
    ) -> Result:
        """Returns list of boosts applied to a chat; requires administrator rights in the channel chat

        Args:
            chat_id (``int``):
                Identifier of the chat

            only_gift_codes (``bool``):
                Pass true to receive only boosts received from gift codes and giveaways created by the chat

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of boosts to be returned; up to 100\. For optimal performance, the number of returned boosts can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``FoundChatBoosts``)
        """

        data = {
            "@type": "getChatBoosts",
            "chat_id": chat_id,
            "only_gift_codes": only_gift_codes,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getUserChatBoosts(self, chat_id: int, user_id: int) -> Result:
        """Returns list of boosts applied to a chat by a given user; requires administrator rights in the channel chat; for bots only

        Args:
            chat_id (``int``):
                Identifier of the chat

            user_id (``int``):
                Identifier of the user


        Returns:
            :class:`~pytdbot.types.Result` (``FoundChatBoosts``)
        """

        data = {
            "@type": "getUserChatBoosts",
            "chat_id": chat_id,
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def getAttachmentMenuBot(self, bot_user_id: int) -> Result:
        """Returns information about a bot that can be added to attachment or side menu

        Args:
            bot_user_id (``int``):
                Bot's user identifier


        Returns:
            :class:`~pytdbot.types.Result` (``AttachmentMenuBot``)
        """

        data = {
            "@type": "getAttachmentMenuBot",
            "bot_user_id": bot_user_id,
        }

        return await self.invoke(data)

    async def toggleBotIsAddedToAttachmentMenu(
        self, bot_user_id: int, is_added: bool, allow_write_access: bool
    ) -> Result:
        """Adds or removes a bot to attachment and side menu\. Bot can be added to the menu, only if userTypeBot\.can\_be\_added\_to\_attachment\_menu \=\= true

        Args:
            bot_user_id (``int``):
                Bot's user identifier

            is_added (``bool``):
                Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu

            allow_write_access (``bool``):
                Pass true if the current user allowed the bot to send them messages\. Ignored if is\_added is false


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleBotIsAddedToAttachmentMenu",
            "bot_user_id": bot_user_id,
            "is_added": is_added,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data)

    async def getThemedEmojiStatuses(self) -> Result:
        """Returns up to 8 emoji statuses, which must be shown right after the default Premium Badge in the emoji status list


        Returns:
            :class:`~pytdbot.types.Result` (``EmojiStatuses``)
        """

        data = {
            "@type": "getThemedEmojiStatuses",
        }

        return await self.invoke(data)

    async def getRecentEmojiStatuses(self) -> Result:
        """Returns recent emoji statuses


        Returns:
            :class:`~pytdbot.types.Result` (``EmojiStatuses``)
        """

        data = {
            "@type": "getRecentEmojiStatuses",
        }

        return await self.invoke(data)

    async def getDefaultEmojiStatuses(self) -> Result:
        """Returns default emoji statuses


        Returns:
            :class:`~pytdbot.types.Result` (``EmojiStatuses``)
        """

        data = {
            "@type": "getDefaultEmojiStatuses",
        }

        return await self.invoke(data)

    async def clearRecentEmojiStatuses(self) -> Result:
        """Clears the list of recently used emoji statuses


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearRecentEmojiStatuses",
        }

        return await self.invoke(data)

    async def downloadFile(
        self, file_id: int, priority: int, offset: int, limit: int, synchronous: bool
    ) -> Result:
        """Downloads a file from the cloud\. Download progress and completion of the download will be notified through updateFile updates

        Args:
            file_id (``int``):
                Identifier of the file to download

            priority (``int``):
                Priority of the download \(1\-32\)\. The higher the priority, the earlier the file will be downloaded\. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first

            offset (``int``):
                The starting position from which the file needs to be downloaded

            limit (``int``):
                Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit

            synchronous (``bool``):
                Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "downloadFile",
            "file_id": file_id,
            "priority": priority,
            "offset": offset,
            "limit": limit,
            "synchronous": synchronous,
        }

        return await self.invoke(data)

    async def getFileDownloadedPrefixSize(self, file_id: int, offset: int) -> Result:
        """Returns file downloaded prefix size from a given offset, in bytes

        Args:
            file_id (``int``):
                Identifier of the file

            offset (``int``):
                Offset from which downloaded prefix size needs to be calculated


        Returns:
            :class:`~pytdbot.types.Result` (``FileDownloadedPrefixSize``)
        """

        data = {
            "@type": "getFileDownloadedPrefixSize",
            "file_id": file_id,
            "offset": offset,
        }

        return await self.invoke(data)

    async def cancelDownloadFile(self, file_id: int, only_if_pending: bool) -> Result:
        """Stops the downloading of a file\. If a file has already been downloaded, does nothing

        Args:
            file_id (``int``):
                Identifier of a file to stop downloading

            only_if_pending (``bool``):
                Pass true to stop downloading only if it hasn't been started, i\.e\. request hasn't been sent to server


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "cancelDownloadFile",
            "file_id": file_id,
            "only_if_pending": only_if_pending,
        }

        return await self.invoke(data)

    async def getSuggestedFileName(self, file_id: int, directory: str) -> Result:
        """Returns suggested name for saving a file in a given directory

        Args:
            file_id (``int``):
                Identifier of the file

            directory (``str``):
                Directory in which the file is supposed to be saved


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getSuggestedFileName",
            "file_id": file_id,
            "directory": directory,
        }

        return await self.invoke(data)

    async def preliminaryUploadFile(
        self, file: dict, priority: int, file_type: dict = None
    ) -> Result:
        """Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes\. Updates updateFile will be used to notify about upload progress and successful completion of the upload\. The file will not have a persistent remote identifier until it is sent in a message

        Args:
            file (``InputFile``):
                File to upload

            priority (``int``):
                Priority of the upload \(1\-32\)\. The higher the priority, the earlier the file will be uploaded\. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first

            file_type (``FileType``, *optional*):
                File type; pass null if unknown


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "preliminaryUploadFile",
            "file": file,
            "file_type": file_type,
            "priority": priority,
        }

        return await self.invoke(data)

    async def cancelPreliminaryUploadFile(self, file_id: int) -> Result:
        """Stops the preliminary uploading of a file\. Supported only for files uploaded by using preliminaryUploadFile\. For other files the behavior is undefined

        Args:
            file_id (``int``):
                Identifier of the file to stop uploading


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "cancelPreliminaryUploadFile",
            "file_id": file_id,
        }

        return await self.invoke(data)

    async def writeGeneratedFilePart(
        self, generation_id: int, offset: int, data: bytes
    ) -> Result:
        """Writes a part of a generated file\. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

        Args:
            generation_id (``int``):
                The identifier of the generation process

            offset (``int``):
                The offset from which to write the data to the file

            data (``bytes``):
                The data to write


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "writeGeneratedFilePart",
            "generation_id": generation_id,
            "offset": offset,
            "data": data,
        }

        return await self.invoke(data)

    async def setFileGenerationProgress(
        self, generation_id: int, expected_size: int, local_prefix_size: int
    ) -> Result:
        """Informs TDLib on a file generation progress

        Args:
            generation_id (``int``):
                The identifier of the generation process

            expected_size (``int``):
                Expected size of the generated file, in bytes; 0 if unknown

            local_prefix_size (``int``):
                The number of bytes already generated


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setFileGenerationProgress",
            "generation_id": generation_id,
            "expected_size": expected_size,
            "local_prefix_size": local_prefix_size,
        }

        return await self.invoke(data)

    async def finishFileGeneration(
        self, generation_id: int, error: dict = None
    ) -> Result:
        """Finishes the file generation

        Args:
            generation_id (``int``):
                The identifier of the generation process

            error (``error``, *optional*):
                If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "finishFileGeneration",
            "generation_id": generation_id,
            "error": error,
        }

        return await self.invoke(data)

    async def readFilePart(self, file_id: int, offset: int, count: int) -> Result:
        """Reads a part of a file from the TDLib file cache and returns read bytes\. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

        Args:
            file_id (``int``):
                Identifier of the file\. The file must be located in the TDLib file cache

            offset (``int``):
                The offset from which to read the file

            count (``int``):
                Number of bytes to read\. An error will be returned if there are not enough bytes available in the file from the specified position\. Pass 0 to read all available data from the specified position


        Returns:
            :class:`~pytdbot.types.Result` (``FilePart``)
        """

        data = {
            "@type": "readFilePart",
            "file_id": file_id,
            "offset": offset,
            "count": count,
        }

        return await self.invoke(data)

    async def deleteFile(self, file_id: int) -> Result:
        """Deletes a file from the TDLib file cache

        Args:
            file_id (``int``):
                Identifier of the file to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteFile",
            "file_id": file_id,
        }

        return await self.invoke(data)

    async def addFileToDownloads(
        self, file_id: int, chat_id: int, message_id: int, priority: int
    ) -> Result:
        """Adds a file from a message to the list of file downloads\. Download progress and completion of the download will be notified through updateFile updates\. If message database is used, the list of file downloads is persistent across application restarts\. The downloading is independent from download using downloadFile, i\.e\. it continues if downloadFile is canceled or is used to download a part of the file

        Args:
            file_id (``int``):
                Identifier of the file to download

            chat_id (``int``):
                Chat identifier of the message with the file

            message_id (``int``):
                Message identifier

            priority (``int``):
                Priority of the download \(1\-32\)\. The higher the priority, the earlier the file will be downloaded\. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "addFileToDownloads",
            "file_id": file_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "priority": priority,
        }

        return await self.invoke(data)

    async def toggleDownloadIsPaused(self, file_id: int, is_paused: bool) -> Result:
        """Changes pause state of a file in the file download list

        Args:
            file_id (``int``):
                Identifier of the downloaded file

            is_paused (``bool``):
                Pass true if the download is paused


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleDownloadIsPaused",
            "file_id": file_id,
            "is_paused": is_paused,
        }

        return await self.invoke(data)

    async def toggleAllDownloadsArePaused(self, are_paused: bool) -> Result:
        """Changes pause state of all files in the file download list

        Args:
            are_paused (``bool``):
                Pass true to pause all downloads; pass false to unpause them


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleAllDownloadsArePaused",
            "are_paused": are_paused,
        }

        return await self.invoke(data)

    async def removeFileFromDownloads(
        self, file_id: int, delete_from_cache: bool
    ) -> Result:
        """Removes a file from the file download list

        Args:
            file_id (``int``):
                Identifier of the downloaded file

            delete_from_cache (``bool``):
                Pass true to delete the file from the TDLib file cache


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeFileFromDownloads",
            "file_id": file_id,
            "delete_from_cache": delete_from_cache,
        }

        return await self.invoke(data)

    async def removeAllFilesFromDownloads(
        self, only_active: bool, only_completed: bool, delete_from_cache: bool
    ) -> Result:
        """Removes all files from the file download list

        Args:
            only_active (``bool``):
                Pass true to remove only active downloads, including paused

            only_completed (``bool``):
                Pass true to remove only completed downloads

            delete_from_cache (``bool``):
                Pass true to delete the file from the TDLib file cache


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeAllFilesFromDownloads",
            "only_active": only_active,
            "only_completed": only_completed,
            "delete_from_cache": delete_from_cache,
        }

        return await self.invoke(data)

    async def searchFileDownloads(
        self,
        only_active: bool,
        only_completed: bool,
        offset: str,
        limit: int,
        query: str = None,
    ) -> Result:
        """Searches for files in the file download list or recently downloaded files from the list

        Args:
            only_active (``bool``):
                Pass true to search only for active downloads, including paused

            only_completed (``bool``):
                Pass true to search only for completed downloads

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of files to be returned

            query (``str``, *optional*):
                Query to search for; may be empty to return all downloaded files


        Returns:
            :class:`~pytdbot.types.Result` (``FoundFileDownloads``)
        """

        data = {
            "@type": "searchFileDownloads",
            "query": query,
            "only_active": only_active,
            "only_completed": only_completed,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getMessageFileType(self, message_file_head: str) -> Result:
        """Returns information about a file with messages exported from another application

        Args:
            message_file_head (``str``):
                Beginning of the message file; up to 100 first lines


        Returns:
            :class:`~pytdbot.types.Result` (``MessageFileType``)
        """

        data = {
            "@type": "getMessageFileType",
            "message_file_head": message_file_head,
        }

        return await self.invoke(data)

    async def getMessageImportConfirmationText(self, chat_id: int) -> Result:
        """Returns a confirmation text to be shown to the user before starting message import

        Args:
            chat_id (``int``):
                Identifier of a chat to which the messages will be imported\. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can\_change\_info administrator right


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getMessageImportConfirmationText",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def importMessages(
        self, chat_id: int, message_file: dict, attached_files: list
    ) -> Result:
        """Imports messages exported from another app

        Args:
            chat_id (``int``):
                Identifier of a chat to which the messages will be imported\. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can\_change\_info administrator right

            message_file (``InputFile``):
                File with messages to import\. Only inputFileLocal and inputFileGenerated are supported\. The file must not be previously uploaded

            attached_files (``list``):
                Files used in the imported messages\. Only inputFileLocal and inputFileGenerated are supported\. The files must not be previously uploaded


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "importMessages",
            "chat_id": chat_id,
            "message_file": message_file,
            "attached_files": attached_files,
        }

        return await self.invoke(data)

    async def replacePrimaryChatInviteLink(self, chat_id: int) -> Result:
        """Replaces current primary invite link for a chat with a new primary invite link\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLink``)
        """

        data = {
            "@type": "replacePrimaryChatInviteLink",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def createChatInviteLink(
        self,
        chat_id: int,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
    ) -> Result:
        """Creates a new invite link for a chat\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right in the chat

        Args:
            chat_id (``int``):
                Chat identifier

            name (``str``):
                Invite link name; 0\-32 characters

            expiration_date (``int``):
                Point in time \(Unix timestamp\) when the link will expire; pass 0 if never

            member_limit (``int``):
                The maximum number of chat members that can join the chat via the link simultaneously; 0\-99999; pass 0 if not limited

            creates_join_request (``bool``):
                Pass true if users joining the chat via the link need to be approved by chat administrators\. In this case, member\_limit must be 0


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLink``)
        """

        data = {
            "@type": "createChatInviteLink",
            "chat_id": chat_id,
            "name": name,
            "expiration_date": expiration_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }

        return await self.invoke(data)

    async def editChatInviteLink(
        self,
        chat_id: int,
        invite_link: str,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
    ) -> Result:
        """Edits a non\-primary invite link for a chat\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to be edited

            name (``str``):
                Invite link name; 0\-32 characters

            expiration_date (``int``):
                Point in time \(Unix timestamp\) when the link will expire; pass 0 if never

            member_limit (``int``):
                The maximum number of chat members that can join the chat via the link simultaneously; 0\-99999; pass 0 if not limited

            creates_join_request (``bool``):
                Pass true if users joining the chat via the link need to be approved by chat administrators\. In this case, member\_limit must be 0


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLink``)
        """

        data = {
            "@type": "editChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "name": name,
            "expiration_date": expiration_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }

        return await self.invoke(data)

    async def getChatInviteLink(self, chat_id: int, invite_link: str) -> Result:
        """Returns information about an invite link\. Requires administrator privileges and can\_invite\_users right in the chat to get own links and owner privileges to get other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to get


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLink``)
        """

        data = {
            "@type": "getChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def getChatInviteLinkCounts(self, chat_id: int) -> Result:
        """Returns list of chat administrators with number of their invite links\. Requires owner privileges in the chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLinkCounts``)
        """

        data = {
            "@type": "getChatInviteLinkCounts",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getChatInviteLinks(
        self,
        chat_id: int,
        creator_user_id: int,
        is_revoked: bool,
        offset_date: int,
        offset_invite_link: str,
        limit: int,
    ) -> Result:
        """Returns invite links for a chat created by specified administrator\. Requires administrator privileges and can\_invite\_users right in the chat to get own links and owner privileges to get other links

        Args:
            chat_id (``int``):
                Chat identifier

            creator_user_id (``int``):
                User identifier of a chat administrator\. Must be an identifier of the current user for non\-owner

            is_revoked (``bool``):
                Pass true if revoked links needs to be returned instead of active or expired

            offset_date (``int``):
                Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning

            offset_invite_link (``str``):
                Invite link starting after which to return invite links; use empty string to get results from the beginning

            limit (``int``):
                The maximum number of invite links to return; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLinks``)
        """

        data = {
            "@type": "getChatInviteLinks",
            "chat_id": chat_id,
            "creator_user_id": creator_user_id,
            "is_revoked": is_revoked,
            "offset_date": offset_date,
            "offset_invite_link": offset_invite_link,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getChatInviteLinkMembers(
        self, chat_id: int, invite_link: str, limit: int, offset_member: dict = None
    ) -> Result:
        """Returns chat members joined a chat via an invite link\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to return chat members

            limit (``int``):
                The maximum number of chat members to return; up to 100

            offset_member (``chatInviteLinkMember``, *optional*):
                A chat member from which to return next chat members; pass null to get results from the beginning


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLinkMembers``)
        """

        data = {
            "@type": "getChatInviteLinkMembers",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "offset_member": offset_member,
            "limit": limit,
        }

        return await self.invoke(data)

    async def revokeChatInviteLink(self, chat_id: int, invite_link: str) -> Result:
        """Revokes invite link for a chat\. Available for basic groups, supergroups, and channels\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links\. If a primary link is revoked, then additionally to the revoked link returns new primary link

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to be revoked


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLinks``)
        """

        data = {
            "@type": "revokeChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def deleteRevokedChatInviteLink(
        self, chat_id: int, invite_link: str
    ) -> Result:
        """Deletes revoked chat invite links\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to revoke


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteRevokedChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def deleteAllRevokedChatInviteLinks(
        self, chat_id: int, creator_user_id: int
    ) -> Result:
        """Deletes all revoked chat invite links created by a given chat administrator\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            creator_user_id (``int``):
                User identifier of a chat administrator, which links will be deleted\. Must be an identifier of the current user for non\-owner


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteAllRevokedChatInviteLinks",
            "chat_id": chat_id,
            "creator_user_id": creator_user_id,
        }

        return await self.invoke(data)

    async def checkChatInviteLink(self, invite_link: str) -> Result:
        """Checks the validity of an invite link for a chat and returns information about the corresponding chat

        Args:
            invite_link (``str``):
                Invite link to be checked


        Returns:
            :class:`~pytdbot.types.Result` (``ChatInviteLinkInfo``)
        """

        data = {
            "@type": "checkChatInviteLink",
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def joinChatByInviteLink(self, invite_link: str) -> Result:
        """Uses an invite link to add the current user to the chat if possible\. May return an error with a message "INVITE\_REQUEST\_SENT" if only a join request was created

        Args:
            invite_link (``str``):
                Invite link to use


        Returns:
            :class:`~pytdbot.types.Result` (``Chat``)
        """

        data = {
            "@type": "joinChatByInviteLink",
            "invite_link": invite_link,
        }

        return await self.invoke(data)

    async def getChatJoinRequests(
        self,
        chat_id: int,
        invite_link: str,
        query: str,
        limit: int,
        offset_request: dict = None,
    ) -> Result:
        """Returns pending join requests in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to return join requests\. If empty, all join requests will be returned\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

            query (``str``):
                A query to search for in the first names, last names and usernames of the users to return

            limit (``int``):
                The maximum number of requests to join the chat to return

            offset_request (``chatJoinRequest``, *optional*):
                A chat join request from which to return next requests; pass null to get results from the beginning


        Returns:
            :class:`~pytdbot.types.Result` (``ChatJoinRequests``)
        """

        data = {
            "@type": "getChatJoinRequests",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "query": query,
            "offset_request": offset_request,
            "limit": limit,
        }

        return await self.invoke(data)

    async def processChatJoinRequest(
        self, chat_id: int, user_id: int, approve: bool
    ) -> Result:
        """Handles a pending join request in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user that sent the request

            approve (``bool``):
                Pass true to approve the request; pass false to decline it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "processChatJoinRequest",
            "chat_id": chat_id,
            "user_id": user_id,
            "approve": approve,
        }

        return await self.invoke(data)

    async def processChatJoinRequests(
        self, chat_id: int, invite_link: str, approve: bool
    ) -> Result:
        """Handles all pending join requests for a given link in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to process join requests\. If empty, all join requests will be processed\. Requires administrator privileges and can\_invite\_users right in the chat for own links and owner privileges for other links

            approve (``bool``):
                Pass true to approve all requests; pass false to decline them


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "processChatJoinRequests",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "approve": approve,
        }

        return await self.invoke(data)

    async def createCall(self, user_id: int, protocol: dict, is_video: bool) -> Result:
        """Creates a new call

        Args:
            user_id (``int``):
                Identifier of the user to be called

            protocol (``callProtocol``):
                The call protocols supported by the application

            is_video (``bool``):
                Pass true to create a video call


        Returns:
            :class:`~pytdbot.types.Result` (``CallId``)
        """

        data = {
            "@type": "createCall",
            "user_id": user_id,
            "protocol": protocol,
            "is_video": is_video,
        }

        return await self.invoke(data)

    async def acceptCall(self, call_id: int, protocol: dict) -> Result:
        """Accepts an incoming call

        Args:
            call_id (``int``):
                Call identifier

            protocol (``callProtocol``):
                The call protocols supported by the application


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "acceptCall",
            "call_id": call_id,
            "protocol": protocol,
        }

        return await self.invoke(data)

    async def sendCallSignalingData(self, call_id: int, data: bytes) -> Result:
        """Sends call signaling data

        Args:
            call_id (``int``):
                Call identifier

            data (``bytes``):
                The data


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendCallSignalingData",
            "call_id": call_id,
            "data": data,
        }

        return await self.invoke(data)

    async def discardCall(
        self,
        call_id: int,
        is_disconnected: bool,
        duration: int,
        is_video: bool,
        connection_id: int,
    ) -> Result:
        """Discards a call

        Args:
            call_id (``int``):
                Call identifier

            is_disconnected (``bool``):
                Pass true if the user was disconnected

            duration (``int``):
                The call duration, in seconds

            is_video (``bool``):
                Pass true if the call was a video call

            connection_id (``int``):
                Identifier of the connection used during the call


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "discardCall",
            "call_id": call_id,
            "is_disconnected": is_disconnected,
            "duration": duration,
            "is_video": is_video,
            "connection_id": connection_id,
        }

        return await self.invoke(data)

    async def sendCallRating(
        self, call_id: int, rating: int, comment: str, problems: list
    ) -> Result:
        """Sends a call rating

        Args:
            call_id (``int``):
                Call identifier

            rating (``int``):
                Call rating; 1\-5

            comment (``str``):
                An optional user comment if the rating is less than 5

            problems (``list``):
                List of the exact types of problems with the call, specified by the user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendCallRating",
            "call_id": call_id,
            "rating": rating,
            "comment": comment,
            "problems": problems,
        }

        return await self.invoke(data)

    async def sendCallDebugInformation(
        self, call_id: int, debug_information: str
    ) -> Result:
        """Sends debug information for a call to Telegram servers

        Args:
            call_id (``int``):
                Call identifier

            debug_information (``str``):
                Debug information in application\-specific format


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendCallDebugInformation",
            "call_id": call_id,
            "debug_information": debug_information,
        }

        return await self.invoke(data)

    async def sendCallLog(self, call_id: int, log_file: dict) -> Result:
        """Sends log file for a call to Telegram servers

        Args:
            call_id (``int``):
                Call identifier

            log_file (``InputFile``):
                Call log file\. Only inputFileLocal and inputFileGenerated are supported


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendCallLog",
            "call_id": call_id,
            "log_file": log_file,
        }

        return await self.invoke(data)

    async def getVideoChatAvailableParticipants(self, chat_id: int) -> Result:
        """Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``MessageSenders``)
        """

        data = {
            "@type": "getVideoChatAvailableParticipants",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def setVideoChatDefaultParticipant(
        self, chat_id: int, default_participant_id: dict
    ) -> Result:
        """Changes default participant identifier, on whose behalf a video chat in the chat will be joined

        Args:
            chat_id (``int``):
                Chat identifier

            default_participant_id (``MessageSender``):
                Default group call participant identifier to join the video chats


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setVideoChatDefaultParticipant",
            "chat_id": chat_id,
            "default_participant_id": default_participant_id,
        }

        return await self.invoke(data)

    async def createVideoChat(
        self, chat_id: int, title: str, start_date: int, is_rtmp_stream: bool
    ) -> Result:
        """Creates a video chat \(a group call bound to a chat\)\. Available only for basic groups, supergroups and channels; requires can\_manage\_video\_chats rights

        Args:
            chat_id (``int``):
                Identifier of a chat in which the video chat will be created

            title (``str``):
                Group call title; if empty, chat title will be used

            start_date (``int``):
                Point in time \(Unix timestamp\) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately\. The date must be at least 10 seconds and at most 8 days in the future

            is_rtmp_stream (``bool``):
                Pass true to create an RTMP stream instead of an ordinary video chat; requires creator privileges


        Returns:
            :class:`~pytdbot.types.Result` (``GroupCallId``)
        """

        data = {
            "@type": "createVideoChat",
            "chat_id": chat_id,
            "title": title,
            "start_date": start_date,
            "is_rtmp_stream": is_rtmp_stream,
        }

        return await self.invoke(data)

    async def getVideoChatRtmpUrl(self, chat_id: int) -> Result:
        """Returns RTMP URL for streaming to the chat; requires creator privileges

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``RtmpUrl``)
        """

        data = {
            "@type": "getVideoChatRtmpUrl",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def replaceVideoChatRtmpUrl(self, chat_id: int) -> Result:
        """Replaces the current RTMP URL for streaming to the chat; requires creator privileges

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``RtmpUrl``)
        """

        data = {
            "@type": "replaceVideoChatRtmpUrl",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getGroupCall(self, group_call_id: int) -> Result:
        """Returns information about a group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``GroupCall``)
        """

        data = {
            "@type": "getGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def startScheduledGroupCall(self, group_call_id: int) -> Result:
        """Starts a scheduled group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "startScheduledGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def toggleGroupCallEnabledStartNotification(
        self, group_call_id: int, enabled_start_notification: bool
    ) -> Result:
        """Toggles whether the current user will receive a notification when the group call starts; scheduled group calls only

        Args:
            group_call_id (``int``):
                Group call identifier

            enabled_start_notification (``bool``):
                New value of the enabled\_start\_notification setting


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallEnabledStartNotification",
            "group_call_id": group_call_id,
            "enabled_start_notification": enabled_start_notification,
        }

        return await self.invoke(data)

    async def joinGroupCall(
        self,
        group_call_id: int,
        audio_source_id: int,
        payload: str,
        is_muted: bool,
        is_my_video_enabled: bool,
        participant_id: dict = None,
        invite_hash: str = None,
    ) -> Result:
        """Joins an active group call\. Returns join response payload for tgcalls

        Args:
            group_call_id (``int``):
                Group call identifier

            audio_source_id (``int``):
                Caller audio channel synchronization source identifier; received from tgcalls

            payload (``str``):
                Group call join payload; received from tgcalls

            is_muted (``bool``):
                Pass true to join the call with muted microphone

            is_my_video_enabled (``bool``):
                Pass true if the user's video is enabled

            participant_id (``MessageSender``, *optional*):
                Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only

            invite_hash (``str``, *optional*):
                If non\-empty, invite hash to be used to join the group call without being muted by administrators


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "joinGroupCall",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "audio_source_id": audio_source_id,
            "payload": payload,
            "is_muted": is_muted,
            "is_my_video_enabled": is_my_video_enabled,
            "invite_hash": invite_hash,
        }

        return await self.invoke(data)

    async def startGroupCallScreenSharing(
        self, group_call_id: int, audio_source_id: int, payload: str
    ) -> Result:
        """Starts screen sharing in a joined group call\. Returns join response payload for tgcalls

        Args:
            group_call_id (``int``):
                Group call identifier

            audio_source_id (``int``):
                Screen sharing audio channel synchronization source identifier; received from tgcalls

            payload (``str``):
                Group call join payload; received from tgcalls


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "startGroupCallScreenSharing",
            "group_call_id": group_call_id,
            "audio_source_id": audio_source_id,
            "payload": payload,
        }

        return await self.invoke(data)

    async def toggleGroupCallScreenSharingIsPaused(
        self, group_call_id: int, is_paused: bool
    ) -> Result:
        """Pauses or unpauses screen sharing in a joined group call

        Args:
            group_call_id (``int``):
                Group call identifier

            is_paused (``bool``):
                Pass true to pause screen sharing; pass false to unpause it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallScreenSharingIsPaused",
            "group_call_id": group_call_id,
            "is_paused": is_paused,
        }

        return await self.invoke(data)

    async def endGroupCallScreenSharing(self, group_call_id: int) -> Result:
        """Ends screen sharing in a joined group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "endGroupCallScreenSharing",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def setGroupCallTitle(self, group_call_id: int, title: str) -> Result:
        """Sets group call title\. Requires groupCall\.can\_be\_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            title (``str``):
                New group call title; 1\-64 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setGroupCallTitle",
            "group_call_id": group_call_id,
            "title": title,
        }

        return await self.invoke(data)

    async def toggleGroupCallMuteNewParticipants(
        self, group_call_id: int, mute_new_participants: bool
    ) -> Result:
        """Toggles whether new participants of a group call can be unmuted only by administrators of the group call\. Requires groupCall\.can\_toggle\_mute\_new\_participants group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            mute_new_participants (``bool``):
                New value of the mute\_new\_participants setting


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallMuteNewParticipants",
            "group_call_id": group_call_id,
            "mute_new_participants": mute_new_participants,
        }

        return await self.invoke(data)

    async def inviteGroupCallParticipants(
        self, group_call_id: int, user_ids: list
    ) -> Result:
        """Invites users to an active group call\. Sends a service message of type messageInviteVideoChatParticipants for video chats

        Args:
            group_call_id (``int``):
                Group call identifier

            user_ids (``list``):
                User identifiers\. At most 10 users can be invited simultaneously


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "inviteGroupCallParticipants",
            "group_call_id": group_call_id,
            "user_ids": user_ids,
        }

        return await self.invoke(data)

    async def getGroupCallInviteLink(
        self, group_call_id: int, can_self_unmute: bool
    ) -> Result:
        """Returns invite link to a video chat in a public chat

        Args:
            group_call_id (``int``):
                Group call identifier

            can_self_unmute (``bool``):
                Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves\. Requires groupCall\.can\_be\_managed group call flag


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getGroupCallInviteLink",
            "group_call_id": group_call_id,
            "can_self_unmute": can_self_unmute,
        }

        return await self.invoke(data)

    async def revokeGroupCallInviteLink(self, group_call_id: int) -> Result:
        """Revokes invite link for a group call\. Requires groupCall\.can\_be\_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "revokeGroupCallInviteLink",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def startGroupCallRecording(
        self,
        group_call_id: int,
        title: str,
        record_video: bool,
        use_portrait_orientation: bool,
    ) -> Result:
        """Starts recording of an active group call\. Requires groupCall\.can\_be\_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            title (``str``):
                Group call recording title; 0\-64 characters

            record_video (``bool``):
                Pass true to record a video file instead of an audio file

            use_portrait_orientation (``bool``):
                Pass true to use portrait orientation for video instead of landscape one


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "startGroupCallRecording",
            "group_call_id": group_call_id,
            "title": title,
            "record_video": record_video,
            "use_portrait_orientation": use_portrait_orientation,
        }

        return await self.invoke(data)

    async def endGroupCallRecording(self, group_call_id: int) -> Result:
        """Ends recording of an active group call\. Requires groupCall\.can\_be\_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "endGroupCallRecording",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def toggleGroupCallIsMyVideoPaused(
        self, group_call_id: int, is_my_video_paused: bool
    ) -> Result:
        """Toggles whether current user's video is paused

        Args:
            group_call_id (``int``):
                Group call identifier

            is_my_video_paused (``bool``):
                Pass true if the current user's video is paused


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallIsMyVideoPaused",
            "group_call_id": group_call_id,
            "is_my_video_paused": is_my_video_paused,
        }

        return await self.invoke(data)

    async def toggleGroupCallIsMyVideoEnabled(
        self, group_call_id: int, is_my_video_enabled: bool
    ) -> Result:
        """Toggles whether current user's video is enabled

        Args:
            group_call_id (``int``):
                Group call identifier

            is_my_video_enabled (``bool``):
                Pass true if the current user's video is enabled


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallIsMyVideoEnabled",
            "group_call_id": group_call_id,
            "is_my_video_enabled": is_my_video_enabled,
        }

        return await self.invoke(data)

    async def setGroupCallParticipantIsSpeaking(
        self, group_call_id: int, audio_source: int, is_speaking: bool
    ) -> Result:
        """Informs TDLib that speaking state of a participant of an active group has changed

        Args:
            group_call_id (``int``):
                Group call identifier

            audio_source (``int``):
                Group call participant's synchronization audio source identifier, or 0 for the current user

            is_speaking (``bool``):
                Pass true if the user is speaking


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setGroupCallParticipantIsSpeaking",
            "group_call_id": group_call_id,
            "audio_source": audio_source,
            "is_speaking": is_speaking,
        }

        return await self.invoke(data)

    async def toggleGroupCallParticipantIsMuted(
        self, group_call_id: int, participant_id: dict, is_muted: bool
    ) -> Result:
        """Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``MessageSender``):
                Participant identifier

            is_muted (``bool``):
                Pass true to mute the user; pass false to unmute them


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallParticipantIsMuted",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "is_muted": is_muted,
        }

        return await self.invoke(data)

    async def setGroupCallParticipantVolumeLevel(
        self, group_call_id: int, participant_id: dict, volume_level: int
    ) -> Result:
        """Changes volume level of a participant of an active group call\. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``MessageSender``):
                Participant identifier

            volume_level (``int``):
                New participant's volume level; 1\-20000 in hundreds of percents


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setGroupCallParticipantVolumeLevel",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "volume_level": volume_level,
        }

        return await self.invoke(data)

    async def toggleGroupCallParticipantIsHandRaised(
        self, group_call_id: int, participant_id: dict, is_hand_raised: bool
    ) -> Result:
        """Toggles whether a group call participant hand is rased

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``MessageSender``):
                Participant identifier

            is_hand_raised (``bool``):
                Pass true if the user's hand needs to be raised\. Only self hand can be raised\. Requires groupCall\.can\_be\_managed group call flag to lower other's hand


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleGroupCallParticipantIsHandRaised",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "is_hand_raised": is_hand_raised,
        }

        return await self.invoke(data)

    async def loadGroupCallParticipants(self, group_call_id: int, limit: int) -> Result:
        """Loads more participants of a group call\. The loaded participants will be received through updates\. Use the field groupCall\.loaded\_all\_participants to check whether all participants have already been loaded

        Args:
            group_call_id (``int``):
                Group call identifier\. The group call must be previously received through getGroupCall and must be joined or being joined

            limit (``int``):
                The maximum number of participants to load; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "loadGroupCallParticipants",
            "group_call_id": group_call_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def leaveGroupCall(self, group_call_id: int) -> Result:
        """Leaves a group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "leaveGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def endGroupCall(self, group_call_id: int) -> Result:
        """Ends a group call\. Requires groupCall\.can\_be\_managed

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "endGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def getGroupCallStreams(self, group_call_id: int) -> Result:
        """Returns information about available group call streams

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Result` (``GroupCallStreams``)
        """

        data = {
            "@type": "getGroupCallStreams",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data)

    async def getGroupCallStreamSegment(
        self,
        group_call_id: int,
        time_offset: int,
        scale: int,
        channel_id: int,
        video_quality: dict = None,
    ) -> Result:
        """Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG\-4 format for video

        Args:
            group_call_id (``int``):
                Group call identifier

            time_offset (``int``):
                Point in time when the stream segment begins; Unix timestamp in milliseconds

            scale (``int``):
                Segment duration scale; 0\-1\. Segment's duration is 1000/\(2\*\*scale\) milliseconds

            channel_id (``int``):
                Identifier of an audio/video channel to get as received from tgcalls

            video_quality (``GroupCallVideoQuality``, *optional*):
                Video quality as received from tgcalls; pass null to get the worst available quality


        Returns:
            :class:`~pytdbot.types.Result` (``FilePart``)
        """

        data = {
            "@type": "getGroupCallStreamSegment",
            "group_call_id": group_call_id,
            "time_offset": time_offset,
            "scale": scale,
            "channel_id": channel_id,
            "video_quality": video_quality,
        }

        return await self.invoke(data)

    async def setMessageSenderBlockList(
        self, sender_id: dict, block_list: dict = None
    ) -> Result:
        """Changes the block list of a message sender\. Currently, only users and supergroup chats can be blocked

        Args:
            sender_id (``MessageSender``):
                Identifier of a message sender to block/unblock

            block_list (``BlockList``, *optional*):
                New block list for the message sender; pass null to unblock the message sender


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setMessageSenderBlockList",
            "sender_id": sender_id,
            "block_list": block_list,
        }

        return await self.invoke(data)

    async def blockMessageSenderFromReplies(
        self,
        message_id: int,
        delete_message: bool,
        delete_all_messages: bool,
        report_spam: bool,
    ) -> Result:
        """Blocks an original sender of a message in the Replies chat

        Args:
            message_id (``int``):
                The identifier of an incoming message in the Replies chat

            delete_message (``bool``):
                Pass true to delete the message

            delete_all_messages (``bool``):
                Pass true to delete all messages from the same sender

            report_spam (``bool``):
                Pass true to report the sender to the Telegram moderators


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "blockMessageSenderFromReplies",
            "message_id": message_id,
            "delete_message": delete_message,
            "delete_all_messages": delete_all_messages,
            "report_spam": report_spam,
        }

        return await self.invoke(data)

    async def getBlockedMessageSenders(
        self, block_list: dict, offset: int, limit: int
    ) -> Result:
        """Returns users and chats that were blocked by the current user

        Args:
            block_list (``BlockList``):
                Block list from which to return users

            offset (``int``):
                Number of users and chats to skip in the result; must be non\-negative

            limit (``int``):
                The maximum number of users and chats to return; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``MessageSenders``)
        """

        data = {
            "@type": "getBlockedMessageSenders",
            "block_list": block_list,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def addContact(self, contact: dict, share_phone_number: bool) -> Result:
        """Adds a user to the contact list or edits an existing contact by their user identifier

        Args:
            contact (``contact``):
                The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored

            share_phone_number (``bool``):
                Pass true to share the current user's phone number with the new contact\. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed\. Use the field userFullInfo\.need\_phone\_number\_privacy\_exception to check whether the current user needs to be asked to share their phone number


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addContact",
            "contact": contact,
            "share_phone_number": share_phone_number,
        }

        return await self.invoke(data)

    async def importContacts(self, contacts: list) -> Result:
        """Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

        Args:
            contacts (``list``):
                The list of contacts to import or edit; contacts' vCard are ignored and are not imported


        Returns:
            :class:`~pytdbot.types.Result` (``ImportedContacts``)
        """

        data = {
            "@type": "importContacts",
            "contacts": contacts,
        }

        return await self.invoke(data)

    async def getContacts(self) -> Result:
        """Returns all contacts of the user


        Returns:
            :class:`~pytdbot.types.Result` (``Users``)
        """

        data = {
            "@type": "getContacts",
        }

        return await self.invoke(data)

    async def searchContacts(self, limit: int, query: str = None) -> Result:
        """Searches for the specified query in the first names, last names and usernames of the known user contacts

        Args:
            limit (``int``):
                The maximum number of users to be returned

            query (``str``, *optional*):
                Query to search for; may be empty to return all contacts


        Returns:
            :class:`~pytdbot.types.Result` (``Users``)
        """

        data = {
            "@type": "searchContacts",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def removeContacts(self, user_ids: list) -> Result:
        """Removes users from the contact list

        Args:
            user_ids (``list``):
                Identifiers of users to be deleted


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeContacts",
            "user_ids": user_ids,
        }

        return await self.invoke(data)

    async def getImportedContactCount(self) -> Result:
        """Returns the total number of imported contacts


        Returns:
            :class:`~pytdbot.types.Result` (``Count``)
        """

        data = {
            "@type": "getImportedContactCount",
        }

        return await self.invoke(data)

    async def changeImportedContacts(self, contacts: list) -> Result:
        """Changes imported contacts using the list of contacts saved on the device\. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts\. Query result depends on the result of the previous query, so only one query is possible at the same time

        Args:
            contacts (``list``):
                The new list of contacts, contact's vCard are ignored and are not imported


        Returns:
            :class:`~pytdbot.types.Result` (``ImportedContacts``)
        """

        data = {
            "@type": "changeImportedContacts",
            "contacts": contacts,
        }

        return await self.invoke(data)

    async def clearImportedContacts(self) -> Result:
        """Clears all imported contacts, contact list remains unchanged


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearImportedContacts",
        }

        return await self.invoke(data)

    async def setCloseFriends(self, user_ids: list) -> Result:
        """Changes the list of close friends of the current user

        Args:
            user_ids (``list``):
                User identifiers of close friends; the users must be contacts of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setCloseFriends",
            "user_ids": user_ids,
        }

        return await self.invoke(data)

    async def getCloseFriends(self) -> Result:
        """Returns all close friends of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``Users``)
        """

        data = {
            "@type": "getCloseFriends",
        }

        return await self.invoke(data)

    async def setUserPersonalProfilePhoto(
        self, user_id: int, photo: dict = None
    ) -> Result:
        """Changes a personal profile photo of a contact user

        Args:
            user_id (``int``):
                User identifier

            photo (``InputChatPhoto``, *optional*):
                Profile photo to set; pass null to delete the photo; inputChatPhotoPrevious isn't supported in this function


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setUserPersonalProfilePhoto",
            "user_id": user_id,
            "photo": photo,
        }

        return await self.invoke(data)

    async def suggestUserProfilePhoto(self, user_id: int, photo: dict) -> Result:
        """Suggests a profile photo to another regular user with common messages

        Args:
            user_id (``int``):
                User identifier

            photo (``InputChatPhoto``):
                Profile photo to suggest; inputChatPhotoPrevious isn't supported in this function


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "suggestUserProfilePhoto",
            "user_id": user_id,
            "photo": photo,
        }

        return await self.invoke(data)

    async def searchUserByPhoneNumber(self, phone_number: str) -> Result:
        """Searches a user by their phone number\. Returns a 404 error if the user can't be found

        Args:
            phone_number (``str``):
                Phone number to search for


        Returns:
            :class:`~pytdbot.types.Result` (``User``)
        """

        data = {
            "@type": "searchUserByPhoneNumber",
            "phone_number": phone_number,
        }

        return await self.invoke(data)

    async def sharePhoneNumber(self, user_id: int) -> Result:
        """Shares the phone number of the current user with a mutual contact\. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber

        Args:
            user_id (``int``):
                Identifier of the user with whom to share the phone number\. The user must be a mutual contact


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sharePhoneNumber",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def getUserProfilePhotos(
        self, user_id: int, offset: int, limit: int
    ) -> Result:
        """Returns the profile photos of a user\. Personal and public photo aren't returned

        Args:
            user_id (``int``):
                User identifier

            offset (``int``):
                The number of photos to skip; must be non\-negative

            limit (``int``):
                The maximum number of photos to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``ChatPhotos``)
        """

        data = {
            "@type": "getUserProfilePhotos",
            "user_id": user_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getStickers(
        self, sticker_type: dict, query: str, limit: int, chat_id: int
    ) -> Result:
        """Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker\-specific keywords\. If the query is non\-empty, then favorite, recently used or trending stickers may also be returned

        Args:
            sticker_type (``StickerType``):
                Type of the stickers to return

            query (``str``):
                Search query; a space\-separated list of emoji or a keyword prefix\. If empty, returns all known installed stickers

            limit (``int``):
                The maximum number of stickers to be returned

            chat_id (``int``):
                Chat identifier for which to return stickers\. Available custom emoji stickers may be different for different chats


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getStickers",
            "sticker_type": sticker_type,
            "query": query,
            "limit": limit,
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getAllStickerEmojis(
        self, sticker_type: dict, query: str, chat_id: int, return_only_main_emoji: bool
    ) -> Result:
        """Returns unique emoji that correspond to stickers to be found by the getStickers\(sticker\_type, query, 1000000, chat\_id\)

        Args:
            sticker_type (``StickerType``):
                Type of the stickers to search for

            query (``str``):
                Search query

            chat_id (``int``):
                Chat identifier for which to find stickers

            return_only_main_emoji (``bool``):
                Pass true if only main emoji for each found sticker must be included in the result


        Returns:
            :class:`~pytdbot.types.Result` (``Emojis``)
        """

        data = {
            "@type": "getAllStickerEmojis",
            "sticker_type": sticker_type,
            "query": query,
            "chat_id": chat_id,
            "return_only_main_emoji": return_only_main_emoji,
        }

        return await self.invoke(data)

    async def searchStickers(
        self, sticker_type: dict, emojis: str, limit: int
    ) -> Result:
        """Searches for stickers from public sticker sets that correspond to any of the given emoji

        Args:
            sticker_type (``StickerType``):
                Type of the stickers to return

            emojis (``str``):
                Space\-separated list of emoji to search for; must be non\-empty

            limit (``int``):
                The maximum number of stickers to be returned; 0\-100


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "searchStickers",
            "sticker_type": sticker_type,
            "emojis": emojis,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getPremiumStickers(self, limit: int) -> Result:
        """Returns premium stickers from regular sticker sets

        Args:
            limit (``int``):
                The maximum number of stickers to be returned; 0\-100


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getPremiumStickers",
            "limit": limit,
        }

        return await self.invoke(data)

    async def getInstalledStickerSets(self, sticker_type: dict) -> Result:
        """Returns a list of installed sticker sets

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to return


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSets``)
        """

        data = {
            "@type": "getInstalledStickerSets",
            "sticker_type": sticker_type,
        }

        return await self.invoke(data)

    async def getArchivedStickerSets(
        self, sticker_type: dict, offset_sticker_set_id: int, limit: int
    ) -> Result:
        """Returns a list of archived sticker sets

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to return

            offset_sticker_set_id (``int``):
                Identifier of the sticker set from which to return the result

            limit (``int``):
                The maximum number of sticker sets to return; up to 100


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSets``)
        """

        data = {
            "@type": "getArchivedStickerSets",
            "sticker_type": sticker_type,
            "offset_sticker_set_id": offset_sticker_set_id,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getTrendingStickerSets(
        self, sticker_type: dict, offset: int, limit: int
    ) -> Result:
        """Returns a list of trending sticker sets\. For optimal performance, the number of returned sticker sets is chosen by TDLib

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to return

            offset (``int``):
                The offset from which to return the sticker sets; must be non\-negative

            limit (``int``):
                The maximum number of sticker sets to be returned; up to 100\. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached


        Returns:
            :class:`~pytdbot.types.Result` (``TrendingStickerSets``)
        """

        data = {
            "@type": "getTrendingStickerSets",
            "sticker_type": sticker_type,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getAttachedStickerSets(self, file_id: int) -> Result:
        """Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets\. Currently, only animations, photos, and videos can have attached sticker sets

        Args:
            file_id (``int``):
                File identifier


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSets``)
        """

        data = {
            "@type": "getAttachedStickerSets",
            "file_id": file_id,
        }

        return await self.invoke(data)

    async def getStickerSet(self, set_id: int) -> Result:
        """Returns information about a sticker set by its identifier

        Args:
            set_id (``int``):
                Identifier of the sticker set


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSet``)
        """

        data = {
            "@type": "getStickerSet",
            "set_id": set_id,
        }

        return await self.invoke(data)

    async def searchStickerSet(self, name: str) -> Result:
        """Searches for a sticker set by its name

        Args:
            name (``str``):
                Name of the sticker set


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSet``)
        """

        data = {
            "@type": "searchStickerSet",
            "name": name,
        }

        return await self.invoke(data)

    async def searchInstalledStickerSets(
        self, sticker_type: dict, query: str, limit: int
    ) -> Result:
        """Searches for installed sticker sets by looking for specified query in their title and name

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to search for

            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of sticker sets to return


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSets``)
        """

        data = {
            "@type": "searchInstalledStickerSets",
            "sticker_type": sticker_type,
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data)

    async def searchStickerSets(self, sticker_type: dict, query: str) -> Result:
        """Searches for sticker sets by looking for specified query in their title and name\. Excludes installed sticker sets from the results

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to return

            query (``str``):
                Query to search for


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSets``)
        """

        data = {
            "@type": "searchStickerSets",
            "sticker_type": sticker_type,
            "query": query,
        }

        return await self.invoke(data)

    async def changeStickerSet(
        self, set_id: int, is_installed: bool, is_archived: bool
    ) -> Result:
        """Installs/uninstalls or activates/archives a sticker set

        Args:
            set_id (``int``):
                Identifier of the sticker set

            is_installed (``bool``):
                The new value of is\_installed

            is_archived (``bool``):
                The new value of is\_archived\. A sticker set can't be installed and archived simultaneously


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "changeStickerSet",
            "set_id": set_id,
            "is_installed": is_installed,
            "is_archived": is_archived,
        }

        return await self.invoke(data)

    async def viewTrendingStickerSets(self, sticker_set_ids: list) -> Result:
        """Informs the server that some trending sticker sets have been viewed by the user

        Args:
            sticker_set_ids (``list``):
                Identifiers of viewed trending sticker sets


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "viewTrendingStickerSets",
            "sticker_set_ids": sticker_set_ids,
        }

        return await self.invoke(data)

    async def reorderInstalledStickerSets(
        self, sticker_type: dict, sticker_set_ids: list
    ) -> Result:
        """Changes the order of installed sticker sets

        Args:
            sticker_type (``StickerType``):
                Type of the sticker sets to reorder

            sticker_set_ids (``list``):
                Identifiers of installed sticker sets in the new correct order


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reorderInstalledStickerSets",
            "sticker_type": sticker_type,
            "sticker_set_ids": sticker_set_ids,
        }

        return await self.invoke(data)

    async def getRecentStickers(self, is_attached: bool) -> Result:
        """Returns a list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getRecentStickers",
            "is_attached": is_attached,
        }

        return await self.invoke(data)

    async def addRecentSticker(self, is_attached: bool, sticker: dict) -> Result:
        """Manually adds a new sticker to the list of recently used stickers\. The new sticker is added to the top of the list\. If the sticker was already in the list, it is removed from the list first\. Only stickers belonging to a sticker set can be added to this list\. Emoji stickers can't be added to recent stickers

        Args:
            is_attached (``bool``):
                Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers

            sticker (``InputFile``):
                Sticker file to add


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "addRecentSticker",
            "is_attached": is_attached,
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def removeRecentSticker(self, is_attached: bool, sticker: dict) -> Result:
        """Removes a sticker from the list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers

            sticker (``InputFile``):
                Sticker file to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeRecentSticker",
            "is_attached": is_attached,
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def clearRecentStickers(self, is_attached: bool) -> Result:
        """Clears the list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearRecentStickers",
            "is_attached": is_attached,
        }

        return await self.invoke(data)

    async def getFavoriteStickers(self) -> Result:
        """Returns favorite stickers


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getFavoriteStickers",
        }

        return await self.invoke(data)

    async def addFavoriteSticker(self, sticker: dict) -> Result:
        """Adds a new sticker to the list of favorite stickers\. The new sticker is added to the top of the list\. If the sticker was already in the list, it is removed from the list first\. Only stickers belonging to a sticker set can be added to this list\. Emoji stickers can't be added to favorite stickers

        Args:
            sticker (``InputFile``):
                Sticker file to add


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addFavoriteSticker",
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def removeFavoriteSticker(self, sticker: dict) -> Result:
        """Removes a sticker from the list of favorite stickers

        Args:
            sticker (``InputFile``):
                Sticker file to delete from the list


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeFavoriteSticker",
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def getStickerEmojis(self, sticker: dict) -> Result:
        """Returns emoji corresponding to a sticker\. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

        Args:
            sticker (``InputFile``):
                Sticker file identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Emojis``)
        """

        data = {
            "@type": "getStickerEmojis",
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def searchEmojis(
        self, text: str, exact_match: bool, input_language_codes: list = None
    ) -> Result:
        """Searches for emojis by keywords\. Supported only if the file database is enabled

        Args:
            text (``str``):
                Text to search for

            exact_match (``bool``):
                Pass true if only emojis, which exactly match the text, needs to be returned

            input_language_codes (``list``, *optional*):
                List of possible IETF language tags of the user's input language; may be empty if unknown


        Returns:
            :class:`~pytdbot.types.Result` (``Emojis``)
        """

        data = {
            "@type": "searchEmojis",
            "text": text,
            "exact_match": exact_match,
            "input_language_codes": input_language_codes,
        }

        return await self.invoke(data)

    async def getEmojiCategories(self, type: dict = None) -> Result:
        """Returns available emojis categories

        Args:
            type (``EmojiCategoryType``, *optional*):
                Type of emoji categories to return; pass null to get default emoji categories


        Returns:
            :class:`~pytdbot.types.Result` (``EmojiCategories``)
        """

        data = {
            "@type": "getEmojiCategories",
            "type": type,
        }

        return await self.invoke(data)

    async def getAnimatedEmoji(self, emoji: str) -> Result:
        """Returns an animated emoji corresponding to a given emoji\. Returns a 404 error if the emoji has no animated emoji

        Args:
            emoji (``str``):
                The emoji


        Returns:
            :class:`~pytdbot.types.Result` (``AnimatedEmoji``)
        """

        data = {
            "@type": "getAnimatedEmoji",
            "emoji": emoji,
        }

        return await self.invoke(data)

    async def getEmojiSuggestionsUrl(self, language_code: str) -> Result:
        """Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements\. The URL will be valid for 30 seconds after generation

        Args:
            language_code (``str``):
                Language code for which the emoji replacements will be suggested


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getEmojiSuggestionsUrl",
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def getCustomEmojiStickers(self, custom_emoji_ids: list) -> Result:
        """Returns list of custom emoji stickers by their identifiers\. Stickers are returned in arbitrary order\. Only found stickers are returned

        Args:
            custom_emoji_ids (``list``):
                Identifiers of custom emoji stickers\. At most 200 custom emoji stickers can be received simultaneously


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getCustomEmojiStickers",
            "custom_emoji_ids": custom_emoji_ids,
        }

        return await self.invoke(data)

    async def getDefaultChatPhotoCustomEmojiStickers(self) -> Result:
        """Returns default list of custom emoji stickers for placing on a chat photo


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getDefaultChatPhotoCustomEmojiStickers",
        }

        return await self.invoke(data)

    async def getDefaultProfilePhotoCustomEmojiStickers(self) -> Result:
        """Returns default list of custom emoji stickers for placing on a profile photo


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getDefaultProfilePhotoCustomEmojiStickers",
        }

        return await self.invoke(data)

    async def getDefaultBackgroundCustomEmojiStickers(self) -> Result:
        """Returns default list of custom emoji stickers for reply background


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getDefaultBackgroundCustomEmojiStickers",
        }

        return await self.invoke(data)

    async def getSavedAnimations(self) -> Result:
        """Returns saved animations


        Returns:
            :class:`~pytdbot.types.Result` (``Animations``)
        """

        data = {
            "@type": "getSavedAnimations",
        }

        return await self.invoke(data)

    async def addSavedAnimation(self, animation: dict) -> Result:
        """Manually adds a new animation to the list of saved animations\. The new animation is added to the beginning of the list\. If the animation was already in the list, it is removed first\. Only non\-secret video animations with MIME type "video/mp4" can be added to the list

        Args:
            animation (``InputFile``):
                The animation file to be added\. Only animations known to the server \(i\.e\., successfully sent via a message\) can be added to the list


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addSavedAnimation",
            "animation": animation,
        }

        return await self.invoke(data)

    async def removeSavedAnimation(self, animation: dict) -> Result:
        """Removes an animation from the list of saved animations

        Args:
            animation (``InputFile``):
                Animation file to be removed


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeSavedAnimation",
            "animation": animation,
        }

        return await self.invoke(data)

    async def getRecentInlineBots(self) -> Result:
        """Returns up to 20 recently used inline bots in the order of their last usage


        Returns:
            :class:`~pytdbot.types.Result` (``Users``)
        """

        data = {
            "@type": "getRecentInlineBots",
        }

        return await self.invoke(data)

    async def searchHashtags(self, prefix: str, limit: int) -> Result:
        """Searches for recently used hashtags by their prefix

        Args:
            prefix (``str``):
                Hashtag prefix to search for

            limit (``int``):
                The maximum number of hashtags to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Hashtags``)
        """

        data = {
            "@type": "searchHashtags",
            "prefix": prefix,
            "limit": limit,
        }

        return await self.invoke(data)

    async def removeRecentHashtag(self, hashtag: str) -> Result:
        """Removes a hashtag from the list of recently used hashtags

        Args:
            hashtag (``str``):
                Hashtag to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeRecentHashtag",
            "hashtag": hashtag,
        }

        return await self.invoke(data)

    async def getWebPagePreview(
        self, text: dict, link_preview_options: dict = None
    ) -> Result:
        """Returns a link preview by the text of a message\. Do not call this function too often\. Returns a 404 error if the text has no link preview

        Args:
            text (``formattedText``):
                Message text with formatting

            link_preview_options (``linkPreviewOptions``, *optional*):
                Options to be used for generation of the link preview; pass null to use default link preview options


        Returns:
            :class:`~pytdbot.types.Result` (``WebPage``)
        """

        data = {
            "@type": "getWebPagePreview",
            "text": text,
            "link_preview_options": link_preview_options,
        }

        return await self.invoke(data)

    async def getWebPageInstantView(self, url: str, force_full: bool) -> Result:
        """Returns an instant view version of a web page if available\. Returns a 404 error if the web page has no instant view page

        Args:
            url (``str``):
                The web page URL

            force_full (``bool``):
                Pass true to get full instant view for the web page


        Returns:
            :class:`~pytdbot.types.Result` (``WebPageInstantView``)
        """

        data = {
            "@type": "getWebPageInstantView",
            "url": url,
            "force_full": force_full,
        }

        return await self.invoke(data)

    async def setProfilePhoto(self, photo: dict, is_public: bool) -> Result:
        """Changes a profile photo for the current user

        Args:
            photo (``InputChatPhoto``):
                Profile photo to set

            is_public (``bool``):
                Pass true to set a public photo, which will be visible even the main photo is hidden by privacy settings


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setProfilePhoto",
            "photo": photo,
            "is_public": is_public,
        }

        return await self.invoke(data)

    async def deleteProfilePhoto(self, profile_photo_id: int) -> Result:
        """Deletes a profile photo

        Args:
            profile_photo_id (``int``):
                Identifier of the profile photo to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteProfilePhoto",
            "profile_photo_id": profile_photo_id,
        }

        return await self.invoke(data)

    async def setAccentColor(
        self, accent_color_id: int, background_custom_emoji_id: int
    ) -> Result:
        """Changes accent color and background custom emoji for the current user; for Telegram Premium users only

        Args:
            accent_color_id (``int``):
                Identifier of the accent color to use

            background_custom_emoji_id (``int``):
                Identifier of a custom emoji to be shown on the reply header background; 0 if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAccentColor",
            "accent_color_id": accent_color_id,
            "background_custom_emoji_id": background_custom_emoji_id,
        }

        return await self.invoke(data)

    async def setProfileAccentColor(
        self, profile_accent_color_id: int, profile_background_custom_emoji_id: int
    ) -> Result:
        """Changes accent color and background custom emoji for profile of the current user; for Telegram Premium users only

        Args:
            profile_accent_color_id (``int``):
                Identifier of the accent color to use for profile; pass \-1 if none

            profile_background_custom_emoji_id (``int``):
                Identifier of a custom emoji to be shown in the on the user's profile photo background; 0 if none


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setProfileAccentColor",
            "profile_accent_color_id": profile_accent_color_id,
            "profile_background_custom_emoji_id": profile_background_custom_emoji_id,
        }

        return await self.invoke(data)

    async def setName(self, first_name: str, last_name: str) -> Result:
        """Changes the first and last name of the current user

        Args:
            first_name (``str``):
                The new value of the first name for the current user; 1\-64 characters

            last_name (``str``):
                The new value of the optional last name for the current user; 0\-64 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setName",
            "first_name": first_name,
            "last_name": last_name,
        }

        return await self.invoke(data)

    async def setBio(self, bio: str) -> Result:
        """Changes the bio of the current user

        Args:
            bio (``str``):
                The new value of the user bio; 0\-getOption\("bio\_length\_max"\) characters without line feeds


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBio",
            "bio": bio,
        }

        return await self.invoke(data)

    async def setUsername(self, username: str) -> Result:
        """Changes the editable username of the current user

        Args:
            username (``str``):
                The new value of the username\. Use an empty string to remove the username\. The username can't be completely removed if there is another active or disabled username


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setUsername",
            "username": username,
        }

        return await self.invoke(data)

    async def toggleUsernameIsActive(self, username: str, is_active: bool) -> Result:
        """Changes active state for a username of the current user\. The editable username can't be disabled\. May return an error with a message "USERNAMES\_ACTIVE\_TOO\_MUCH" if the maximum number of active usernames has been reached

        Args:
            username (``str``):
                The username to change

            is_active (``bool``):
                Pass true to activate the username; pass false to disable it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleUsernameIsActive",
            "username": username,
            "is_active": is_active,
        }

        return await self.invoke(data)

    async def reorderActiveUsernames(self, usernames: list) -> Result:
        """Changes order of active usernames of the current user

        Args:
            usernames (``list``):
                The new order of active usernames\. All currently active usernames must be specified


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reorderActiveUsernames",
            "usernames": usernames,
        }

        return await self.invoke(data)

    async def setEmojiStatus(self, emoji_status: dict = None) -> Result:
        """Changes the emoji status of the current user; for Telegram Premium users only

        Args:
            emoji_status (``emojiStatus``, *optional*):
                New emoji status; pass null to switch to the default badge


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setEmojiStatus",
            "emoji_status": emoji_status,
        }

        return await self.invoke(data)

    async def setLocation(self, location: dict) -> Result:
        """Changes the location of the current user\. Needs to be called if getOption\("is\_location\_visible"\) is true and location changes for more than 1 kilometer

        Args:
            location (``location``):
                The new location of the user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setLocation",
            "location": location,
        }

        return await self.invoke(data)

    async def changePhoneNumber(
        self, phone_number: str, settings: dict = None
    ) -> Result:
        """Changes the phone number of the user and sends an authentication code to the user's new phone number; for official Android and iOS applications only\. On success, returns information about the sent code

        Args:
            phone_number (``str``):
                The new phone number of the user in international format

            settings (``phoneNumberAuthenticationSettings``, *optional*):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "changePhoneNumber",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data)

    async def resendChangePhoneNumberCode(self) -> Result:
        """Resends the authentication code sent to confirm a new phone number for the current user\. Works only if the previously received authenticationCodeInfo next\_code\_type was not null and the server\-specified timeout has passed


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "resendChangePhoneNumberCode",
        }

        return await self.invoke(data)

    async def checkChangePhoneNumberCode(self, code: str) -> Result:
        """Checks the authentication code sent to confirm a new phone number of the user

        Args:
            code (``str``):
                Authentication code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkChangePhoneNumberCode",
            "code": code,
        }

        return await self.invoke(data)

    async def getUserLink(self) -> Result:
        """Returns an HTTPS link, which can be used to get information about the current user


        Returns:
            :class:`~pytdbot.types.Result` (``UserLink``)
        """

        data = {
            "@type": "getUserLink",
        }

        return await self.invoke(data)

    async def searchUserByToken(self, token: str) -> Result:
        """Searches a user by a token from the user's link

        Args:
            token (``str``):
                Token to search for


        Returns:
            :class:`~pytdbot.types.Result` (``User``)
        """

        data = {
            "@type": "searchUserByToken",
            "token": token,
        }

        return await self.invoke(data)

    async def setCommands(
        self, language_code: str, commands: list, scope: dict = None
    ) -> Result:
        """Sets the list of commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two\-letter ISO 639\-1 language code\. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands

            commands (``list``):
                List of the bot's commands

            scope (``BotCommandScope``, *optional*):
                The scope to which the commands are relevant; pass null to change commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setCommands",
            "scope": scope,
            "language_code": language_code,
            "commands": commands,
        }

        return await self.invoke(data)

    async def deleteCommands(self, language_code: str, scope: dict = None) -> Result:
        """Deletes commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two\-letter ISO 639\-1 language code or an empty string

            scope (``BotCommandScope``, *optional*):
                The scope to which the commands are relevant; pass null to delete commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteCommands",
            "scope": scope,
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def getCommands(self, language_code: str, scope: dict = None) -> Result:
        """Returns list of commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two\-letter ISO 639\-1 language code or an empty string

            scope (``BotCommandScope``, *optional*):
                The scope to which the commands are relevant; pass null to get commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Result` (``BotCommands``)
        """

        data = {
            "@type": "getCommands",
            "scope": scope,
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def setMenuButton(self, user_id: int, menu_button: dict) -> Result:
        """Sets menu button for the given user or for all users; for bots only

        Args:
            user_id (``int``):
                Identifier of the user or 0 to set menu button for all users

            menu_button (``botMenuButton``):
                New menu button


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setMenuButton",
            "user_id": user_id,
            "menu_button": menu_button,
        }

        return await self.invoke(data)

    async def getMenuButton(self, user_id: int) -> Result:
        """Returns menu button set by the bot for the given user; for bots only

        Args:
            user_id (``int``):
                Identifier of the user or 0 to get the default menu button


        Returns:
            :class:`~pytdbot.types.Result` (``BotMenuButton``)
        """

        data = {
            "@type": "getMenuButton",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def setDefaultGroupAdministratorRights(
        self, default_group_administrator_rights: dict = None
    ) -> Result:
        """Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

        Args:
            default_group_administrator_rights (``chatAdministratorRights``, *optional*):
                Default administrator rights for adding the bot to basic group and supergroup chats; pass null to remove default rights


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setDefaultGroupAdministratorRights",
            "default_group_administrator_rights": default_group_administrator_rights,
        }

        return await self.invoke(data)

    async def setDefaultChannelAdministratorRights(
        self, default_channel_administrator_rights: dict = None
    ) -> Result:
        """Sets default administrator rights for adding the bot to channel chats; for bots only

        Args:
            default_channel_administrator_rights (``chatAdministratorRights``, *optional*):
                Default administrator rights for adding the bot to channels; pass null to remove default rights


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setDefaultChannelAdministratorRights",
            "default_channel_administrator_rights": default_channel_administrator_rights,
        }

        return await self.invoke(data)

    async def canBotSendMessages(self, bot_user_id: int) -> Result:
        """Checks whether the specified bot can send messages to the user\. Returns a 404 error if can't and the access can be granted by call to allowBotToSendMessages

        Args:
            bot_user_id (``int``):
                Identifier of the target bot


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "canBotSendMessages",
            "bot_user_id": bot_user_id,
        }

        return await self.invoke(data)

    async def allowBotToSendMessages(self, bot_user_id: int) -> Result:
        """Allows the specified bot to send messages to the user

        Args:
            bot_user_id (``int``):
                Identifier of the target bot


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "allowBotToSendMessages",
            "bot_user_id": bot_user_id,
        }

        return await self.invoke(data)

    async def sendWebAppCustomRequest(
        self, bot_user_id: int, method: str, parameters: str
    ) -> Result:
        """Sends a custom request from a Web App

        Args:
            bot_user_id (``int``):
                Identifier of the bot

            method (``str``):
                The method name

            parameters (``str``):
                JSON\-serialized method parameters


        Returns:
            :class:`~pytdbot.types.Result` (``CustomRequestResult``)
        """

        data = {
            "@type": "sendWebAppCustomRequest",
            "bot_user_id": bot_user_id,
            "method": method,
            "parameters": parameters,
        }

        return await self.invoke(data)

    async def setBotName(
        self, bot_user_id: int, language_code: str, name: str
    ) -> Result:
        """Sets the name of a bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code\. If empty, the name will be shown to all users for whose languages there is no dedicated name

            name (``str``):
                New bot's name on the specified language; 0\-64 characters; must be non\-empty if language code is empty


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBotName",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
            "name": name,
        }

        return await self.invoke(data)

    async def getBotName(self, bot_user_id: int, language_code: str) -> Result:
        """Returns the name of a bot in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code or an empty string


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getBotName",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def setBotProfilePhoto(self, bot_user_id: int, photo: dict = None) -> Result:
        """Changes a profile photo for a bot

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            photo (``InputChatPhoto``, *optional*):
                Profile photo to set; pass null to delete the chat photo


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBotProfilePhoto",
            "bot_user_id": bot_user_id,
            "photo": photo,
        }

        return await self.invoke(data)

    async def toggleBotUsernameIsActive(
        self, bot_user_id: int, username: str, is_active: bool
    ) -> Result:
        """Changes active state for a username of a bot\. The editable username can't be disabled\. May return an error with a message "USERNAMES\_ACTIVE\_TOO\_MUCH" if the maximum number of active usernames has been reached\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            username (``str``):
                The username to change

            is_active (``bool``):
                Pass true to activate the username; pass false to disable it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleBotUsernameIsActive",
            "bot_user_id": bot_user_id,
            "username": username,
            "is_active": is_active,
        }

        return await self.invoke(data)

    async def reorderBotActiveUsernames(
        self, bot_user_id: int, usernames: list
    ) -> Result:
        """Changes order of active usernames of a bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            usernames (``list``):
                The new order of active usernames\. All currently active usernames must be specified


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reorderBotActiveUsernames",
            "bot_user_id": bot_user_id,
            "usernames": usernames,
        }

        return await self.invoke(data)

    async def setBotInfoDescription(
        self, bot_user_id: int, language_code: str, description: str
    ) -> Result:
        """Sets the text shown in the chat with a bot if the chat is empty\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code\. If empty, the description will be shown to all users for whose languages there is no dedicated description

            description (``str``):
                New bot's description on the specified language


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBotInfoDescription",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
            "description": description,
        }

        return await self.invoke(data)

    async def getBotInfoDescription(
        self, bot_user_id: int, language_code: str
    ) -> Result:
        """Returns the text shown in the chat with a bot if the chat is empty in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code or an empty string


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getBotInfoDescription",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def setBotInfoShortDescription(
        self, bot_user_id: int, language_code: str, short_description: str
    ) -> Result:
        """Sets the text shown on a bot's profile page and sent together with the link when users share the bot\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code\. If empty, the short description will be shown to all users for whose languages there is no dedicated description

            short_description (``str``):
                New bot's short description on the specified language


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBotInfoShortDescription",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
            "short_description": short_description,
        }

        return await self.invoke(data)

    async def getBotInfoShortDescription(
        self, bot_user_id: int, language_code: str
    ) -> Result:
        """Returns the text shown on a bot's profile page and sent together with the link when users share the bot in the given language\. Can be called only if userTypeBot\.can\_be\_edited \=\= true

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            language_code (``str``):
                A two\-letter ISO 639\-1 language code or an empty string


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getBotInfoShortDescription",
            "bot_user_id": bot_user_id,
            "language_code": language_code,
        }

        return await self.invoke(data)

    async def getActiveSessions(self) -> Result:
        """Returns all active sessions of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``Sessions``)
        """

        data = {
            "@type": "getActiveSessions",
        }

        return await self.invoke(data)

    async def terminateSession(self, session_id: int) -> Result:
        """Terminates a session of the current user

        Args:
            session_id (``int``):
                Session identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "terminateSession",
            "session_id": session_id,
        }

        return await self.invoke(data)

    async def terminateAllOtherSessions(self) -> Result:
        """Terminates all other sessions of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "terminateAllOtherSessions",
        }

        return await self.invoke(data)

    async def confirmSession(self, session_id: int) -> Result:
        """Confirms an unconfirmed session of the current user from another device

        Args:
            session_id (``int``):
                Session identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "confirmSession",
            "session_id": session_id,
        }

        return await self.invoke(data)

    async def toggleSessionCanAcceptCalls(
        self, session_id: int, can_accept_calls: bool
    ) -> Result:
        """Toggles whether a session can accept incoming calls

        Args:
            session_id (``int``):
                Session identifier

            can_accept_calls (``bool``):
                Pass true to allow accepting incoming calls by the session; pass false otherwise


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSessionCanAcceptCalls",
            "session_id": session_id,
            "can_accept_calls": can_accept_calls,
        }

        return await self.invoke(data)

    async def toggleSessionCanAcceptSecretChats(
        self, session_id: int, can_accept_secret_chats: bool
    ) -> Result:
        """Toggles whether a session can accept incoming secret chats

        Args:
            session_id (``int``):
                Session identifier

            can_accept_secret_chats (``bool``):
                Pass true to allow accepting secret chats by the session; pass false otherwise


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSessionCanAcceptSecretChats",
            "session_id": session_id,
            "can_accept_secret_chats": can_accept_secret_chats,
        }

        return await self.invoke(data)

    async def setInactiveSessionTtl(self, inactive_session_ttl_days: int) -> Result:
        """Changes the period of inactivity after which sessions will automatically be terminated

        Args:
            inactive_session_ttl_days (``int``):
                New number of days of inactivity before sessions will be automatically terminated; 1\-366 days


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setInactiveSessionTtl",
            "inactive_session_ttl_days": inactive_session_ttl_days,
        }

        return await self.invoke(data)

    async def getConnectedWebsites(self) -> Result:
        """Returns all website where the current user used Telegram to log in


        Returns:
            :class:`~pytdbot.types.Result` (``ConnectedWebsites``)
        """

        data = {
            "@type": "getConnectedWebsites",
        }

        return await self.invoke(data)

    async def disconnectWebsite(self, website_id: int) -> Result:
        """Disconnects website from the current user's Telegram account

        Args:
            website_id (``int``):
                Website identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "disconnectWebsite",
            "website_id": website_id,
        }

        return await self.invoke(data)

    async def disconnectAllWebsites(self) -> Result:
        """Disconnects all websites from the current user's Telegram account


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "disconnectAllWebsites",
        }

        return await self.invoke(data)

    async def setSupergroupUsername(self, supergroup_id: int, username: str) -> Result:
        """Changes the editable username of a supergroup or channel, requires owner privileges in the supergroup or channel

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            username (``str``):
                New value of the username\. Use an empty string to remove the username\. The username can't be completely removed if there is another active or disabled username


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setSupergroupUsername",
            "supergroup_id": supergroup_id,
            "username": username,
        }

        return await self.invoke(data)

    async def toggleSupergroupUsernameIsActive(
        self, supergroup_id: int, username: str, is_active: bool
    ) -> Result:
        """Changes active state for a username of a supergroup or channel, requires owner privileges in the supergroup or channel\. The editable username can't be disabled\. May return an error with a message "USERNAMES\_ACTIVE\_TOO\_MUCH" if the maximum number of active usernames has been reached

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            username (``str``):
                The username to change

            is_active (``bool``):
                Pass true to activate the username; pass false to disable it


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupUsernameIsActive",
            "supergroup_id": supergroup_id,
            "username": username,
            "is_active": is_active,
        }

        return await self.invoke(data)

    async def disableAllSupergroupUsernames(self, supergroup_id: int) -> Result:
        """Disables all active non\-editable usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "disableAllSupergroupUsernames",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data)

    async def reorderSupergroupActiveUsernames(
        self, supergroup_id: int, usernames: list
    ) -> Result:
        """Changes order of active usernames of a supergroup or channel, requires owner privileges in the supergroup or channel

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            usernames (``list``):
                The new order of active usernames\. All currently active usernames must be specified


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reorderSupergroupActiveUsernames",
            "supergroup_id": supergroup_id,
            "usernames": usernames,
        }

        return await self.invoke(data)

    async def setSupergroupStickerSet(
        self, supergroup_id: int, sticker_set_id: int
    ) -> Result:
        """Changes the sticker set of a supergroup; requires can\_change\_info administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            sticker_set_id (``int``):
                New value of the supergroup sticker set identifier\. Use 0 to remove the supergroup sticker set


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setSupergroupStickerSet",
            "supergroup_id": supergroup_id,
            "sticker_set_id": sticker_set_id,
        }

        return await self.invoke(data)

    async def toggleSupergroupSignMessages(
        self, supergroup_id: int, sign_messages: bool
    ) -> Result:
        """Toggles whether sender signature is added to sent messages in a channel; requires can\_change\_info administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the channel

            sign_messages (``bool``):
                New value of sign\_messages


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupSignMessages",
            "supergroup_id": supergroup_id,
            "sign_messages": sign_messages,
        }

        return await self.invoke(data)

    async def toggleSupergroupJoinToSendMessages(
        self, supergroup_id: int, join_to_send_messages: bool
    ) -> Result:
        """Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can\_restrict\_members administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            join_to_send_messages (``bool``):
                New value of join\_to\_send\_messages


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupJoinToSendMessages",
            "supergroup_id": supergroup_id,
            "join_to_send_messages": join_to_send_messages,
        }

        return await self.invoke(data)

    async def toggleSupergroupJoinByRequest(
        self, supergroup_id: int, join_by_request: bool
    ) -> Result:
        """Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can\_restrict\_members administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the channel

            join_by_request (``bool``):
                New value of join\_by\_request


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupJoinByRequest",
            "supergroup_id": supergroup_id,
            "join_by_request": join_by_request,
        }

        return await self.invoke(data)

    async def toggleSupergroupIsAllHistoryAvailable(
        self, supergroup_id: int, is_all_history_available: bool
    ) -> Result:
        """Toggles whether the message history of a supergroup is available to new members; requires can\_change\_info administrator right

        Args:
            supergroup_id (``int``):
                The identifier of the supergroup

            is_all_history_available (``bool``):
                The new value of is\_all\_history\_available


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupIsAllHistoryAvailable",
            "supergroup_id": supergroup_id,
            "is_all_history_available": is_all_history_available,
        }

        return await self.invoke(data)

    async def toggleSupergroupHasHiddenMembers(
        self, supergroup_id: int, has_hidden_members: bool
    ) -> Result:
        """Toggles whether non\-administrators can receive only administrators and bots using getSupergroupMembers or searchChatMembers\. Can be called only if supergroupFullInfo\.can\_hide\_members \=\= true

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            has_hidden_members (``bool``):
                New value of has\_hidden\_members


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupHasHiddenMembers",
            "supergroup_id": supergroup_id,
            "has_hidden_members": has_hidden_members,
        }

        return await self.invoke(data)

    async def toggleSupergroupHasAggressiveAntiSpamEnabled(
        self, supergroup_id: int, has_aggressive_anti_spam_enabled: bool
    ) -> Result:
        """Toggles whether aggressive anti\-spam checks are enabled in the supergroup\. Can be called only if supergroupFullInfo\.can\_toggle\_aggressive\_anti\_spam \=\= true

        Args:
            supergroup_id (``int``):
                The identifier of the supergroup, which isn't a broadcast group

            has_aggressive_anti_spam_enabled (``bool``):
                The new value of has\_aggressive\_anti\_spam\_enabled


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupHasAggressiveAntiSpamEnabled",
            "supergroup_id": supergroup_id,
            "has_aggressive_anti_spam_enabled": has_aggressive_anti_spam_enabled,
        }

        return await self.invoke(data)

    async def toggleSupergroupIsForum(
        self, supergroup_id: int, is_forum: bool
    ) -> Result:
        """Toggles whether the supergroup is a forum; requires owner privileges in the supergroup\. Discussion supergroups can't be converted to forums

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            is_forum (``bool``):
                New value of is\_forum


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupIsForum",
            "supergroup_id": supergroup_id,
            "is_forum": is_forum,
        }

        return await self.invoke(data)

    async def toggleSupergroupIsBroadcastGroup(self, supergroup_id: int) -> Result:
        """Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "toggleSupergroupIsBroadcastGroup",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data)

    async def reportSupergroupSpam(
        self, supergroup_id: int, message_ids: list
    ) -> Result:
        """Reports messages in a supergroup as spam; requires administrator rights in the supergroup

        Args:
            supergroup_id (``int``):
                Supergroup identifier

            message_ids (``list``):
                Identifiers of messages to report


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportSupergroupSpam",
            "supergroup_id": supergroup_id,
            "message_ids": message_ids,
        }

        return await self.invoke(data)

    async def reportSupergroupAntiSpamFalsePositive(
        self, supergroup_id: int, message_id: int
    ) -> Result:
        """Reports a false deletion of a message by aggressive anti\-spam checks; requires administrator rights in the supergroup\. Can be called only for messages from chatEventMessageDeleted with can\_report\_anti\_spam\_false\_positive \=\= true

        Args:
            supergroup_id (``int``):
                Supergroup identifier

            message_id (``int``):
                Identifier of the erroneously deleted message


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportSupergroupAntiSpamFalsePositive",
            "supergroup_id": supergroup_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getSupergroupMembers(
        self, supergroup_id: int, offset: int, limit: int, filter: dict = None
    ) -> Result:
        """Returns information about members or banned users in a supergroup or channel\. Can be used only if supergroupFullInfo\.can\_get\_members \=\= true; additionally, administrator privileges may be required for some filters

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            offset (``int``):
                Number of users to skip

            limit (``int``):
                The maximum number of users be returned; up to 200

            filter (``SupergroupMembersFilter``, *optional*):
                The type of users to return; pass null to use supergroupMembersFilterRecent


        Returns:
            :class:`~pytdbot.types.Result` (``ChatMembers``)
        """

        data = {
            "@type": "getSupergroupMembers",
            "supergroup_id": supergroup_id,
            "filter": filter,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def closeSecretChat(self, secret_chat_id: int) -> Result:
        """Closes a secret chat, effectively transferring its state to secretChatStateClosed

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "closeSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data)

    async def getChatEventLog(
        self,
        chat_id: int,
        query: str,
        from_event_id: int,
        limit: int,
        user_ids: list,
        filters: dict = None,
    ) -> Result:
        """Returns a list of service actions taken by chat members and administrators in the last 48 hours\. Available only for supergroups and channels\. Requires administrator rights\. Returns results in reverse chronological order \(i\.e\., in order of decreasing event\_id\)

        Args:
            chat_id (``int``):
                Chat identifier

            query (``str``):
                Search query by which to filter events

            from_event_id (``int``):
                Identifier of an event from which to return results\. Use 0 to get results from the latest events

            limit (``int``):
                The maximum number of events to return; up to 100

            user_ids (``list``):
                User identifiers by which to filter events\. By default, events relating to all users will be returned

            filters (``chatEventLogFilters``, *optional*):
                The types of events to return; pass null to get chat events of all types


        Returns:
            :class:`~pytdbot.types.Result` (``ChatEvents``)
        """

        data = {
            "@type": "getChatEventLog",
            "chat_id": chat_id,
            "query": query,
            "from_event_id": from_event_id,
            "limit": limit,
            "filters": filters,
            "user_ids": user_ids,
        }

        return await self.invoke(data)

    async def getPaymentForm(self, input_invoice: dict, theme: dict = None) -> Result:
        """Returns an invoice payment form\. This method must be called when the user presses inline button of the type inlineKeyboardButtonTypeBuy

        Args:
            input_invoice (``InputInvoice``):
                The invoice

            theme (``themeParameters``, *optional*):
                Preferred payment form theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Result` (``PaymentForm``)
        """

        data = {
            "@type": "getPaymentForm",
            "input_invoice": input_invoice,
            "theme": theme,
        }

        return await self.invoke(data)

    async def validateOrderInfo(
        self, input_invoice: dict, allow_save: bool, order_info: dict = None
    ) -> Result:
        """Validates the order information provided by a user and returns the available shipping options for a flexible invoice

        Args:
            input_invoice (``InputInvoice``):
                The invoice

            allow_save (``bool``):
                Pass true to save the order information

            order_info (``orderInfo``, *optional*):
                The order information, provided by the user; pass null if empty


        Returns:
            :class:`~pytdbot.types.Result` (``ValidatedOrderInfo``)
        """

        data = {
            "@type": "validateOrderInfo",
            "input_invoice": input_invoice,
            "order_info": order_info,
            "allow_save": allow_save,
        }

        return await self.invoke(data)

    async def sendPaymentForm(
        self,
        input_invoice: dict,
        payment_form_id: int,
        order_info_id: str,
        shipping_option_id: str,
        credentials: dict,
        tip_amount: int,
    ) -> Result:
        """Sends a filled\-out payment form to the bot for final verification

        Args:
            input_invoice (``InputInvoice``):
                The invoice

            payment_form_id (``int``):
                Payment form identifier returned by getPaymentForm

            order_info_id (``str``):
                Identifier returned by validateOrderInfo, or an empty string

            shipping_option_id (``str``):
                Identifier of a chosen shipping option, if applicable

            credentials (``InputCredentials``):
                The credentials chosen by user for payment

            tip_amount (``int``):
                Chosen by the user amount of tip in the smallest units of the currency


        Returns:
            :class:`~pytdbot.types.Result` (``PaymentResult``)
        """

        data = {
            "@type": "sendPaymentForm",
            "input_invoice": input_invoice,
            "payment_form_id": payment_form_id,
            "order_info_id": order_info_id,
            "shipping_option_id": shipping_option_id,
            "credentials": credentials,
            "tip_amount": tip_amount,
        }

        return await self.invoke(data)

    async def getPaymentReceipt(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a successful payment

        Args:
            chat_id (``int``):
                Chat identifier of the messagePaymentSuccessful message

            message_id (``int``):
                Message identifier


        Returns:
            :class:`~pytdbot.types.Result` (``PaymentReceipt``)
        """

        data = {
            "@type": "getPaymentReceipt",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def getSavedOrderInfo(self) -> Result:
        """Returns saved order information\. Returns a 404 error if there is no saved order information


        Returns:
            :class:`~pytdbot.types.Result` (``OrderInfo``)
        """

        data = {
            "@type": "getSavedOrderInfo",
        }

        return await self.invoke(data)

    async def deleteSavedOrderInfo(self) -> Result:
        """Deletes saved order information


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteSavedOrderInfo",
        }

        return await self.invoke(data)

    async def deleteSavedCredentials(self) -> Result:
        """Deletes saved credentials for all payment provider bots


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteSavedCredentials",
        }

        return await self.invoke(data)

    async def createInvoiceLink(self, invoice: dict) -> Result:
        """Creates a link for the given invoice; for bots only

        Args:
            invoice (``InputMessageContent``):
                Information about the invoice of the type inputMessageInvoice


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "createInvoiceLink",
            "invoice": invoice,
        }

        return await self.invoke(data)

    async def getSupportUser(self) -> Result:
        """Returns a user that can be contacted to get support


        Returns:
            :class:`~pytdbot.types.Result` (``User``)
        """

        data = {
            "@type": "getSupportUser",
        }

        return await self.invoke(data)

    async def getBackgrounds(self, for_dark_theme: bool) -> Result:
        """Returns backgrounds installed by the user

        Args:
            for_dark_theme (``bool``):
                Pass true to order returned backgrounds for a dark theme


        Returns:
            :class:`~pytdbot.types.Result` (``Backgrounds``)
        """

        data = {
            "@type": "getBackgrounds",
            "for_dark_theme": for_dark_theme,
        }

        return await self.invoke(data)

    async def getBackgroundUrl(self, name: str, type: dict) -> Result:
        """Constructs a persistent HTTP URL for a background

        Args:
            name (``str``):
                Background name

            type (``BackgroundType``):
                Background type


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getBackgroundUrl",
            "name": name,
            "type": type,
        }

        return await self.invoke(data)

    async def searchBackground(self, name: str) -> Result:
        """Searches for a background by its name

        Args:
            name (``str``):
                The name of the background


        Returns:
            :class:`~pytdbot.types.Result` (``Background``)
        """

        data = {
            "@type": "searchBackground",
            "name": name,
        }

        return await self.invoke(data)

    async def setBackground(
        self, for_dark_theme: bool, background: dict = None, type: dict = None
    ) -> Result:
        """Changes the background selected by the user; adds background to the list of installed backgrounds

        Args:
            for_dark_theme (``bool``):
                Pass true if the background is changed for a dark theme

            background (``InputBackground``, *optional*):
                The input background to use; pass null to create a new filled background or to remove the current background

            type (``BackgroundType``, *optional*):
                Background type; pass null to use the default type of the remote background or to remove the current background


        Returns:
            :class:`~pytdbot.types.Result` (``Background``)
        """

        data = {
            "@type": "setBackground",
            "background": background,
            "type": type,
            "for_dark_theme": for_dark_theme,
        }

        return await self.invoke(data)

    async def removeBackground(self, background_id: int) -> Result:
        """Removes background from the list of installed backgrounds

        Args:
            background_id (``int``):
                The background identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeBackground",
            "background_id": background_id,
        }

        return await self.invoke(data)

    async def resetBackgrounds(self) -> Result:
        """Resets list of installed backgrounds to its default value


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "resetBackgrounds",
        }

        return await self.invoke(data)

    async def getLocalizationTargetInfo(self, only_local: bool) -> Result:
        """Returns information about the current localization target\. This is an offline request if only\_local is true\. Can be called before authorization

        Args:
            only_local (``bool``):
                Pass true to get only locally available information without sending network requests


        Returns:
            :class:`~pytdbot.types.Result` (``LocalizationTargetInfo``)
        """

        data = {
            "@type": "getLocalizationTargetInfo",
            "only_local": only_local,
        }

        return await self.invoke(data)

    async def getLanguagePackInfo(self, language_pack_id: str) -> Result:
        """Returns information about a language pack\. Returned language pack identifier may be different from a provided one\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier


        Returns:
            :class:`~pytdbot.types.Result` (``LanguagePackInfo``)
        """

        data = {
            "@type": "getLanguagePackInfo",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data)

    async def getLanguagePackStrings(self, language_pack_id: str, keys: list) -> Result:
        """Returns strings from a language pack in the current localization target by their keys\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier of the strings to be returned

            keys (``list``):
                Language pack keys of the strings to be returned; leave empty to request all available strings


        Returns:
            :class:`~pytdbot.types.Result` (``LanguagePackStrings``)
        """

        data = {
            "@type": "getLanguagePackStrings",
            "language_pack_id": language_pack_id,
            "keys": keys,
        }

        return await self.invoke(data)

    async def synchronizeLanguagePack(self, language_pack_id: str) -> Result:
        """Fetches the latest versions of all strings from a language pack in the current localization target from the server\. This method doesn't need to be called explicitly for the current used/base language packs\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "synchronizeLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data)

    async def addCustomServerLanguagePack(self, language_pack_id: str) -> Result:
        """Adds a custom server language pack to the list of installed language packs in current localization target\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of a language pack to be added


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addCustomServerLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data)

    async def setCustomLanguagePack(self, info: dict, strings: list) -> Result:
        """Adds or changes a custom local language pack to the current localization target

        Args:
            info (``languagePackInfo``):
                Information about the language pack\. Language pack identifier must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters\. Can be called before authorization

            strings (``list``):
                Strings of the new language pack


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setCustomLanguagePack",
            "info": info,
            "strings": strings,
        }

        return await self.invoke(data)

    async def editCustomLanguagePackInfo(self, info: dict) -> Result:
        """Edits information about a custom local language pack in the current localization target\. Can be called before authorization

        Args:
            info (``languagePackInfo``):
                New information about the custom local language pack


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "editCustomLanguagePackInfo",
            "info": info,
        }

        return await self.invoke(data)

    async def setCustomLanguagePackString(
        self, language_pack_id: str, new_string: dict
    ) -> Result:
        """Adds, edits or deletes a string in a custom local language pack\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of a previously added custom local language pack in the current localization target

            new_string (``languagePackString``):
                New language pack string


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setCustomLanguagePackString",
            "language_pack_id": language_pack_id,
            "new_string": new_string,
        }

        return await self.invoke(data)

    async def deleteLanguagePack(self, language_pack_id: str) -> Result:
        """Deletes all information about a language pack in the current localization target\. The language pack which is currently in use \(including base language pack\) or is being synchronized can't be deleted\. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of the language pack to delete


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data)

    async def registerDevice(self, device_token: dict, other_user_ids: list) -> Result:
        """Registers the currently used device for receiving push notifications\. Returns a globally unique identifier of the push notification subscription

        Args:
            device_token (``DeviceToken``):
                Device token

            other_user_ids (``list``):
                List of user identifiers of other users currently using the application


        Returns:
            :class:`~pytdbot.types.Result` (``PushReceiverId``)
        """

        data = {
            "@type": "registerDevice",
            "device_token": device_token,
            "other_user_ids": other_user_ids,
        }

        return await self.invoke(data)

    async def processPushNotification(self, payload: str) -> Result:
        """Handles a push notification\. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data\. Can be called before authorization

        Args:
            payload (``str``):
                JSON\-encoded push notification payload with all fields sent by the server, and "google\.sent\_time" and "google\.notification\.sound" fields added


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "processPushNotification",
            "payload": payload,
        }

        return await self.invoke(data)

    async def getPushReceiverId(self, payload: str) -> Result:
        """Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification\. Can be called synchronously

        Args:
            payload (``str``):
                JSON\-encoded push notification payload


        Returns:
            :class:`~pytdbot.types.Result` (``PushReceiverId``)
        """

        data = {
            "@type": "getPushReceiverId",
            "payload": payload,
        }

        return await self.invoke(data)

    async def getRecentlyVisitedTMeUrls(self, referrer: str) -> Result:
        """Returns t\.me URLs recently visited by a newly registered user

        Args:
            referrer (``str``):
                Google Play referrer to identify the user


        Returns:
            :class:`~pytdbot.types.Result` (``TMeUrls``)
        """

        data = {
            "@type": "getRecentlyVisitedTMeUrls",
            "referrer": referrer,
        }

        return await self.invoke(data)

    async def setUserPrivacySettingRules(self, setting: dict, rules: dict) -> Result:
        """Changes user privacy settings

        Args:
            setting (``UserPrivacySetting``):
                The privacy setting

            rules (``userPrivacySettingRules``):
                The new privacy rules


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setUserPrivacySettingRules",
            "setting": setting,
            "rules": rules,
        }

        return await self.invoke(data)

    async def getUserPrivacySettingRules(self, setting: dict) -> Result:
        """Returns the current privacy settings

        Args:
            setting (``UserPrivacySetting``):
                The privacy setting


        Returns:
            :class:`~pytdbot.types.Result` (``UserPrivacySettingRules``)
        """

        data = {
            "@type": "getUserPrivacySettingRules",
            "setting": setting,
        }

        return await self.invoke(data)

    async def getOption(self, name: str) -> Result:
        """Returns the value of an option by its name\. \(Check the list of available options on https://core\.telegram\.org/tdlib/options\.\) Can be called before authorization\. Can be called synchronously for options "version" and "commit\_hash"

        Args:
            name (``str``):
                The name of the option


        Returns:
            :class:`~pytdbot.types.Result` (``OptionValue``)
        """

        data = {
            "@type": "getOption",
            "name": name,
        }

        return await self.invoke(data)

    async def setOption(self, name: str, value: dict = None) -> Result:
        """Sets the value of an option\. \(Check the list of available options on https://core\.telegram\.org/tdlib/options\.\) Only writable options can be set\. Can be called before authorization

        Args:
            name (``str``):
                The name of the option

            value (``OptionValue``, *optional*):
                The new value of the option; pass null to reset option value to a default value


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setOption",
            "name": name,
            "value": value,
        }

        return await self.invoke(data)

    async def setAccountTtl(self, ttl: dict) -> Result:
        """Changes the period of inactivity after which the account of the current user will automatically be deleted

        Args:
            ttl (``accountTtl``):
                New account TTL


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAccountTtl",
            "ttl": ttl,
        }

        return await self.invoke(data)

    async def getAccountTtl(self) -> Result:
        """Returns the period of inactivity after which the account of the current user will automatically be deleted


        Returns:
            :class:`~pytdbot.types.Result` (``AccountTtl``)
        """

        data = {
            "@type": "getAccountTtl",
        }

        return await self.invoke(data)

    async def deleteAccount(self, reason: str, password: str) -> Result:
        """Deletes the account of the current user, deleting all information associated with the user from the server\. The phone number of the account can be used to create a new account\. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

        Args:
            reason (``str``):
                The reason why the account was deleted; optional

            password (``str``):
                The 2\-step verification password of the current user\. If not specified, account deletion can be canceled within one week


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteAccount",
            "reason": reason,
            "password": password,
        }

        return await self.invoke(data)

    async def setDefaultMessageAutoDeleteTime(
        self, message_auto_delete_time: dict
    ) -> Result:
        """Changes the default message auto\-delete time for new chats

        Args:
            message_auto_delete_time (``messageAutoDeleteTime``):
                New default message auto\-delete time; must be from 0 up to 365 \* 86400 and be divisible by 86400\. If 0, then messages aren't deleted automatically


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setDefaultMessageAutoDeleteTime",
            "message_auto_delete_time": message_auto_delete_time,
        }

        return await self.invoke(data)

    async def getDefaultMessageAutoDeleteTime(self) -> Result:
        """Returns default message auto\-delete time setting for new chats


        Returns:
            :class:`~pytdbot.types.Result` (``MessageAutoDeleteTime``)
        """

        data = {
            "@type": "getDefaultMessageAutoDeleteTime",
        }

        return await self.invoke(data)

    async def removeChatActionBar(self, chat_id: int) -> Result:
        """Removes a chat action bar without any other action

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeChatActionBar",
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def reportChat(
        self, chat_id: int, reason: dict, text: str, message_ids: list = None
    ) -> Result:
        """Reports a chat to the Telegram moderators\. A chat can be reported only from the chat action bar, or if chat\.can\_be\_reported

        Args:
            chat_id (``int``):
                Chat identifier

            reason (``ReportReason``):
                The reason for reporting the chat

            text (``str``):
                Additional report details; 0\-1024 characters

            message_ids (``list``, *optional*):
                Identifiers of reported messages; may be empty to report the whole chat


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportChat",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "reason": reason,
            "text": text,
        }

        return await self.invoke(data)

    async def reportChatPhoto(
        self, chat_id: int, file_id: int, reason: dict, text: str
    ) -> Result:
        """Reports a chat photo to the Telegram moderators\. A chat photo can be reported only if chat\.can\_be\_reported

        Args:
            chat_id (``int``):
                Chat identifier

            file_id (``int``):
                Identifier of the photo to report\. Only full photos from chatPhoto can be reported

            reason (``ReportReason``):
                The reason for reporting the chat photo

            text (``str``):
                Additional report details; 0\-1024 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportChatPhoto",
            "chat_id": chat_id,
            "file_id": file_id,
            "reason": reason,
            "text": text,
        }

        return await self.invoke(data)

    async def reportMessageReactions(
        self, chat_id: int, message_id: int, sender_id: dict
    ) -> Result:
        """Reports reactions set on a message to the Telegram moderators\. Reactions on a message can be reported only if message\.can\_report\_reactions

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier

            sender_id (``MessageSender``):
                Identifier of the sender, which added the reaction


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "reportMessageReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "sender_id": sender_id,
        }

        return await self.invoke(data)

    async def getChatStatistics(self, chat_id: int, is_dark: bool) -> Result:
        """Returns detailed statistics about a chat\. Currently, this method can be used only for supergroups and channels\. Can be used only if supergroupFullInfo\.can\_get\_statistics \=\= true

        Args:
            chat_id (``int``):
                Chat identifier

            is_dark (``bool``):
                Pass true if a dark theme is used by the application


        Returns:
            :class:`~pytdbot.types.Result` (``ChatStatistics``)
        """

        data = {
            "@type": "getChatStatistics",
            "chat_id": chat_id,
            "is_dark": is_dark,
        }

        return await self.invoke(data)

    async def getMessageStatistics(
        self, chat_id: int, message_id: int, is_dark: bool
    ) -> Result:
        """Returns detailed statistics about a message\. Can be used only if message\.can\_get\_statistics \=\= true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier

            is_dark (``bool``):
                Pass true if a dark theme is used by the application


        Returns:
            :class:`~pytdbot.types.Result` (``MessageStatistics``)
        """

        data = {
            "@type": "getMessageStatistics",
            "chat_id": chat_id,
            "message_id": message_id,
            "is_dark": is_dark,
        }

        return await self.invoke(data)

    async def getMessagePublicForwards(
        self, chat_id: int, message_id: int, offset: str, limit: int
    ) -> Result:
        """Returns forwarded copies of a channel message to different public channels\. Can be used only if message\.can\_get\_statistics \=\= true\. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Message identifier

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100\. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Result` (``FoundMessages``)
        """

        data = {
            "@type": "getMessagePublicForwards",
            "chat_id": chat_id,
            "message_id": message_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data)

    async def getStoryStatistics(
        self, chat_id: int, story_id: int, is_dark: bool
    ) -> Result:
        """Returns detailed statistics about a story\. Can be used only if story\.can\_get\_statistics \=\= true

        Args:
            chat_id (``int``):
                Chat identifier

            story_id (``int``):
                Story identifier

            is_dark (``bool``):
                Pass true if a dark theme is used by the application


        Returns:
            :class:`~pytdbot.types.Result` (``StoryStatistics``)
        """

        data = {
            "@type": "getStoryStatistics",
            "chat_id": chat_id,
            "story_id": story_id,
            "is_dark": is_dark,
        }

        return await self.invoke(data)

    async def getStatisticalGraph(self, chat_id: int, token: str, x: int) -> Result:
        """Loads an asynchronous or a zoomed in statistical graph

        Args:
            chat_id (``int``):
                Chat identifier

            token (``str``):
                The token for graph loading

            x (``int``):
                X\-value for zoomed in graph or 0 otherwise


        Returns:
            :class:`~pytdbot.types.Result` (``StatisticalGraph``)
        """

        data = {
            "@type": "getStatisticalGraph",
            "chat_id": chat_id,
            "token": token,
            "x": x,
        }

        return await self.invoke(data)

    async def getStorageStatistics(self, chat_limit: int) -> Result:
        """Returns storage usage statistics\. Can be called before authorization

        Args:
            chat_limit (``int``):
                The maximum number of chats with the largest storage usage for which separate statistics need to be returned\. All other chats will be grouped in entries with chat\_id \=\= 0\. If the chat info database is not used, the chat\_limit is ignored and is always set to 0


        Returns:
            :class:`~pytdbot.types.Result` (``StorageStatistics``)
        """

        data = {
            "@type": "getStorageStatistics",
            "chat_limit": chat_limit,
        }

        return await self.invoke(data)

    async def getStorageStatisticsFast(self) -> Result:
        """Quickly returns approximate storage usage statistics\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``StorageStatisticsFast``)
        """

        data = {
            "@type": "getStorageStatisticsFast",
        }

        return await self.invoke(data)

    async def getDatabaseStatistics(self) -> Result:
        """Returns database statistics


        Returns:
            :class:`~pytdbot.types.Result` (``DatabaseStatistics``)
        """

        data = {
            "@type": "getDatabaseStatistics",
        }

        return await self.invoke(data)

    async def optimizeStorage(
        self,
        size: int,
        ttl: int,
        count: int,
        immunity_delay: int,
        return_deleted_file_statistics: bool,
        chat_limit: int,
        file_types: list = None,
        chat_ids: list = None,
        exclude_chat_ids: list = None,
    ) -> Result:
        """Optimizes storage usage, i\.e\. deletes some files and returns new storage usage statistics\. Secret thumbnails can't be deleted

        Args:
            size (``int``):
                Limit on the total size of files after deletion, in bytes\. Pass \-1 to use the default limit

            ttl (``int``):
                Limit on the time that has passed since the last time a file was accessed \(or creation time for some filesystems\)\. Pass \-1 to use the default limit

            count (``int``):
                Limit on the total number of files after deletion\. Pass \-1 to use the default limit

            immunity_delay (``int``):
                The amount of time after the creation of a file during which it can't be deleted, in seconds\. Pass \-1 to use the default value

            return_deleted_file_statistics (``bool``):
                Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics\. Affects only returned statistics

            chat_limit (``int``):
                Same as in getStorageStatistics\. Affects only returned statistics

            file_types (``list``, *optional*):
                If non\-empty, only files with the given types are considered\. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted

            chat_ids (``list``, *optional*):
                If non\-empty, only files from the given chats are considered\. Use 0 as chat identifier to delete files not belonging to any chat \(e\.g\., profile photos\)

            exclude_chat_ids (``list``, *optional*):
                If non\-empty, files from the given chats are excluded\. Use 0 as chat identifier to exclude all files not belonging to any chat \(e\.g\., profile photos\)


        Returns:
            :class:`~pytdbot.types.Result` (``StorageStatistics``)
        """

        data = {
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

        return await self.invoke(data)

    async def setNetworkType(self, type: dict = None) -> Result:
        """Sets the current network type\. Can be called before authorization\. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same\. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics

        Args:
            type (``NetworkType``, *optional*):
                The new network type; pass null to set network type to networkTypeOther


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setNetworkType",
            "type": type,
        }

        return await self.invoke(data)

    async def getNetworkStatistics(self, only_current: bool) -> Result:
        """Returns network data usage statistics\. Can be called before authorization

        Args:
            only_current (``bool``):
                Pass true to get statistics only for the current library launch


        Returns:
            :class:`~pytdbot.types.Result` (``NetworkStatistics``)
        """

        data = {
            "@type": "getNetworkStatistics",
            "only_current": only_current,
        }

        return await self.invoke(data)

    async def addNetworkStatistics(self, entry: dict) -> Result:
        """Adds the specified data to data usage statistics\. Can be called before authorization

        Args:
            entry (``NetworkStatisticsEntry``):
                The network statistics entry with the data to be added to statistics


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addNetworkStatistics",
            "entry": entry,
        }

        return await self.invoke(data)

    async def resetNetworkStatistics(self) -> Result:
        """Resets all network data usage statistics to zero\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "resetNetworkStatistics",
        }

        return await self.invoke(data)

    async def getAutoDownloadSettingsPresets(self) -> Result:
        """Returns auto\-download settings presets for the current user


        Returns:
            :class:`~pytdbot.types.Result` (``AutoDownloadSettingsPresets``)
        """

        data = {
            "@type": "getAutoDownloadSettingsPresets",
        }

        return await self.invoke(data)

    async def setAutoDownloadSettings(self, settings: dict, type: dict) -> Result:
        """Sets auto\-download settings

        Args:
            settings (``autoDownloadSettings``):
                New user auto\-download settings

            type (``NetworkType``):
                Type of the network for which the new settings are relevant


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAutoDownloadSettings",
            "settings": settings,
            "type": type,
        }

        return await self.invoke(data)

    async def getAutosaveSettings(self) -> Result:
        """Returns autosave settings for the current user


        Returns:
            :class:`~pytdbot.types.Result` (``AutosaveSettings``)
        """

        data = {
            "@type": "getAutosaveSettings",
        }

        return await self.invoke(data)

    async def setAutosaveSettings(self, scope: dict, settings: dict = None) -> Result:
        """Sets autosave settings for the given scope\. The method is guaranteed to work only after at least one call to getAutosaveSettings

        Args:
            scope (``AutosaveSettingsScope``):
                Autosave settings scope

            settings (``scopeAutosaveSettings``, *optional*):
                New autosave settings for the scope; pass null to set autosave settings to default


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAutosaveSettings",
            "scope": scope,
            "settings": settings,
        }

        return await self.invoke(data)

    async def clearAutosaveSettingsExceptions(self) -> Result:
        """Clears the list of all autosave settings exceptions\. The method is guaranteed to work only after at least one call to getAutosaveSettings


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clearAutosaveSettingsExceptions",
        }

        return await self.invoke(data)

    async def getBankCardInfo(self, bank_card_number: str) -> Result:
        """Returns information about a bank card

        Args:
            bank_card_number (``str``):
                The bank card number


        Returns:
            :class:`~pytdbot.types.Result` (``BankCardInfo``)
        """

        data = {
            "@type": "getBankCardInfo",
            "bank_card_number": bank_card_number,
        }

        return await self.invoke(data)

    async def getPassportElement(self, type: dict, password: str) -> Result:
        """Returns one of the available Telegram Passport elements

        Args:
            type (``PassportElementType``):
                Telegram Passport element type

            password (``str``):
                The 2\-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``PassportElement``)
        """

        data = {
            "@type": "getPassportElement",
            "type": type,
            "password": password,
        }

        return await self.invoke(data)

    async def getAllPassportElements(self, password: str) -> Result:
        """Returns all available Telegram Passport elements

        Args:
            password (``str``):
                The 2\-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``PassportElements``)
        """

        data = {
            "@type": "getAllPassportElements",
            "password": password,
        }

        return await self.invoke(data)

    async def setPassportElement(self, element: dict, password: str) -> Result:
        """Adds an element to the user's Telegram Passport\. May return an error with a message "PHONE\_VERIFICATION\_NEEDED" or "EMAIL\_VERIFICATION\_NEEDED" if the chosen phone number or the chosen email address must be verified first

        Args:
            element (``InputPassportElement``):
                Input Telegram Passport element

            password (``str``):
                The 2\-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``PassportElement``)
        """

        data = {
            "@type": "setPassportElement",
            "element": element,
            "password": password,
        }

        return await self.invoke(data)

    async def deletePassportElement(self, type: dict) -> Result:
        """Deletes a Telegram Passport element

        Args:
            type (``PassportElementType``):
                Element type


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deletePassportElement",
            "type": type,
        }

        return await self.invoke(data)

    async def setPassportElementErrors(self, user_id: int, errors: list) -> Result:
        """Informs the user that some of the elements in their Telegram Passport contain errors; for bots only\. The user will not be able to resend the elements, until the errors are fixed

        Args:
            user_id (``int``):
                User identifier

            errors (``list``):
                The errors


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setPassportElementErrors",
            "user_id": user_id,
            "errors": errors,
        }

        return await self.invoke(data)

    async def getPreferredCountryLanguage(self, country_code: str) -> Result:
        """Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details\. Returns a 404 error if unknown

        Args:
            country_code (``str``):
                A two\-letter ISO 3166\-1 alpha\-2 country code


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getPreferredCountryLanguage",
            "country_code": country_code,
        }

        return await self.invoke(data)

    async def sendPhoneNumberVerificationCode(
        self, phone_number: str, settings: dict = None
    ) -> Result:
        """Sends a code to verify a phone number to be added to a user's Telegram Passport

        Args:
            phone_number (``str``):
                The phone number of the user, in international format

            settings (``phoneNumberAuthenticationSettings``, *optional*):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "sendPhoneNumberVerificationCode",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data)

    async def resendPhoneNumberVerificationCode(self) -> Result:
        """Resends the code to verify a phone number to be added to a user's Telegram Passport


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "resendPhoneNumberVerificationCode",
        }

        return await self.invoke(data)

    async def checkPhoneNumberVerificationCode(self, code: str) -> Result:
        """Checks the phone number verification code for Telegram Passport

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkPhoneNumberVerificationCode",
            "code": code,
        }

        return await self.invoke(data)

    async def sendEmailAddressVerificationCode(self, email_address: str) -> Result:
        """Sends a code to verify an email address to be added to a user's Telegram Passport

        Args:
            email_address (``str``):
                Email address


        Returns:
            :class:`~pytdbot.types.Result` (``EmailAddressAuthenticationCodeInfo``)
        """

        data = {
            "@type": "sendEmailAddressVerificationCode",
            "email_address": email_address,
        }

        return await self.invoke(data)

    async def resendEmailAddressVerificationCode(self) -> Result:
        """Resends the code to verify an email address to be added to a user's Telegram Passport


        Returns:
            :class:`~pytdbot.types.Result` (``EmailAddressAuthenticationCodeInfo``)
        """

        data = {
            "@type": "resendEmailAddressVerificationCode",
        }

        return await self.invoke(data)

    async def checkEmailAddressVerificationCode(self, code: str) -> Result:
        """Checks the email address verification code for Telegram Passport

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkEmailAddressVerificationCode",
            "code": code,
        }

        return await self.invoke(data)

    async def getPassportAuthorizationForm(
        self, bot_user_id: int, scope: str, public_key: str, nonce: str
    ) -> Result:
        """Returns a Telegram Passport authorization form for sharing data with a service

        Args:
            bot_user_id (``int``):
                User identifier of the service's bot

            scope (``str``):
                Telegram Passport element types requested by the service

            public_key (``str``):
                Service's public key

            nonce (``str``):
                Unique request identifier provided by the service


        Returns:
            :class:`~pytdbot.types.Result` (``PassportAuthorizationForm``)
        """

        data = {
            "@type": "getPassportAuthorizationForm",
            "bot_user_id": bot_user_id,
            "scope": scope,
            "public_key": public_key,
            "nonce": nonce,
        }

        return await self.invoke(data)

    async def getPassportAuthorizationFormAvailableElements(
        self, authorization_form_id: int, password: str
    ) -> Result:
        """Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form\. Result can be received only once for each authorization form

        Args:
            authorization_form_id (``int``):
                Authorization form identifier

            password (``str``):
                The 2\-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Result` (``PassportElementsWithErrors``)
        """

        data = {
            "@type": "getPassportAuthorizationFormAvailableElements",
            "authorization_form_id": authorization_form_id,
            "password": password,
        }

        return await self.invoke(data)

    async def sendPassportAuthorizationForm(
        self, authorization_form_id: int, types: list
    ) -> Result:
        """Sends a Telegram Passport authorization form, effectively sharing data with the service\. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused

        Args:
            authorization_form_id (``int``):
                Authorization form identifier

            types (``list``):
                Types of Telegram Passport elements chosen by user to complete the authorization form


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "sendPassportAuthorizationForm",
            "authorization_form_id": authorization_form_id,
            "types": types,
        }

        return await self.invoke(data)

    async def sendPhoneNumberConfirmationCode(
        self, hash: str, phone_number: str, settings: dict = None
    ) -> Result:
        """Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation

        Args:
            hash (``str``):
                Hash value from the link

            phone_number (``str``):
                Phone number value from the link

            settings (``phoneNumberAuthenticationSettings``, *optional*):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "sendPhoneNumberConfirmationCode",
            "hash": hash,
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data)

    async def resendPhoneNumberConfirmationCode(self) -> Result:
        """Resends phone number confirmation code


        Returns:
            :class:`~pytdbot.types.Result` (``AuthenticationCodeInfo``)
        """

        data = {
            "@type": "resendPhoneNumberConfirmationCode",
        }

        return await self.invoke(data)

    async def checkPhoneNumberConfirmationCode(self, code: str) -> Result:
        """Checks phone number confirmation code

        Args:
            code (``str``):
                Confirmation code to check


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "checkPhoneNumberConfirmationCode",
            "code": code,
        }

        return await self.invoke(data)

    async def setBotUpdatesStatus(
        self, pending_update_count: int, error_message: str
    ) -> Result:
        """Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only

        Args:
            pending_update_count (``int``):
                The number of pending updates

            error_message (``str``):
                The last error message


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setBotUpdatesStatus",
            "pending_update_count": pending_update_count,
            "error_message": error_message,
        }

        return await self.invoke(data)

    async def uploadStickerFile(
        self, user_id: int, sticker_format: dict, sticker: dict
    ) -> Result:
        """Uploads a file with a sticker; returns the uploaded file

        Args:
            user_id (``int``):
                Sticker file owner; ignored for regular users

            sticker_format (``StickerFormat``):
                Sticker format

            sticker (``InputFile``):
                File file to upload; must fit in a 512x512 square\. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server\-side\. See https://core\.telegram\.org/animated\_stickers\#technical\-requirements for technical requirements


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "uploadStickerFile",
            "user_id": user_id,
            "sticker_format": sticker_format,
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def getSuggestedStickerSetName(self, title: str) -> Result:
        """Returns a suggested name for a new sticker set with a given title

        Args:
            title (``str``):
                Sticker set title; 1\-64 characters


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getSuggestedStickerSetName",
            "title": title,
        }

        return await self.invoke(data)

    async def checkStickerSetName(self, name: str) -> Result:
        """Checks whether a name can be used for a new sticker set

        Args:
            name (``str``):
                Name to be checked


        Returns:
            :class:`~pytdbot.types.Result` (``CheckStickerSetNameResult``)
        """

        data = {
            "@type": "checkStickerSetName",
            "name": name,
        }

        return await self.invoke(data)

    async def createNewStickerSet(
        self,
        user_id: int,
        title: str,
        name: str,
        sticker_format: dict,
        sticker_type: dict,
        needs_repainting: bool,
        stickers: list,
        source: str = None,
    ) -> Result:
        """Creates a new sticker set\. Returns the newly created sticker set

        Args:
            user_id (``int``):
                Sticker set owner; ignored for regular users

            title (``str``):
                Sticker set title; 1\-64 characters

            name (``str``):
                Sticker set name\. Can contain only English letters, digits and underscores\. Must end with \*"\_by\_<bot username\>"\* \(\*<bot\_username\>\* is case insensitive\) for bots; 1\-64 characters

            sticker_format (``StickerFormat``):
                Format of the stickers in the set

            sticker_type (``StickerType``):
                Type of the stickers in the set

            needs_repainting (``bool``):
                Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only

            stickers (``list``):
                List of stickers to be added to the set; must be non\-empty\. All stickers must have the same format\. For TGS stickers, uploadStickerFile must be used before the sticker is shown

            source (``str``, *optional*):
                Source of the sticker set; may be empty if unknown


        Returns:
            :class:`~pytdbot.types.Result` (``StickerSet``)
        """

        data = {
            "@type": "createNewStickerSet",
            "user_id": user_id,
            "title": title,
            "name": name,
            "sticker_format": sticker_format,
            "sticker_type": sticker_type,
            "needs_repainting": needs_repainting,
            "stickers": stickers,
            "source": source,
        }

        return await self.invoke(data)

    async def addStickerToSet(self, user_id: int, name: str, sticker: dict) -> Result:
        """Adds a new sticker to a set; for bots only

        Args:
            user_id (``int``):
                Sticker set owner

            name (``str``):
                Sticker set name

            sticker (``inputSticker``):
                Sticker to add to the set


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addStickerToSet",
            "user_id": user_id,
            "name": name,
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def setStickerSetThumbnail(
        self, user_id: int, name: str, thumbnail: dict = None
    ) -> Result:
        """Sets a sticker set thumbnail; for bots only

        Args:
            user_id (``int``):
                Sticker set owner

            name (``str``):
                Sticker set name

            thumbnail (``InputFile``, *optional*):
                Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail\. Thumbnail format must match the format of stickers in the set


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerSetThumbnail",
            "user_id": user_id,
            "name": name,
            "thumbnail": thumbnail,
        }

        return await self.invoke(data)

    async def setCustomEmojiStickerSetThumbnail(
        self, name: str, custom_emoji_id: int
    ) -> Result:
        """Sets a custom emoji sticker set thumbnail; for bots only

        Args:
            name (``str``):
                Sticker set name

            custom_emoji_id (``int``):
                Identifier of the custom emoji from the sticker set, which will be set as sticker set thumbnail; pass 0 to remove the sticker set thumbnail


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setCustomEmojiStickerSetThumbnail",
            "name": name,
            "custom_emoji_id": custom_emoji_id,
        }

        return await self.invoke(data)

    async def setStickerSetTitle(self, name: str, title: str) -> Result:
        """Sets a sticker set title; for bots only

        Args:
            name (``str``):
                Sticker set name

            title (``str``):
                New sticker set title


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerSetTitle",
            "name": name,
            "title": title,
        }

        return await self.invoke(data)

    async def deleteStickerSet(self, name: str) -> Result:
        """Deleted a sticker set; for bots only

        Args:
            name (``str``):
                Sticker set name


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "deleteStickerSet",
            "name": name,
        }

        return await self.invoke(data)

    async def setStickerPositionInSet(self, sticker: dict, position: int) -> Result:
        """Changes the position of a sticker in the set to which it belongs; for bots only\. The sticker set must have been created by the bot

        Args:
            sticker (``InputFile``):
                Sticker

            position (``int``):
                New position of the sticker in the set, 0\-based


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerPositionInSet",
            "sticker": sticker,
            "position": position,
        }

        return await self.invoke(data)

    async def removeStickerFromSet(self, sticker: dict) -> Result:
        """Removes a sticker from the set to which it belongs; for bots only\. The sticker set must have been created by the bot

        Args:
            sticker (``InputFile``):
                Sticker


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeStickerFromSet",
            "sticker": sticker,
        }

        return await self.invoke(data)

    async def setStickerEmojis(self, sticker: dict, emojis: str) -> Result:
        """Changes the list of emoji corresponding to a sticker; for bots only\. The sticker must belong to a regular or custom emoji sticker set created by the bot

        Args:
            sticker (``InputFile``):
                Sticker

            emojis (``str``):
                New string with 1\-20 emoji corresponding to the sticker


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerEmojis",
            "sticker": sticker,
            "emojis": emojis,
        }

        return await self.invoke(data)

    async def setStickerKeywords(self, sticker: dict, keywords: list) -> Result:
        """Changes the list of keywords of a sticker; for bots only\. The sticker must belong to a regular or custom emoji sticker set created by the bot

        Args:
            sticker (``InputFile``):
                Sticker

            keywords (``list``):
                List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerKeywords",
            "sticker": sticker,
            "keywords": keywords,
        }

        return await self.invoke(data)

    async def setStickerMaskPosition(
        self, sticker: dict, mask_position: dict = None
    ) -> Result:
        """Changes the mask position of a mask sticker; for bots only\. The sticker must belong to a mask sticker set created by the bot

        Args:
            sticker (``InputFile``):
                Sticker

            mask_position (``maskPosition``, *optional*):
                Position where the mask is placed; pass null to remove mask position


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setStickerMaskPosition",
            "sticker": sticker,
            "mask_position": mask_position,
        }

        return await self.invoke(data)

    async def getMapThumbnailFile(
        self,
        location: dict,
        zoom: int,
        width: int,
        height: int,
        scale: int,
        chat_id: int,
    ) -> Result:
        """Returns information about a file with a map thumbnail in PNG format\. Only map thumbnail files with size less than 1MB can be downloaded

        Args:
            location (``location``):
                Location of the map center

            zoom (``int``):
                Map zoom level; 13\-20

            width (``int``):
                Map width in pixels before applying scale; 16\-1024

            height (``int``):
                Map height in pixels before applying scale; 16\-1024

            scale (``int``):
                Map scale; 1\-3

            chat_id (``int``):
                Identifier of a chat in which the thumbnail will be shown\. Use 0 if unknown


        Returns:
            :class:`~pytdbot.types.Result` (``File``)
        """

        data = {
            "@type": "getMapThumbnailFile",
            "location": location,
            "zoom": zoom,
            "width": width,
            "height": height,
            "scale": scale,
            "chat_id": chat_id,
        }

        return await self.invoke(data)

    async def getPremiumLimit(self, limit_type: dict) -> Result:
        """Returns information about a limit, increased for Premium users\. Returns a 404 error if the limit is unknown

        Args:
            limit_type (``PremiumLimitType``):
                Type of the limit


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumLimit``)
        """

        data = {
            "@type": "getPremiumLimit",
            "limit_type": limit_type,
        }

        return await self.invoke(data)

    async def getPremiumFeatures(self, source: dict = None) -> Result:
        """Returns information about features, available to Premium users

        Args:
            source (``PremiumSource``, *optional*):
                Source of the request; pass null if the method is called from some non\-standard source


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumFeatures``)
        """

        data = {
            "@type": "getPremiumFeatures",
            "source": source,
        }

        return await self.invoke(data)

    async def getPremiumStickerExamples(self) -> Result:
        """Returns examples of premium stickers for demonstration purposes


        Returns:
            :class:`~pytdbot.types.Result` (``Stickers``)
        """

        data = {
            "@type": "getPremiumStickerExamples",
        }

        return await self.invoke(data)

    async def viewPremiumFeature(self, feature: dict) -> Result:
        """Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

        Args:
            feature (``PremiumFeature``):
                The viewed premium feature


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "viewPremiumFeature",
            "feature": feature,
        }

        return await self.invoke(data)

    async def clickPremiumSubscriptionButton(self) -> Result:
        """Informs TDLib that the user clicked Premium subscription button on the Premium features screen


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "clickPremiumSubscriptionButton",
        }

        return await self.invoke(data)

    async def getPremiumState(self) -> Result:
        """Returns state of Telegram Premium subscription and promotion videos for Premium features


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumState``)
        """

        data = {
            "@type": "getPremiumState",
        }

        return await self.invoke(data)

    async def getPremiumGiftCodePaymentOptions(self, boosted_chat_id: int) -> Result:
        """Returns available options for Telegram Premium gift code or giveaway creation

        Args:
            boosted_chat_id (``int``):
                Identifier of the channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user; 0 if none


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumGiftCodePaymentOptions``)
        """

        data = {
            "@type": "getPremiumGiftCodePaymentOptions",
            "boosted_chat_id": boosted_chat_id,
        }

        return await self.invoke(data)

    async def checkPremiumGiftCode(self, code: str) -> Result:
        """Return information about a Telegram Premium gift code

        Args:
            code (``str``):
                The code to check


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumGiftCodeInfo``)
        """

        data = {
            "@type": "checkPremiumGiftCode",
            "code": code,
        }

        return await self.invoke(data)

    async def applyPremiumGiftCode(self, code: str) -> Result:
        """Applies a Telegram Premium gift code

        Args:
            code (``str``):
                The code to apply


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "applyPremiumGiftCode",
            "code": code,
        }

        return await self.invoke(data)

    async def launchPrepaidPremiumGiveaway(
        self, giveaway_id: int, parameters: dict
    ) -> Result:
        """Launches a prepaid Telegram Premium giveaway for subscribers of channel chats; requires can\_post\_messages rights in the channels

        Args:
            giveaway_id (``int``):
                Unique identifier of the prepaid giveaway

            parameters (``premiumGiveawayParameters``):
                Giveaway parameters


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "launchPrepaidPremiumGiveaway",
            "giveaway_id": giveaway_id,
            "parameters": parameters,
        }

        return await self.invoke(data)

    async def getPremiumGiveawayInfo(self, chat_id: int, message_id: int) -> Result:
        """Returns information about a Telegram Premium giveaway

        Args:
            chat_id (``int``):
                Identifier of the channel chat which started the giveaway

            message_id (``int``):
                Identifier of the giveaway message in the chat


        Returns:
            :class:`~pytdbot.types.Result` (``PremiumGiveawayInfo``)
        """

        data = {
            "@type": "getPremiumGiveawayInfo",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data)

    async def canPurchasePremium(self, purpose: dict) -> Result:
        """Checks whether Telegram Premium purchase is possible\. Must be called before in\-store Premium purchase

        Args:
            purpose (``StorePaymentPurpose``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "canPurchasePremium",
            "purpose": purpose,
        }

        return await self.invoke(data)

    async def assignAppStoreTransaction(self, receipt: bytes, purpose: dict) -> Result:
        """Informs server about a purchase through App Store\. For official applications only

        Args:
            receipt (``bytes``):
                App Store receipt

            purpose (``StorePaymentPurpose``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "assignAppStoreTransaction",
            "receipt": receipt,
            "purpose": purpose,
        }

        return await self.invoke(data)

    async def assignGooglePlayTransaction(
        self,
        package_name: str,
        store_product_id: str,
        purchase_token: str,
        purpose: dict,
    ) -> Result:
        """Informs server about a purchase through Google Play\. For official applications only

        Args:
            package_name (``str``):
                Application package name

            store_product_id (``str``):
                Identifier of the purchased store product

            purchase_token (``str``):
                Google Play purchase token

            purpose (``StorePaymentPurpose``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "assignGooglePlayTransaction",
            "package_name": package_name,
            "store_product_id": store_product_id,
            "purchase_token": purchase_token,
            "purpose": purpose,
        }

        return await self.invoke(data)

    async def acceptTermsOfService(self, terms_of_service_id: str) -> Result:
        """Accepts Telegram terms of services

        Args:
            terms_of_service_id (``str``):
                Terms of service identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "acceptTermsOfService",
            "terms_of_service_id": terms_of_service_id,
        }

        return await self.invoke(data)

    async def searchStringsByPrefix(
        self, strings: list, query: str, limit: int, return_none_for_empty_query: bool
    ) -> Result:
        """Searches specified query by word prefixes in the provided strings\. Returns 0\-based positions of strings that matched\. Can be called synchronously

        Args:
            strings (``list``):
                The strings to search in for the query

            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of objects to return

            return_none_for_empty_query (``bool``):
                Pass true to receive no results for an empty query


        Returns:
            :class:`~pytdbot.types.Result` (``FoundPositions``)
        """

        data = {
            "@type": "searchStringsByPrefix",
            "strings": strings,
            "query": query,
            "limit": limit,
            "return_none_for_empty_query": return_none_for_empty_query,
        }

        return await self.invoke(data)

    async def sendCustomRequest(self, method: str, parameters: str) -> Result:
        """Sends a custom request; for bots only

        Args:
            method (``str``):
                The method name

            parameters (``str``):
                JSON\-serialized method parameters


        Returns:
            :class:`~pytdbot.types.Result` (``CustomRequestResult``)
        """

        data = {
            "@type": "sendCustomRequest",
            "method": method,
            "parameters": parameters,
        }

        return await self.invoke(data)

    async def answerCustomQuery(self, custom_query_id: int, data: str) -> Result:
        """Answers a custom query; for bots only

        Args:
            custom_query_id (``int``):
                Identifier of a custom query

            data (``str``):
                JSON\-serialized answer to the query


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "answerCustomQuery",
            "custom_query_id": custom_query_id,
            "data": data,
        }

        return await self.invoke(data)

    async def setAlarm(self, seconds: float) -> Result:
        """Succeeds after a specified amount of time has passed\. Can be called before initialization

        Args:
            seconds (``float``):
                Number of seconds before the function returns


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setAlarm",
            "seconds": seconds,
        }

        return await self.invoke(data)

    async def getCountries(self) -> Result:
        """Returns information about existing countries\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Countries``)
        """

        data = {
            "@type": "getCountries",
        }

        return await self.invoke(data)

    async def getCountryCode(self) -> Result:
        """Uses the current IP address to find the current country\. Returns two\-letter ISO 3166\-1 alpha\-2 country code\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getCountryCode",
        }

        return await self.invoke(data)

    async def getPhoneNumberInfo(self, phone_number_prefix: str) -> Result:
        """Returns information about a phone number by its prefix\. Can be called before authorization

        Args:
            phone_number_prefix (``str``):
                The phone number prefix


        Returns:
            :class:`~pytdbot.types.Result` (``PhoneNumberInfo``)
        """

        data = {
            "@type": "getPhoneNumberInfo",
            "phone_number_prefix": phone_number_prefix,
        }

        return await self.invoke(data)

    async def getPhoneNumberInfoSync(
        self, language_code: str, phone_number_prefix: str
    ) -> Result:
        """Returns information about a phone number by its prefix synchronously\. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected\. Can be called synchronously

        Args:
            language_code (``str``):
                A two\-letter ISO 639\-1 language code for country information localization

            phone_number_prefix (``str``):
                The phone number prefix


        Returns:
            :class:`~pytdbot.types.Result` (``PhoneNumberInfo``)
        """

        data = {
            "@type": "getPhoneNumberInfoSync",
            "language_code": language_code,
            "phone_number_prefix": phone_number_prefix,
        }

        return await self.invoke(data)

    async def getDeepLinkInfo(self, link: str) -> Result:
        """Returns information about a tg:// deep link\. Use "tg://need\_update\_for\_some\_feature" or "tg:some\_unsupported\_feature" for testing\. Returns a 404 error for unknown links\. Can be called before authorization

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Result` (``DeepLinkInfo``)
        """

        data = {
            "@type": "getDeepLinkInfo",
            "link": link,
        }

        return await self.invoke(data)

    async def getApplicationConfig(self) -> Result:
        """Returns application config, provided by the server\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``JsonValue``)
        """

        data = {
            "@type": "getApplicationConfig",
        }

        return await self.invoke(data)

    async def addApplicationChangelog(
        self, previous_application_version: str
    ) -> Result:
        """Adds server\-provided application changelog as messages to the chat 777000 \(Telegram\) or as a stories; for official applications only\. Returns a 404 error if nothing changed

        Args:
            previous_application_version (``str``):
                The previous application version


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addApplicationChangelog",
            "previous_application_version": previous_application_version,
        }

        return await self.invoke(data)

    async def saveApplicationLogEvent(
        self, type: str, chat_id: int, data: dict
    ) -> Result:
        """Saves application log event on the server\. Can be called before authorization

        Args:
            type (``str``):
                Event type

            chat_id (``int``):
                Optional chat identifier, associated with the event

            data (``JsonValue``):
                The log event data


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "saveApplicationLogEvent",
            "type": type,
            "chat_id": chat_id,
            "data": data,
        }

        return await self.invoke(data)

    async def getApplicationDownloadLink(self) -> Result:
        """Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getApplicationDownloadLink",
        }

        return await self.invoke(data)

    async def addProxy(
        self, server: str, port: int, enable: bool, type: dict
    ) -> Result:
        """Adds a proxy server for network requests\. Can be called before authorization

        Args:
            server (``str``):
                Proxy server domain or IP address

            port (``int``):
                Proxy server port

            enable (``bool``):
                Pass true to immediately enable the proxy

            type (``ProxyType``):
                Proxy type


        Returns:
            :class:`~pytdbot.types.Result` (``Proxy``)
        """

        data = {
            "@type": "addProxy",
            "server": server,
            "port": port,
            "enable": enable,
            "type": type,
        }

        return await self.invoke(data)

    async def editProxy(
        self, proxy_id: int, server: str, port: int, enable: bool, type: dict
    ) -> Result:
        """Edits an existing proxy server for network requests\. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier

            server (``str``):
                Proxy server domain or IP address

            port (``int``):
                Proxy server port

            enable (``bool``):
                Pass true to immediately enable the proxy

            type (``ProxyType``):
                Proxy type


        Returns:
            :class:`~pytdbot.types.Result` (``Proxy``)
        """

        data = {
            "@type": "editProxy",
            "proxy_id": proxy_id,
            "server": server,
            "port": port,
            "enable": enable,
            "type": type,
        }

        return await self.invoke(data)

    async def enableProxy(self, proxy_id: int) -> Result:
        """Enables a proxy\. Only one proxy can be enabled at a time\. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "enableProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data)

    async def disableProxy(self) -> Result:
        """Disables the currently enabled proxy\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "disableProxy",
        }

        return await self.invoke(data)

    async def removeProxy(self, proxy_id: int) -> Result:
        """Removes a proxy server\. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "removeProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data)

    async def getProxies(self) -> Result:
        """Returns list of proxies that are currently set up\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Proxies``)
        """

        data = {
            "@type": "getProxies",
        }

        return await self.invoke(data)

    async def getProxyLink(self, proxy_id: int) -> Result:
        """Returns an HTTPS link, which can be used to add a proxy\. Available only for SOCKS5 and MTProto proxies\. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Result` (``HttpUrl``)
        """

        data = {
            "@type": "getProxyLink",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data)

    async def pingProxy(self, proxy_id: int) -> Result:
        """Computes time needed to receive a response from a Telegram server through a proxy\. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier\. Use 0 to ping a Telegram server without a proxy


        Returns:
            :class:`~pytdbot.types.Result` (``Seconds``)
        """

        data = {
            "@type": "pingProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data)

    async def setLogStream(self, log_stream: dict) -> Result:
        """Sets new log stream for internal logging of TDLib\. Can be called synchronously

        Args:
            log_stream (``LogStream``):
                New log stream


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setLogStream",
            "log_stream": log_stream,
        }

        return await self.invoke(data)

    async def getLogStream(self) -> Result:
        """Returns information about currently used log stream for internal logging of TDLib\. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Result` (``LogStream``)
        """

        data = {
            "@type": "getLogStream",
        }

        return await self.invoke(data)

    async def setLogVerbosityLevel(self, new_verbosity_level: int) -> Result:
        """Sets the verbosity level of the internal logging of TDLib\. Can be called synchronously

        Args:
            new_verbosity_level (``int``):
                New value of the verbosity level for logging\. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setLogVerbosityLevel",
            "new_verbosity_level": new_verbosity_level,
        }

        return await self.invoke(data)

    async def getLogVerbosityLevel(self) -> Result:
        """Returns current verbosity level of the internal logging of TDLib\. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Result` (``LogVerbosityLevel``)
        """

        data = {
            "@type": "getLogVerbosityLevel",
        }

        return await self.invoke(data)

    async def getLogTags(self) -> Result:
        """Returns list of available TDLib internal log tags, for example, \["actor", "binlog", "connections", "notifications", "proxy"\]\. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Result` (``LogTags``)
        """

        data = {
            "@type": "getLogTags",
        }

        return await self.invoke(data)

    async def setLogTagVerbosityLevel(
        self, tag: str, new_verbosity_level: int
    ) -> Result:
        """Sets the verbosity level for a specified TDLib internal log tag\. Can be called synchronously

        Args:
            tag (``str``):
                Logging tag to change verbosity level

            new_verbosity_level (``int``):
                New verbosity level; 1\-1024


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "setLogTagVerbosityLevel",
            "tag": tag,
            "new_verbosity_level": new_verbosity_level,
        }

        return await self.invoke(data)

    async def getLogTagVerbosityLevel(self, tag: str) -> Result:
        """Returns current verbosity level for a specified TDLib internal log tag\. Can be called synchronously

        Args:
            tag (``str``):
                Logging tag to change verbosity level


        Returns:
            :class:`~pytdbot.types.Result` (``LogVerbosityLevel``)
        """

        data = {
            "@type": "getLogTagVerbosityLevel",
            "tag": tag,
        }

        return await self.invoke(data)

    async def addLogMessage(self, verbosity_level: int, text: str) -> Result:
        """Adds a message to TDLib internal log\. Can be called synchronously

        Args:
            verbosity_level (``int``):
                The minimum verbosity level needed for the message to be logged; 0\-1023

            text (``str``):
                Text of a message to log


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "addLogMessage",
            "verbosity_level": verbosity_level,
            "text": text,
        }

        return await self.invoke(data)

    async def getUserSupportInfo(self, user_id: int) -> Result:
        """Returns support information for the given user; for Telegram support only

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Result` (``UserSupportInfo``)
        """

        data = {
            "@type": "getUserSupportInfo",
            "user_id": user_id,
        }

        return await self.invoke(data)

    async def setUserSupportInfo(self, user_id: int, message: dict) -> Result:
        """Sets support information for the given user; for Telegram support only

        Args:
            user_id (``int``):
                User identifier

            message (``formattedText``):
                New information message


        Returns:
            :class:`~pytdbot.types.Result` (``UserSupportInfo``)
        """

        data = {
            "@type": "setUserSupportInfo",
            "user_id": user_id,
            "message": message,
        }

        return await self.invoke(data)

    async def getSupportName(self) -> Result:
        """Returns localized name of the Telegram support user; for Telegram support only


        Returns:
            :class:`~pytdbot.types.Result` (``Text``)
        """

        data = {
            "@type": "getSupportName",
        }

        return await self.invoke(data)

    async def testCallEmpty(self) -> Result:
        """Does nothing; for testing only\. This is an offline method\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "testCallEmpty",
        }

        return await self.invoke(data)

    async def testCallString(self, x: str) -> Result:
        """Returns the received string; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``str``):
                String to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestString``)
        """

        data = {
            "@type": "testCallString",
            "x": x,
        }

        return await self.invoke(data)

    async def testCallBytes(self, x: bytes) -> Result:
        """Returns the received bytes; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``bytes``):
                Bytes to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestBytes``)
        """

        data = {
            "@type": "testCallBytes",
            "x": x,
        }

        return await self.invoke(data)

    async def testCallVectorInt(self, x: list) -> Result:
        """Returns the received vector of numbers; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``list``):
                Vector of numbers to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestVectorInt``)
        """

        data = {
            "@type": "testCallVectorInt",
            "x": x,
        }

        return await self.invoke(data)

    async def testCallVectorIntObject(self, x: list) -> Result:
        """Returns the received vector of objects containing a number; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``list``):
                Vector of objects to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestVectorIntObject``)
        """

        data = {
            "@type": "testCallVectorIntObject",
            "x": x,
        }

        return await self.invoke(data)

    async def testCallVectorString(self, x: list) -> Result:
        """Returns the received vector of strings; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``list``):
                Vector of strings to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestVectorString``)
        """

        data = {
            "@type": "testCallVectorString",
            "x": x,
        }

        return await self.invoke(data)

    async def testCallVectorStringObject(self, x: list) -> Result:
        """Returns the received vector of objects containing a string; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``list``):
                Vector of objects to return


        Returns:
            :class:`~pytdbot.types.Result` (``TestVectorStringObject``)
        """

        data = {
            "@type": "testCallVectorStringObject",
            "x": x,
        }

        return await self.invoke(data)

    async def testSquareInt(self, x: int) -> Result:
        """Returns the squared received number; for testing only\. This is an offline method\. Can be called before authorization

        Args:
            x (``int``):
                Number to square


        Returns:
            :class:`~pytdbot.types.Result` (``TestInt``)
        """

        data = {
            "@type": "testSquareInt",
            "x": x,
        }

        return await self.invoke(data)

    async def testNetwork(self) -> Result:
        """Sends a simple network request to the Telegram servers; for testing only\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "testNetwork",
        }

        return await self.invoke(data)

    async def testProxy(
        self, server: str, port: int, type: dict, dc_id: int, timeout: float
    ) -> Result:
        """Sends a simple network request to the Telegram servers via proxy; for testing only\. Can be called before authorization

        Args:
            server (``str``):
                Proxy server domain or IP address

            port (``int``):
                Proxy server port

            type (``ProxyType``):
                Proxy type

            dc_id (``int``):
                Identifier of a datacenter with which to test connection

            timeout (``float``):
                The maximum overall timeout for the request


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "testProxy",
            "server": server,
            "port": port,
            "type": type,
            "dc_id": dc_id,
            "timeout": timeout,
        }

        return await self.invoke(data)

    async def testGetDifference(self) -> Result:
        """Forces an updates\.getDifference call to the Telegram servers; for testing only


        Returns:
            :class:`~pytdbot.types.Result` (``Ok``)
        """

        data = {
            "@type": "testGetDifference",
        }

        return await self.invoke(data)

    async def testUseUpdate(self) -> Result:
        """Does nothing and ensures that the Update object is used; for testing only\. This is an offline method\. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Result` (``Update``)
        """

        data = {
            "@type": "testUseUpdate",
        }

        return await self.invoke(data)

    async def testReturnError(self, error: dict) -> Result:
        """Returns the specified error and ensures that the Error object is used; for testing only\. Can be called synchronously

        Args:
            error (``error``):
                The error to be returned


        Returns:
            :class:`~pytdbot.types.Result` (``Error``)
        """

        data = {
            "@type": "testReturnError",
            "error": error,
        }

        return await self.invoke(data)
