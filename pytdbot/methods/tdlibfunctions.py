from ..types import Response


class TDLibFunctions:
    """Auto generated tdlib functions"""

    async def getAuthorizationState(self, timeout: float = None) -> Response:
        """Returns the current authorization state; this is an offline request. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAuthorizationState",
        }

        return await self.invoke(data, timeout=timeout)

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
        timeout: float = None,
    ) -> Response:
        """Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters

        Args:
            use_test_dc (``bool``):
                Pass true to use Telegram test environment instead of the production environment

            database_directory (``str``):
                The path to the directory for the persistent database; if empty, the current working directory will be used

            files_directory (``str``):
                The path to the directory for storing files; if empty, database_directory will be used

            database_encryption_key (``bytes``):
                Encryption key for the database

            use_file_database (``bool``):
                Pass true to keep information about downloaded and uploaded files between application restarts

            use_chat_info_database (``bool``):
                Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts. Implies use_file_database

            use_message_database (``bool``):
                Pass true to keep cache of chats and messages between restarts. Implies use_chat_info_database

            use_secret_chats (``bool``):
                Pass true to enable support for secret chats

            api_id (``int``):
                Application identifier for Telegram API access, which can be obtained at https://my.telegram.org

            api_hash (``str``):
                Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org

            system_language_code (``str``):
                IETF language tag of the user's operating system language; must be non-empty

            device_model (``str``):
                Model of the device the application is being run on; must be non-empty

            system_version (``str``):
                Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib

            application_version (``str``):
                Application version; must be non-empty

            enable_storage_optimizer (``bool``):
                Pass true to automatically delete old files in background

            ignore_file_names (``bool``):
                Pass true to ignore original file names for downloaded files. Otherwise, downloaded files are saved under names as close as possible to the original name


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def setAuthenticationPhoneNumber(
        self, phone_number: str, settings: dict = None, timeout: float = None
    ) -> Response:
        """Sets the phone number of the user and sends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Args:
            phone_number (``str``):
                The phone number of the user, in international format

            settings (``dict``, optional):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setAuthenticationPhoneNumber",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def setAuthenticationEmailAddress(
        self, email_address: str, timeout: float = None
    ) -> Response:
        """Sets the email address of the user and sends an authentication code to the email address. Works only when the current authorization state is authorizationStateWaitEmailAddress

        Args:
            email_address (``str``):
                The email address of the user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setAuthenticationEmailAddress",
            "email_address": email_address,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendAuthenticationCode(self, timeout: float = None) -> Response:
        """Resends an authentication code to the user. Works only when the current authorization state is authorizationStateWaitCode, the next_code_type of the result is not null and the server-specified timeout has passed, or when the current authorization state is authorizationStateWaitEmailCode


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendAuthenticationCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkAuthenticationEmailCode(
        self, code: dict, timeout: float = None
    ) -> Response:
        """Checks the authentication of a email address. Works only when the current authorization state is authorizationStateWaitEmailCode

        Args:
            code (``dict``):
                Email address authentication to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkAuthenticationEmailCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkAuthenticationCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks the authentication code. Works only when the current authorization state is authorizationStateWaitCode

        Args:
            code (``str``):
                Authentication code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkAuthenticationCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def requestQrCodeAuthentication(
        self, other_user_ids: list, timeout: float = None
    ) -> Response:
        """Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber, or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

        Args:
            other_user_ids (``list``):
                List of user identifiers of other users currently using the application


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "requestQrCodeAuthentication",
            "other_user_ids": other_user_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def registerUser(
        self, first_name: str, last_name: str, timeout: float = None
    ) -> Response:
        """Finishes user registration. Works only when the current authorization state is authorizationStateWaitRegistration

        Args:
            first_name (``str``):
                The first name of the user; 1-64 characters

            last_name (``str``):
                The last name of the user; 0-64 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "registerUser",
            "first_name": first_name,
            "last_name": last_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkAuthenticationPassword(
        self, password: str, timeout: float = None
    ) -> Response:
        """Checks the 2-step verification password for correctness. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            password (``str``):
                The 2-step verification password to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkAuthenticationPassword",
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def requestAuthenticationPasswordRecovery(
        self, timeout: float = None
    ) -> Response:
        """Requests to send a 2-step verification password recovery code to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "requestAuthenticationPasswordRecovery",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkAuthenticationPasswordRecoveryCode(
        self, recovery_code: str, timeout: float = None
    ) -> Response:
        """Checks whether a 2-step verification password recovery code sent to an email address is valid. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            recovery_code (``str``):
                Recovery code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkAuthenticationPasswordRecoveryCode",
            "recovery_code": recovery_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def recoverAuthenticationPassword(
        self,
        recovery_code: str,
        new_password: str = None,
        new_hint: str = None,
        timeout: float = None,
    ) -> Response:
        """Recovers the 2-step verification password with a password recovery code sent to an email address that was previously set up. Works only when the current authorization state is authorizationStateWaitPassword

        Args:
            recovery_code (``str``):
                Recovery code to check

            new_password (``str``, optional):
                New 2-step verification password of the user; may be empty to remove the password

            new_hint (``str``, optional):
                New password hint; may be empty


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "recoverAuthenticationPassword",
            "recovery_code": recovery_code,
            "new_password": new_password,
            "new_hint": new_hint,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkAuthenticationBotToken(
        self, token: str, timeout: float = None
    ) -> Response:
        """Checks the authentication token of a bot; to log in as a bot. Works only when the current authorization state is authorizationStateWaitPhoneNumber. Can be used instead of setAuthenticationPhoneNumber and checkAuthenticationCode to log in

        Args:
            token (``str``):
                The bot token


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkAuthenticationBotToken",
            "token": token,
        }

        return await self.invoke(data, timeout=timeout)

    async def logOut(self, timeout: float = None) -> Response:
        """Closes the TDLib instance after a proper logout. Requires an available network connection. All local data will be destroyed. After the logout completes, updateAuthorizationState with authorizationStateClosed will be sent


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "logOut",
        }

        return await self.invoke(data, timeout=timeout)

    async def close(self, timeout: float = None) -> Response:
        """Closes the TDLib instance. All databases will be flushed to disk and properly closed. After the close completes, updateAuthorizationState with authorizationStateClosed will be sent. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "close",
        }

        return await self.invoke(data, timeout=timeout)

    async def destroy(self, timeout: float = None) -> Response:
        """Closes the TDLib instance, destroying all local data without a proper logout. The current user session will remain in the list of all active sessions. All local data will be destroyed. After the destruction completes updateAuthorizationState with authorizationStateClosed will be sent. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "destroy",
        }

        return await self.invoke(data, timeout=timeout)

    async def confirmQrCodeAuthentication(
        self, link: str, timeout: float = None
    ) -> Response:
        """Confirms QR code authentication on another device. Returns created session on success

        Args:
            link (``str``):
                A link from a QR code. The link must be scanned by the in-app camera


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "confirmQrCodeAuthentication",
            "link": link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCurrentState(self, timeout: float = None) -> Response:
        """Returns all updates needed to restore current TDLib state, i.e. all actual UpdateAuthorizationState/UpdateUser/UpdateNewChat and others. This is especially useful if TDLib is run in a separate process. Can be called before initialization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCurrentState",
        }

        return await self.invoke(data, timeout=timeout)

    async def setDatabaseEncryptionKey(
        self, new_encryption_key: bytes, timeout: float = None
    ) -> Response:
        """Changes the database encryption key. Usually the encryption key is never changed and is stored in some OS keychain

        Args:
            new_encryption_key (``bytes``):
                New encryption key


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setDatabaseEncryptionKey",
            "new_encryption_key": new_encryption_key,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPasswordState(self, timeout: float = None) -> Response:
        """Returns the current state of 2-step verification


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPasswordState",
        }

        return await self.invoke(data, timeout=timeout)

    async def setPassword(
        self,
        old_password: str,
        set_recovery_email_address: bool,
        new_password: str = None,
        new_hint: str = None,
        new_recovery_email_address: str = None,
        timeout: float = None,
    ) -> Response:
        """Changes the 2-step verification password for the current user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed

        Args:
            old_password (``str``):
                Previous 2-step verification password of the user

            set_recovery_email_address (``bool``):
                Pass true to change also the recovery email address

            new_password (``str``, optional):
                New 2-step verification password of the user; may be empty to remove the password

            new_hint (``str``, optional):
                New password hint; may be empty

            new_recovery_email_address (``str``, optional):
                New recovery email address; may be empty


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setPassword",
            "old_password": old_password,
            "new_password": new_password,
            "new_hint": new_hint,
            "set_recovery_email_address": set_recovery_email_address,
            "new_recovery_email_address": new_recovery_email_address,
        }

        return await self.invoke(data, timeout=timeout)

    async def setLoginEmailAddress(
        self, new_login_email_address: str, timeout: float = None
    ) -> Response:
        """Changes the login email address of the user. The change will not be applied until the new login email address is confirmed with `checkLoginEmailAddressCode`. To use Apple ID/Google ID instead of a email address, call `checkLoginEmailAddressCode` directly

        Args:
            new_login_email_address (``str``):
                New login email address


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setLoginEmailAddress",
            "new_login_email_address": new_login_email_address,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendLoginEmailAddressCode(self, timeout: float = None) -> Response:
        """Resends the login email address verification code


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendLoginEmailAddressCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkLoginEmailAddressCode(
        self, code: dict, timeout: float = None
    ) -> Response:
        """Checks the login email address authentication

        Args:
            code (``dict``):
                Email address authentication to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkLoginEmailAddressCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecoveryEmailAddress(
        self, password: str, timeout: float = None
    ) -> Response:
        """Returns a 2-step verification recovery email address that was previously set up. This method can be used to verify a password provided by the user

        Args:
            password (``str``):
                The 2-step verification password for the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecoveryEmailAddress",
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def setRecoveryEmailAddress(
        self, password: str, new_recovery_email_address: str, timeout: float = None
    ) -> Response:
        """Changes the 2-step verification recovery email address of the user. If a new recovery email address is specified, then the change will not be applied until the new recovery email address is confirmed. If new_recovery_email_address is the same as the email address that is currently set up, this call succeeds immediately and aborts all other requests waiting for an email confirmation

        Args:
            password (``str``):
                The 2-step verification password of the current user

            new_recovery_email_address (``str``):
                New recovery email address


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setRecoveryEmailAddress",
            "password": password,
            "new_recovery_email_address": new_recovery_email_address,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkRecoveryEmailAddressCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks the 2-step verification recovery email address verification code

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkRecoveryEmailAddressCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendRecoveryEmailAddressCode(self, timeout: float = None) -> Response:
        """Resends the 2-step verification recovery email address verification code


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendRecoveryEmailAddressCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def requestPasswordRecovery(self, timeout: float = None) -> Response:
        """Requests to send a 2-step verification password recovery code to an email address that was previously set up


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "requestPasswordRecovery",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkPasswordRecoveryCode(
        self, recovery_code: str, timeout: float = None
    ) -> Response:
        """Checks whether a 2-step verification password recovery code sent to an email address is valid

        Args:
            recovery_code (``str``):
                Recovery code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkPasswordRecoveryCode",
            "recovery_code": recovery_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def recoverPassword(
        self,
        recovery_code: str,
        new_password: str = None,
        new_hint: str = None,
        timeout: float = None,
    ) -> Response:
        """Recovers the 2-step verification password using a recovery code sent to an email address that was previously set up

        Args:
            recovery_code (``str``):
                Recovery code to check

            new_password (``str``, optional):
                New 2-step verification password of the user; may be empty to remove the password

            new_hint (``str``, optional):
                New password hint; may be empty


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "recoverPassword",
            "recovery_code": recovery_code,
            "new_password": new_password,
            "new_hint": new_hint,
        }

        return await self.invoke(data, timeout=timeout)

    async def resetPassword(self, timeout: float = None) -> Response:
        """Removes 2-step verification password without previous password and access to recovery email address. The password can't be reset immediately and the request needs to be repeated after the specified time


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resetPassword",
        }

        return await self.invoke(data, timeout=timeout)

    async def cancelPasswordReset(self, timeout: float = None) -> Response:
        """Cancels reset of 2-step verification password. The method can be called if passwordState.pending_reset_date > 0


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "cancelPasswordReset",
        }

        return await self.invoke(data, timeout=timeout)

    async def createTemporaryPassword(
        self, password: str, valid_for: int, timeout: float = None
    ) -> Response:
        """Creates a new temporary password for processing payments

        Args:
            password (``str``):
                The 2-step verification password of the current user

            valid_for (``int``):
                Time during which the temporary password will be valid, in seconds; must be between 60 and 86400


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createTemporaryPassword",
            "password": password,
            "valid_for": valid_for,
        }

        return await self.invoke(data, timeout=timeout)

    async def getTemporaryPasswordState(self, timeout: float = None) -> Response:
        """Returns information about the current temporary password


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getTemporaryPasswordState",
        }

        return await self.invoke(data, timeout=timeout)

    async def getMe(self, timeout: float = None) -> Response:
        """Returns the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMe",
        }

        return await self.invoke(data, timeout=timeout)

    async def getUser(self, user_id: int, timeout: float = None) -> Response:
        """Returns information about a user by their identifier. This is an offline request if the current user is not a bot

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getUser",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getUserFullInfo(self, user_id: int, timeout: float = None) -> Response:
        """Returns full information about a user by their identifier

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getUserFullInfo",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getBasicGroup(
        self, basic_group_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a basic group by its identifier. This is an offline request if the current user is not a bot

        Args:
            basic_group_id (``int``):
                Basic group identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBasicGroup",
            "basic_group_id": basic_group_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getBasicGroupFullInfo(
        self, basic_group_id: int, timeout: float = None
    ) -> Response:
        """Returns full information about a basic group by its identifier

        Args:
            basic_group_id (``int``):
                Basic group identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBasicGroupFullInfo",
            "basic_group_id": basic_group_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSupergroup(
        self, supergroup_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a supergroup or a channel by its identifier. This is an offline request if the current user is not a bot

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSupergroup",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSupergroupFullInfo(
        self, supergroup_id: int, timeout: float = None
    ) -> Response:
        """Returns full information about a supergroup or a channel by its identifier, cached for up to 1 minute

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSupergroupFullInfo",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSecretChat(
        self, secret_chat_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a secret chat by its identifier. This is an offline request

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChat(self, chat_id: int, timeout: float = None) -> Response:
        """Returns information about a chat by its identifier, this is an offline request if the current user is not a bot

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessage(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a message

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the message to get


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageLocally(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a message, if it is available without sending network request. This is an offline request

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the message to get


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageLocally",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRepliedMessage(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a message that is replied by a given message. Also returns the pinned message, the game message, and the invoice message for messages of the types messagePinMessage, messageGameScore, and messagePaymentSuccessful respectively

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Identifier of the reply message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRepliedMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatPinnedMessage(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a newest pinned message in the chat

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatPinnedMessage",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCallbackQueryMessage(
        self,
        chat_id: int,
        message_id: int,
        callback_query_id: int,
        timeout: float = None,
    ) -> Response:
        """Returns information about a message with the callback button that originated a callback query; for bots only

        Args:
            chat_id (``int``):
                Identifier of the chat the message belongs to

            message_id (``int``):
                Message identifier

            callback_query_id (``int``):
                Identifier of the callback query


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCallbackQueryMessage",
            "chat_id": chat_id,
            "message_id": message_id,
            "callback_query_id": callback_query_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessages(
        self, chat_id: int, message_ids: list, timeout: float = None
    ) -> Response:
        """Returns information about messages. If a message is not found, returns null on the corresponding position of the result

        Args:
            chat_id (``int``):
                Identifier of the chat the messages belong to

            message_ids (``list``):
                Identifiers of the messages to get


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageThread(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a message thread. Can be used only if message.can_get_message_thread == true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageThread",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageViewers(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if message.can_get_viewers == true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageViewers",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getFile(self, file_id: int, timeout: float = None) -> Response:
        """Returns information about a file; this is an offline request

        Args:
            file_id (``int``):
                Identifier of the file to get


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getFile",
            "file_id": file_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRemoteFile(
        self, remote_file_id: str, file_type: dict = None, timeout: float = None
    ) -> Response:
        """Returns information about a file by its remote ID; this is an offline request. Can be used to register a URL as a file for further uploading, or sending as a message. Even the request succeeds, the file can be used only if it is still accessible to the user. For example, if the file is from a message, then the message must be not deleted and accessible to the user. If the file database is disabled, then the corresponding object with the file must be preloaded by the application

        Args:
            remote_file_id (``str``):
                Remote identifier of the file to get

            file_type (``dict``, optional):
                File type; pass null if unknown


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRemoteFile",
            "remote_file_id": remote_file_id,
            "file_type": file_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def loadChats(
        self, limit: int, chat_list: dict = None, timeout: float = None
    ) -> Response:
        """Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded

        Args:
            limit (``int``):
                The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached

            chat_list (``dict``, optional):
                The chat list in which to load chats; pass null to load chats from the main chat list


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "loadChats",
            "chat_list": chat_list,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChats(
        self, limit: int, chat_list: dict = None, timeout: float = None
    ) -> Response:
        """Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state

        Args:
            limit (``int``):
                The maximum number of chats to be returned

            chat_list (``dict``, optional):
                The chat list in which to return chats; pass null to get chats from the main chat list


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChats",
            "chat_list": chat_list,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchPublicChat(self, username: str, timeout: float = None) -> Response:
        """Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise an error is returned

        Args:
            username (``str``):
                Username to be resolved


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchPublicChat",
            "username": username,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchPublicChats(self, query: str, timeout: float = None) -> Response:
        """Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results. Excludes private chats with contacts and chats from the chat list from the results

        Args:
            query (``str``):
                Query to search for


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchPublicChats",
            "query": query,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchChats(
        self, query: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for the specified query in the title and username of already known chats, this is an offline request. Returns chats in the order seen in the main chat list

        Args:
            query (``str``):
                Query to search for. If the query is empty, returns up to 50 recently found chats

            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchChats",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchChatsOnServer(
        self, query: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list

        Args:
            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchChatsOnServer",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchChatsNearby(
        self, location: dict, timeout: float = None
    ) -> Response:
        """Returns a list of users and location-based supergroups nearby. The list of users nearby will be updated for 60 seconds after the request by the updates updateUsersNearby. The request must be sent again every 25 seconds with adjusted location to not miss new chats

        Args:
            location (``dict``):
                Current user location


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchChatsNearby",
            "location": location,
        }

        return await self.invoke(data, timeout=timeout)

    async def getTopChats(
        self, category: dict, limit: int, timeout: float = None
    ) -> Response:
        """Returns a list of frequently used chats. Supported only if the chat info database is enabled

        Args:
            category (``dict``):
                Category of chats to be returned

            limit (``int``):
                The maximum number of chats to be returned; up to 30


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getTopChats",
            "category": category,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeTopChat(
        self, category: dict, chat_id: int, timeout: float = None
    ) -> Response:
        """Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled

        Args:
            category (``dict``):
                Category of frequently used chats

            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeTopChat",
            "category": category,
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addRecentlyFoundChat(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first

        Args:
            chat_id (``int``):
                Identifier of the chat to add


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addRecentlyFoundChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeRecentlyFoundChat(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Removes a chat from the list of recently found chats

        Args:
            chat_id (``int``):
                Identifier of the chat to be removed


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeRecentlyFoundChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def clearRecentlyFoundChats(self, timeout: float = None) -> Response:
        """Clears the list of recently found chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearRecentlyFoundChats",
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecentlyOpenedChats(
        self, limit: int, timeout: float = None
    ) -> Response:
        """Returns recently opened chats, this is an offline request. Returns chats in the order of last opening

        Args:
            limit (``int``):
                The maximum number of chats to be returned


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecentlyOpenedChats",
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkChatUsername(
        self, chat_id: int, username: str, timeout: float = None
    ) -> Response:
        """Checks whether a username can be set for a chat

        Args:
            chat_id (``int``):
                Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if the chat is being created

            username (``str``):
                Username to be checked


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkChatUsername",
            "chat_id": chat_id,
            "username": username,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCreatedPublicChats(
        self, type: dict, timeout: float = None
    ) -> Response:
        """Returns a list of public chats of the specified type, owned by the user

        Args:
            type (``dict``):
                Type of the public chats to return


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCreatedPublicChats",
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkCreatedPublicChatsLimit(
        self, type: dict, timeout: float = None
    ) -> Response:
        """Checks whether the maximum number of owned public chats has been reached. Returns corresponding error if the limit was reached. The limit can be increased with Telegram Premium

        Args:
            type (``dict``):
                Type of the public chats, for which to check the limit


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkCreatedPublicChatsLimit",
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSuitableDiscussionChats(self, timeout: float = None) -> Response:
        """Returns a list of basic group and supergroup chats, which can be used as a discussion group for a channel. Returned basic group chats must be first upgraded to supergroups before they can be set as a discussion group. To set a returned supergroup as a discussion group, access to its old messages must be enabled using toggleSupergroupIsAllHistoryAvailable first


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSuitableDiscussionChats",
        }

        return await self.invoke(data, timeout=timeout)

    async def getInactiveSupergroupChats(self, timeout: float = None) -> Response:
        """Returns a list of recently inactive supergroups and channels. Can be used when user reaches limit on the number of joined supergroups and channels and receives CHANNELS_TOO_MUCH error. Also, the limit can be increased with Telegram Premium


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getInactiveSupergroupChats",
        }

        return await self.invoke(data, timeout=timeout)

    async def getGroupsInCommon(
        self, user_id: int, offset_chat_id: int, limit: int, timeout: float = None
    ) -> Response:
        """Returns a list of common group chats with a given user. Chats are sorted by their type and creation date

        Args:
            user_id (``int``):
                User identifier

            offset_chat_id (``int``):
                Chat identifier starting from which to return chats; use 0 for the first request

            limit (``int``):
                The maximum number of chats to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGroupsInCommon",
            "user_id": user_id,
            "offset_chat_id": offset_chat_id,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatHistory(
        self,
        chat_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        only_local: bool,
        timeout: float = None,
    ) -> Response:
        """Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib. This is an offline request if only_local is true

        Args:
            chat_id (``int``):
                Chat identifier

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_local (``bool``):
                Pass true to get only messages that are available without sending network requests


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatHistory",
            "chat_id": chat_id,
            "from_message_id": from_message_id,
            "offset": offset,
            "limit": limit,
            "only_local": only_local,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageThreadHistory(
        self,
        chat_id: int,
        message_id: int,
        from_message_id: int,
        offset: int,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier, which thread history needs to be returned

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageThreadHistory",
            "chat_id": chat_id,
            "message_id": message_id,
            "from_message_id": from_message_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChatHistory(
        self,
        chat_id: int,
        remove_from_chat_list: bool,
        revoke: bool,
        timeout: float = None,
    ) -> Response:
        """Deletes all messages in the chat. Use chat.can_be_deleted_only_for_self and chat.can_be_deleted_for_all_users fields to find whether and how the method can be applied to the chat

        Args:
            chat_id (``int``):
                Chat identifier

            remove_from_chat_list (``bool``):
                Pass true to remove the chat from all chat lists

            revoke (``bool``):
                Pass true to delete chat history for all users


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChatHistory",
            "chat_id": chat_id,
            "remove_from_chat_list": remove_from_chat_list,
            "revoke": revoke,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChat(self, chat_id: int, timeout: float = None) -> Response:
        """Deletes a chat along with all messages in the corresponding chat for all chat members. For group chats this will release the username and remove all members. Use the field chat.can_be_deleted_for_all_users to find whether the method can be applied to the chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

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
        timeout: float = None,
    ) -> Response:
        """Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages must be used instead), or without an enabled message database. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Args:
            chat_id (``int``):
                Identifier of the chat in which to search messages

            query (``str``):
                Query to search for

            from_message_id (``int``):
                Identifier of the message starting from which history must be fetched; use 0 to get results from the last message

            offset (``int``):
                Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            message_thread_id (``int``):
                If not 0, only messages in the specified thread will be returned; supergroups only

            sender_id (``dict``, optional):
                Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats

            filter (``dict``, optional):
                Additional filter for messages to search; pass null to search for all messages


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def searchMessages(
        self,
        query: str,
        offset_date: int,
        offset_chat_id: int,
        offset_message_id: int,
        limit: int,
        min_date: int,
        max_date: int,
        chat_list: dict = None,
        filter: dict = None,
        timeout: float = None,
    ) -> Response:
        """Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

        Args:
            query (``str``):
                Query to search for

            offset_date (``int``):
                The date of the message starting from which the results need to be fetched. Use 0 or any date in the future to get results from the last message

            offset_chat_id (``int``):
                The chat identifier of the last found message, or 0 for the first request

            offset_message_id (``int``):
                The message identifier of the last found message, or 0 for the first request

            limit (``int``):
                The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            min_date (``int``):
                If not 0, the minimum date of the messages to return

            max_date (``int``):
                If not 0, the maximum date of the messages to return

            chat_list (``dict``, optional):
                Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported

            filter (``dict``, optional):
                Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchMessages",
            "chat_list": chat_list,
            "query": query,
            "offset_date": offset_date,
            "offset_chat_id": offset_chat_id,
            "offset_message_id": offset_message_id,
            "limit": limit,
            "filter": filter,
            "min_date": min_date,
            "max_date": max_date,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchSecretMessages(
        self,
        chat_id: int,
        query: str,
        offset: str,
        limit: int,
        filter: dict = None,
        timeout: float = None,
    ) -> Response:
        """Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Identifier of the chat in which to search. Specify 0 to search in all secret chats

            query (``str``):
                Query to search for. If empty, searchChatMessages must be used instead

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            filter (``dict``, optional):
                Additional filter for messages to search; pass null to search for all messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchSecretMessages",
            "chat_id": chat_id,
            "query": query,
            "offset": offset,
            "limit": limit,
            "filter": filter,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchCallMessages(
        self, from_message_id: int, limit: int, only_missed: bool, timeout: float = None
    ) -> Response:
        """Searches for call messages. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            from_message_id (``int``):
                Identifier of the message from which to search; use 0 to get results from the last message

            limit (``int``):
                The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

            only_missed (``bool``):
                Pass true to search only for messages with missed/declined calls


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchCallMessages",
            "from_message_id": from_message_id,
            "limit": limit,
            "only_missed": only_missed,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchOutgoingDocumentMessages(
        self, query: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order

        Args:
            query (``str``):
                Query to search for in document file name and message caption

            limit (``int``):
                The maximum number of messages to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchOutgoingDocumentMessages",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteAllCallMessages(
        self, revoke: bool, timeout: float = None
    ) -> Response:
        """Deletes all call messages

        Args:
            revoke (``bool``):
                Pass true to delete the messages for all users


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteAllCallMessages",
            "revoke": revoke,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchChatRecentLocationMessages(
        self, chat_id: int, limit: int, timeout: float = None
    ) -> Response:
        """Returns information about the recent locations of chat members that were sent to the chat. Returns up to 1 location message per user

        Args:
            chat_id (``int``):
                Chat identifier

            limit (``int``):
                The maximum number of messages to be returned


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchChatRecentLocationMessages",
            "chat_id": chat_id,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getActiveLiveLocationMessages(self, timeout: float = None) -> Response:
        """Returns all active live locations that need to be updated by the application. The list is persistent across application restarts only if the message database is used


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getActiveLiveLocationMessages",
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatMessageByDate(
        self, chat_id: int, date: int, timeout: float = None
    ) -> Response:
        """Returns the last message sent in a chat no later than the specified date

        Args:
            chat_id (``int``):
                Chat identifier

            date (``int``):
                Point in time (Unix timestamp) relative to which to search for messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatMessageByDate",
            "chat_id": chat_id,
            "date": date,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatSparseMessagePositions(
        self,
        chat_id: int,
        filter: dict,
        from_message_id: int,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

        Args:
            chat_id (``int``):
                Identifier of the chat in which to return information about message positions

            filter (``dict``):
                Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (``int``):
                The message identifier from which to return information about message positions

            limit (``int``):
                The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatSparseMessagePositions",
            "chat_id": chat_id,
            "filter": filter,
            "from_message_id": from_message_id,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatMessageCalendar(
        self, chat_id: int, filter: dict, from_message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"

        Args:
            chat_id (``int``):
                Identifier of the chat in which to return information about messages

            filter (``dict``):
                Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function

            from_message_id (``int``):
                The message identifier from which to return information about messages; use 0 to get results from the last message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatMessageCalendar",
            "chat_id": chat_id,
            "filter": filter,
            "from_message_id": from_message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatMessageCount(
        self, chat_id: int, filter: dict, return_local: bool, timeout: float = None
    ) -> Response:
        """Returns approximate number of messages of the specified type in the chat

        Args:
            chat_id (``int``):
                Identifier of the chat in which to count messages

            filter (``dict``):
                Filter for message content; searchMessagesFilterEmpty is unsupported in this function

            return_local (``bool``):
                Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatMessageCount",
            "chat_id": chat_id,
            "filter": filter,
            "return_local": return_local,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatMessagePosition(
        self,
        chat_id: int,
        message_id: int,
        filter: dict,
        message_thread_id: int,
        timeout: float = None,
    ) -> Response:
        """Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats

        Args:
            chat_id (``int``):
                Identifier of the chat in which to find message position

            message_id (``int``):
                Message identifier

            filter (``dict``):
                Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function

            message_thread_id (``int``):
                If not 0, only messages in the specified thread will be considered; supergroups only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatMessagePosition",
            "chat_id": chat_id,
            "message_id": message_id,
            "filter": filter,
            "message_thread_id": message_thread_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatScheduledMessages(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatScheduledMessages",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessagePublicForwards(
        self,
        chat_id: int,
        message_id: int,
        offset: str,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Message identifier

            offset (``str``):
                Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results

            limit (``int``):
                The maximum number of messages to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessagePublicForwards",
            "chat_id": chat_id,
            "message_id": message_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatSponsoredMessage(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns sponsored message to be shown in a chat; for channel chats only. Returns a 404 error if there is no sponsored message in the chat

        Args:
            chat_id (``int``):
                Identifier of the chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatSponsoredMessage",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeNotification(
        self, notification_group_id: int, notification_id: int, timeout: float = None
    ) -> Response:
        """Removes an active notification from notification list. Needs to be called only if the notification is removed by the current user

        Args:
            notification_group_id (``int``):
                Identifier of notification group to which the notification belongs

            notification_id (``int``):
                Identifier of removed notification


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeNotification",
            "notification_group_id": notification_group_id,
            "notification_id": notification_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeNotificationGroup(
        self,
        notification_group_id: int,
        max_notification_id: int,
        timeout: float = None,
    ) -> Response:
        """Removes a group of active notifications. Needs to be called only if the notification group is removed by the current user

        Args:
            notification_group_id (``int``):
                Notification group identifier

            max_notification_id (``int``):
                The maximum identifier of removed notifications


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeNotificationGroup",
            "notification_group_id": notification_group_id,
            "max_notification_id": max_notification_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageLink(
        self,
        chat_id: int,
        message_id: int,
        media_timestamp: int,
        for_album: bool,
        for_comment: bool,
        timeout: float = None,
    ) -> Response:
        """Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            media_timestamp (``int``):
                If not 0, timestamp from which the video/audio/video note/voice note playing must start, in seconds. The media can be in the message content or in its web page preview

            for_album (``bool``):
                Pass true to create a link for the whole media album

            for_comment (``bool``):
                Pass true to create a link to the message as a channel post comment, or from a message thread


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageLink",
            "chat_id": chat_id,
            "message_id": message_id,
            "media_timestamp": media_timestamp,
            "for_album": for_album,
            "for_comment": for_comment,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageEmbeddingCode(
        self, chat_id: int, message_id: int, for_album: bool, timeout: float = None
    ) -> Response:
        """Returns an HTML code for embedding the message. Available only for messages in supergroups and channels with a username

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            for_album (``bool``):
                Pass true to return an HTML code for embedding of the whole media album


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageEmbeddingCode",
            "chat_id": chat_id,
            "message_id": message_id,
            "for_album": for_album,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageLinkInfo(self, url: str, timeout: float = None) -> Response:
        """Returns information about a public or private message link. Can be called for any internal link of the type internalLinkTypeMessage

        Args:
            url (``str``):
                The message link


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageLinkInfo",
            "url": url,
        }

        return await self.invoke(data, timeout=timeout)

    async def translateText(
        self,
        text: str,
        from_language_code: str,
        to_language_code: str,
        timeout: float = None,
    ) -> Response:
        """Translates a text to the given language. Returns a 404 error if the translation can't be performed

        Args:
            text (``str``):
                Text to translate

            from_language_code (``str``):
                A two-letter ISO 639-1 language code of the language from which the message is translated. If empty, the language will be detected automatically

            to_language_code (``str``):
                A two-letter ISO 639-1 language code of the language to which the message is translated


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "translateText",
            "text": text,
            "from_language_code": from_language_code,
            "to_language_code": to_language_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def recognizeSpeech(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Recognizes speech in a voice note message. The message must be successfully sent and must not be scheduled. May return an error with a message "MSG_VOICE_TOO_LONG" if the voice note is too long to be recognized

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "recognizeSpeech",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def rateSpeechRecognition(
        self, chat_id: int, message_id: int, is_good: bool, timeout: float = None
    ) -> Response:
        """Rates recognized speech in a voice note message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            is_good (``bool``):
                Pass true if the speech recognition is good


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "rateSpeechRecognition",
            "chat_id": chat_id,
            "message_id": message_id,
            "is_good": is_good,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatAvailableMessageSenders(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns list of message sender identifiers, which can be used to send messages in a chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatAvailableMessageSenders",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatMessageSender(
        self, chat_id: int, message_sender_id: dict, timeout: float = None
    ) -> Response:
        """Selects a message sender to send messages in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_sender_id (``dict``):
                New message sender for the chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatMessageSender",
            "chat_id": chat_id,
            "message_sender_id": message_sender_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendMessage(
        self,
        chat_id: int,
        message_thread_id: int,
        reply_to_message_id: int,
        input_message_content: dict,
        options: dict = None,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sends a message. Returns the sent message

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``):
                Identifier of the replied message; 0 if none

            input_message_content (``dict``):
                The content of the message to be sent

            options (``dict``, optional):
                Options to be used to send the message; pass null to use default options

            reply_markup (``dict``, optional):
                Markup for replying to the message; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to_message_id": reply_to_message_id,
            "options": options,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendMessageAlbum(
        self,
        chat_id: int,
        message_thread_id: int,
        reply_to_message_id: int,
        input_message_contents: list,
        only_preview: bool,
        options: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the messages will be sent

            reply_to_message_id (``int``):
                Identifier of a replied message; 0 if none

            input_message_contents (``list``):
                Contents of messages to be sent. At most 10 messages can be added to an album

            only_preview (``bool``):
                Pass true to get fake messages instead of actually sending them

            options (``dict``, optional):
                Options to be used to send the messages; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendMessageAlbum",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to_message_id": reply_to_message_id,
            "options": options,
            "input_message_contents": input_message_contents,
            "only_preview": only_preview,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendBotStartMessage(
        self, bot_user_id: int, chat_id: int, parameter: str, timeout: float = None
    ) -> Response:
        """Invites a bot to a chat (if it is not yet a member) and sends it the /start command. Bots can't be invited to a private chat other than the chat with the bot. Bots can't be invited to channels (although they can be added as admins) and secret chats. Returns the sent message

        Args:
            bot_user_id (``int``):
                Identifier of the bot

            chat_id (``int``):
                Identifier of the target chat

            parameter (``str``):
                A hidden parameter sent to the bot for deep linking purposes (https://core.telegram.org/bots#deep-linking)


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendBotStartMessage",
            "bot_user_id": bot_user_id,
            "chat_id": chat_id,
            "parameter": parameter,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendInlineQueryResultMessage(
        self,
        chat_id: int,
        message_thread_id: int,
        reply_to_message_id: int,
        query_id: int,
        result_id: str,
        hide_via_bot: bool,
        options: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message

        Args:
            chat_id (``int``):
                Target chat

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the message will be sent

            reply_to_message_id (``int``):
                Identifier of a replied message; 0 if none

            query_id (``int``):
                Identifier of the inline query

            result_id (``str``):
                Identifier of the inline result

            hide_via_bot (``bool``):
                Pass true to hide the bot, via which the message is sent. Can be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username"), and GetOption("venue_search_bot_username")

            options (``dict``, optional):
                Options to be used to send the message; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendInlineQueryResultMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "reply_to_message_id": reply_to_message_id,
            "options": options,
            "query_id": query_id,
            "result_id": result_id,
            "hide_via_bot": hide_via_bot,
        }

        return await self.invoke(data, timeout=timeout)

    async def forwardMessages(
        self,
        chat_id: int,
        from_chat_id: int,
        message_ids: list,
        send_copy: bool,
        remove_caption: bool,
        only_preview: bool,
        options: dict = None,
        timeout: float = None,
    ) -> Response:
        """Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which to forward messages

            from_chat_id (``int``):
                Identifier of the chat from which to forward messages

            message_ids (``list``):
                Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously

            send_copy (``bool``):
                Pass true to copy content of the messages without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local

            remove_caption (``bool``):
                Pass true to remove media captions of message copies. Ignored if send_copy is false

            only_preview (``bool``):
                Pass true to get fake messages instead of actually forwarding them

            options (``dict``, optional):
                Options to be used to send the messages; pass null to use default options


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "forwardMessages",
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_ids": message_ids,
            "options": options,
            "send_copy": send_copy,
            "remove_caption": remove_caption,
            "only_preview": only_preview,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendMessages(
        self, chat_id: int, message_ids: list, timeout: float = None
    ) -> Response:
        """Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message

        Args:
            chat_id (``int``):
                Identifier of the chat to send messages

            message_ids (``list``):
                Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendChatScreenshotTakenNotification(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendChatScreenshotTakenNotification",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addLocalMessage(
        self,
        chat_id: int,
        sender_id: dict,
        reply_to_message_id: int,
        disable_notification: bool,
        input_message_content: dict,
        timeout: float = None,
    ) -> Response:
        """Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message

        Args:
            chat_id (``int``):
                Target chat

            sender_id (``dict``):
                Identifier of the sender of the message

            reply_to_message_id (``int``):
                Identifier of the replied message; 0 if none

            disable_notification (``bool``):
                Pass true to disable notification for the message

            input_message_content (``dict``):
                The content of the message to be added


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addLocalMessage",
            "chat_id": chat_id,
            "sender_id": sender_id,
            "reply_to_message_id": reply_to_message_id,
            "disable_notification": disable_notification,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteMessages(
        self, chat_id: int, message_ids: list, revoke: bool, timeout: float = None
    ) -> Response:
        """Deletes messages

        Args:
            chat_id (``int``):
                Chat identifier

            message_ids (``list``):
                Identifiers of the messages to be deleted

            revoke (``bool``):
                Pass true to delete messages for all chat members. Always true for supergroups, channels and secret chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteMessages",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "revoke": revoke,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChatMessagesBySender(
        self, chat_id: int, sender_id: dict, timeout: float = None
    ) -> Response:
        """Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges

        Args:
            chat_id (``int``):
                Chat identifier

            sender_id (``dict``):
                Identifier of the sender of messages to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChatMessagesBySender",
            "chat_id": chat_id,
            "sender_id": sender_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChatMessagesByDate(
        self,
        chat_id: int,
        min_date: int,
        max_date: int,
        revoke: bool,
        timeout: float = None,
    ) -> Response:
        """Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted

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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChatMessagesByDate",
            "chat_id": chat_id,
            "min_date": min_date,
            "max_date": max_date,
            "revoke": revoke,
        }

        return await self.invoke(data, timeout=timeout)

    async def editMessageText(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: dict,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            input_message_content (``dict``):
                New text content of the message. Must be of type inputMessageText

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editMessageText",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def editMessageLiveLocation(
        self,
        chat_id: int,
        message_id: int,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: dict = None,
        location: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the message content of a live location. Messages can be edited for a limited period of time specified in the live location. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            heading (``int``):
                The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown

            proximity_alert_radius (``int``):
                The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only

            location (``dict``, optional):
                New location content of the message; pass null to stop sharing the live location


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def editMessageMedia(
        self,
        chat_id: int,
        message_id: int,
        input_message_content: dict,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the content of a message with an animation, an audio, a document, a photo or a video, including message caption. If only the caption needs to be edited, use editMessageCaption instead. The media can't be edited if the message was set to self-destruct or to a self-destructing media. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            input_message_content (``dict``):
                New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editMessageMedia",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def editMessageCaption(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: dict = None,
        caption: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the message content caption. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only

            caption (``dict``, optional):
                New message content caption; 0-GetOption("message_caption_length_max") characters; pass null to remove caption


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editMessageCaption",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
            "caption": caption,
        }

        return await self.invoke(data, timeout=timeout)

    async def editMessageReplyMarkup(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editMessageReplyMarkup",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data, timeout=timeout)

    async def editInlineMessageText(
        self,
        inline_message_id: str,
        input_message_content: dict,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the text of an inline text or game message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            input_message_content (``dict``):
                New text content of the message. Must be of type inputMessageText

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editInlineMessageText",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def editInlineMessageLiveLocation(
        self,
        inline_message_id: str,
        heading: int,
        proximity_alert_radius: int,
        reply_markup: dict = None,
        location: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the content of a live location in an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            heading (``int``):
                The new direction in which the location moves, in degrees; 1-360. Pass 0 if unknown

            proximity_alert_radius (``int``):
                The new maximum distance for proximity alerts, in meters (0-100000). Pass 0 if the notification is disabled

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none

            location (``dict``, optional):
                New location content of the message; pass null to stop sharing the live location


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editInlineMessageLiveLocation",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "location": location,
            "heading": heading,
            "proximity_alert_radius": proximity_alert_radius,
        }

        return await self.invoke(data, timeout=timeout)

    async def editInlineMessageMedia(
        self,
        inline_message_id: str,
        input_message_content: dict,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            input_message_content (``dict``):
                New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editInlineMessageMedia",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "input_message_content": input_message_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def editInlineMessageCaption(
        self,
        inline_message_id: str,
        reply_markup: dict = None,
        caption: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the caption of an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none

            caption (``dict``, optional):
                New message content caption; pass null to remove caption; 0-GetOption("message_caption_length_max") characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editInlineMessageCaption",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
            "caption": caption,
        }

        return await self.invoke(data, timeout=timeout)

    async def editInlineMessageReplyMarkup(
        self, inline_message_id: str, reply_markup: dict = None, timeout: float = None
    ) -> Response:
        """Edits the reply markup of an inline message sent via a bot; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editInlineMessageReplyMarkup",
            "inline_message_id": inline_message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data, timeout=timeout)

    async def editMessageSchedulingState(
        self,
        chat_id: int,
        message_id: int,
        scheduling_state: dict = None,
        timeout: float = None,
    ) -> Response:
        """Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed

        Args:
            chat_id (``int``):
                The chat the message belongs to

            message_id (``int``):
                Identifier of the message

            scheduling_state (``dict``, optional):
                The new message scheduling state; pass null to send the message immediately


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editMessageSchedulingState",
            "chat_id": chat_id,
            "message_id": message_id,
            "scheduling_state": scheduling_state,
        }

        return await self.invoke(data, timeout=timeout)

    async def getEmojiReaction(self, emoji: str, timeout: float = None) -> Response:
        """Returns information about a emoji reaction. Returns a 404 error if the reaction is not found

        Args:
            emoji (``str``):
                Text representation of the reaction


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getEmojiReaction",
            "emoji": emoji,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCustomEmojiReactionAnimations(self, timeout: float = None) -> Response:
        """Returns TGS stickers with generic animations for custom emoji reactions


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCustomEmojiReactionAnimations",
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageAvailableReactions(
        self, chat_id: int, message_id: int, row_size: int, timeout: float = None
    ) -> Response:
        """Returns reactions, which can be added to a message. The list can change after updateActiveEmojiReactions, updateChatAvailableReactions for the chat, or updateMessageInteractionInfo for the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            row_size (``int``):
                Number of reaction per row, 5-25


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageAvailableReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "row_size": row_size,
        }

        return await self.invoke(data, timeout=timeout)

    async def clearRecentReactions(self, timeout: float = None) -> Response:
        """Clears the list of recently used reactions


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearRecentReactions",
        }

        return await self.invoke(data, timeout=timeout)

    async def addMessageReaction(
        self,
        chat_id: int,
        message_id: int,
        reaction_type: dict,
        is_big: bool,
        update_recent_reactions: bool,
        timeout: float = None,
    ) -> Response:
        """Adds a reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            reaction_type (``dict``):
                Type of the reaction to add

            is_big (``bool``):
                Pass true if the reaction is added with a big animation

            update_recent_reactions (``bool``):
                Pass true if the reaction needs to be added to recent reactions


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addMessageReaction",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
            "is_big": is_big,
            "update_recent_reactions": update_recent_reactions,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeMessageReaction(
        self, chat_id: int, message_id: int, reaction_type: dict, timeout: float = None
    ) -> Response:
        """Removes a reaction from a message. A chosen reaction can always be removed

        Args:
            chat_id (``int``):
                Identifier of the chat to which the message belongs

            message_id (``int``):
                Identifier of the message

            reaction_type (``dict``):
                Type of the reaction to remove


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeMessageReaction",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageAddedReactions(
        self,
        chat_id: int,
        message_id: int,
        offset: str,
        limit: int,
        reaction_type: dict = None,
        timeout: float = None,
    ) -> Response:
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

            reaction_type (``dict``, optional):
                Type of the reactions to return; pass null to return all added reactions


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageAddedReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "reaction_type": reaction_type,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def setDefaultReactionType(
        self, reaction_type: dict, timeout: float = None
    ) -> Response:
        """Changes type of default reaction for the current user

        Args:
            reaction_type (``dict``):
                New type of the default reaction


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setDefaultReactionType",
            "reaction_type": reaction_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getTextEntities(self, text: str, timeout: float = None) -> Response:
        """Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) contained in the text. Can be called synchronously

        Args:
            text (``str``):
                The text in which to look for entites


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getTextEntities",
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def parseTextEntities(
        self, text: str, parse_mode: dict, timeout: float = None
    ) -> Response:
        """Parses Bold, Italic, Underline, Strikethrough, Spoiler, CustomEmoji, Code, Pre, PreCode, TextUrl and MentionName entities contained in the text. Can be called synchronously

        Args:
            text (``str``):
                The text to parse

            parse_mode (``dict``):
                Text parse mode


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "parseTextEntities",
            "text": text,
            "parse_mode": parse_mode,
        }

        return await self.invoke(data, timeout=timeout)

    async def parseMarkdown(self, text: dict, timeout: float = None) -> Response:
        """Parses Markdown entities in a human-friendly format, ignoring markup errors. Can be called synchronously

        Args:
            text (``dict``):
                The text to parse. For example, "__italic__ ~~strikethrough~~ ||spoiler|| **bold** `code` ```pre``` __[italic__ text_url](telegram.org) __italic**bold italic__bold**"


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "parseMarkdown",
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMarkdownText(self, text: dict, timeout: float = None) -> Response:
        """Replaces text entities with Markdown formatting in a human-friendly format. Entities that can't be represented in Markdown unambiguously are kept as is. Can be called synchronously

        Args:
            text (``dict``):
                The text


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMarkdownText",
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def getFileMimeType(self, file_name: str, timeout: float = None) -> Response:
        """Returns the MIME type of a file, guessed by its extension. Returns an empty string on failure. Can be called synchronously

        Args:
            file_name (``str``):
                The name of the file or path to the file


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getFileMimeType",
            "file_name": file_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def getFileExtension(self, mime_type: str, timeout: float = None) -> Response:
        """Returns the extension of a file, guessed by its MIME type. Returns an empty string on failure. Can be called synchronously

        Args:
            mime_type (``str``):
                The MIME type of the file


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getFileExtension",
            "mime_type": mime_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def cleanFileName(self, file_name: str, timeout: float = None) -> Response:
        """Removes potentially dangerous characters from the name of a file. The encoding of the file name is supposed to be UTF-8. Returns an empty string on failure. Can be called synchronously

        Args:
            file_name (``str``):
                File name or path to the file


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "cleanFileName",
            "file_name": file_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLanguagePackString(
        self,
        language_pack_database_path: str,
        localization_target: str,
        language_pack_id: str,
        key: str,
        timeout: float = None,
    ) -> Response:
        """Returns a string stored in the local database from the specified localization target and language pack by its key. Returns a 404 error if the string is not found. Can be called synchronously

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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLanguagePackString",
            "language_pack_database_path": language_pack_database_path,
            "localization_target": localization_target,
            "language_pack_id": language_pack_id,
            "key": key,
        }

        return await self.invoke(data, timeout=timeout)

    async def getJsonValue(self, json: str, timeout: float = None) -> Response:
        """Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously

        Args:
            json (``str``):
                The JSON-serialized string


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getJsonValue",
            "json": json,
        }

        return await self.invoke(data, timeout=timeout)

    async def getJsonString(self, json_value: dict, timeout: float = None) -> Response:
        """Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously

        Args:
            json_value (``dict``):
                The JsonValue object


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getJsonString",
            "json_value": json_value,
        }

        return await self.invoke(data, timeout=timeout)

    async def getThemeParametersJsonString(
        self, theme: dict, timeout: float = None
    ) -> Response:
        """Converts a themeParameters object to corresponding JSON-serialized string. Can be called synchronously

        Args:
            theme (``dict``):
                Theme parameters to convert to JSON


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getThemeParametersJsonString",
            "theme": theme,
        }

        return await self.invoke(data, timeout=timeout)

    async def setPollAnswer(
        self, chat_id: int, message_id: int, option_ids: list, timeout: float = None
    ) -> Response:
        """Changes the user answer to a poll. A poll in quiz mode can be answered only once

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            option_ids (``list``):
                0-based identifiers of answer options, chosen by the user. User can choose more than 1 answer option only is the poll allows multiple answers


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setPollAnswer",
            "chat_id": chat_id,
            "message_id": message_id,
            "option_ids": option_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPollVoters(
        self,
        chat_id: int,
        message_id: int,
        option_id: int,
        offset: int,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns users voted for the specified option in a non-anonymous polls. For optimal performance, the number of returned users is chosen by TDLib

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            option_id (``int``):
                0-based identifier of the answer option

            offset (``int``):
                Number of users to skip in the result; must be non-negative

            limit (``int``):
                The maximum number of users to be returned; must be positive and can't be greater than 50. For optimal performance, the number of returned users is chosen by TDLib and can be smaller than the specified limit, even if the end of the voter list has not been reached


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPollVoters",
            "chat_id": chat_id,
            "message_id": message_id,
            "option_id": option_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def stopPoll(
        self,
        chat_id: int,
        message_id: int,
        reply_markup: dict = None,
        timeout: float = None,
    ) -> Response:
        """Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set

        Args:
            chat_id (``int``):
                Identifier of the chat to which the poll belongs

            message_id (``int``):
                Identifier of the message containing the poll

            reply_markup (``dict``, optional):
                The new message reply markup; pass null if none; for bots only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "stopPoll",
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": reply_markup,
        }

        return await self.invoke(data, timeout=timeout)

    async def hideSuggestedAction(
        self, action: dict, timeout: float = None
    ) -> Response:
        """Hides a suggested action

        Args:
            action (``dict``):
                Suggested action to hide


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "hideSuggestedAction",
            "action": action,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLoginUrlInfo(
        self, chat_id: int, message_id: int, button_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a button of type inlineKeyboardButtonTypeLoginUrl. The method needs to be called when the user presses the button

        Args:
            chat_id (``int``):
                Chat identifier of the message with the button

            message_id (``int``):
                Message identifier of the message with the button

            button_id (``int``):
                Button identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLoginUrlInfo",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLoginUrl(
        self,
        chat_id: int,
        message_id: int,
        button_id: int,
        allow_write_access: bool,
        timeout: float = None,
    ) -> Response:
        """Returns an HTTP URL which can be used to automatically authorize the user on a website after clicking an inline button of type inlineKeyboardButtonTypeLoginUrl. Use the method getLoginUrlInfo to find whether a prior user confirmation is needed. If an error is returned, then the button must be handled as an ordinary URL button

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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLoginUrl",
            "chat_id": chat_id,
            "message_id": message_id,
            "button_id": button_id,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data, timeout=timeout)

    async def getInlineQueryResults(
        self,
        bot_user_id: int,
        chat_id: int,
        query: str,
        offset: str,
        user_location: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sends an inline query to a bot and returns its results. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Args:
            bot_user_id (``int``):
                The identifier of the target bot

            chat_id (``int``):
                Identifier of the chat where the query was sent

            query (``str``):
                Text of the query

            offset (``str``):
                Offset of the first entry to return

            user_location (``dict``, optional):
                Location of the user; pass null if unknown or the bot doesn't need user's location


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getInlineQueryResults",
            "bot_user_id": bot_user_id,
            "chat_id": chat_id,
            "user_location": user_location,
            "query": query,
            "offset": offset,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerInlineQuery(
        self,
        inline_query_id: int,
        is_personal: bool,
        results: list,
        cache_time: int,
        next_offset: str,
        switch_pm_parameter: str,
        switch_pm_text: str = None,
        timeout: float = None,
    ) -> Response:
        """Sets the result of an inline query; for bots only

        Args:
            inline_query_id (``int``):
                Identifier of the inline query

            is_personal (``bool``):
                Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query

            results (``list``):
                The results of the query

            cache_time (``int``):
                Allowed time to cache the results of the query, in seconds

            next_offset (``str``):
                Offset for the next inline query; pass an empty string if there are no more results

            switch_pm_parameter (``str``):
                The parameter for the bot start message

            switch_pm_text (``str``, optional):
                If non-empty, this text must be shown on the button that opens a private chat with the bot and sends a start message to the bot with the parameter switch_pm_parameter


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerInlineQuery",
            "inline_query_id": inline_query_id,
            "is_personal": is_personal,
            "results": results,
            "cache_time": cache_time,
            "next_offset": next_offset,
            "switch_pm_text": switch_pm_text,
            "switch_pm_parameter": switch_pm_parameter,
        }

        return await self.invoke(data, timeout=timeout)

    async def getWebAppUrl(
        self,
        bot_user_id: int,
        url: str,
        application_name: str,
        theme: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns an HTTPS URL of a Web App to open after keyboardButtonTypeWebApp button is pressed

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            url (``str``):
                The URL from the keyboardButtonTypeWebApp button

            application_name (``str``):
                Short name of the application; 0-64 English letters, digits, and underscores

            theme (``dict``, optional):
                Preferred Web App theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getWebAppUrl",
            "bot_user_id": bot_user_id,
            "url": url,
            "theme": theme,
            "application_name": application_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendWebAppData(
        self, bot_user_id: int, button_text: str, data: str, timeout: float = None
    ) -> Response:
        """Sends data received from a keyboardButtonTypeWebApp Web App to a bot

        Args:
            bot_user_id (``int``):
                Identifier of the target bot

            button_text (``str``):
                Text of the keyboardButtonTypeWebApp button, which opened the Web App

            data (``str``):
                Received data


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendWebAppData",
            "bot_user_id": bot_user_id,
            "button_text": button_text,
            "data": data,
        }

        return await self.invoke(data, timeout=timeout)

    async def openWebApp(
        self,
        chat_id: int,
        bot_user_id: int,
        url: str,
        application_name: str,
        reply_to_message_id: int,
        theme: dict = None,
        timeout: float = None,
    ) -> Response:
        """Informs TDLib that a Web App is being opened from attachment menu, a botMenuButton button, an internalLinkTypeAttachmentMenuBot link, or an inlineKeyboardButtonTypeWebApp button. For each bot, a confirmation alert about data sent to the bot must be shown once

        Args:
            chat_id (``int``):
                Identifier of the chat in which the Web App is opened

            bot_user_id (``int``):
                Identifier of the bot, providing the Web App

            url (``str``):
                The URL from an inlineKeyboardButtonTypeWebApp button, a botMenuButton button, or an internalLinkTypeAttachmentMenuBot link, or an empty string otherwise

            application_name (``str``):
                Short name of the application; 0-64 English letters, digits, and underscores

            reply_to_message_id (``int``):
                Identifier of the replied message for the message sent by the Web App; 0 if none

            theme (``dict``, optional):
                Preferred Web App theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "openWebApp",
            "chat_id": chat_id,
            "bot_user_id": bot_user_id,
            "url": url,
            "theme": theme,
            "application_name": application_name,
            "reply_to_message_id": reply_to_message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def closeWebApp(
        self, web_app_launch_id: int, timeout: float = None
    ) -> Response:
        """Informs TDLib that a previously opened Web App was closed

        Args:
            web_app_launch_id (``int``):
                Identifier of Web App launch, received from openWebApp


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "closeWebApp",
            "web_app_launch_id": web_app_launch_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerWebAppQuery(
        self, web_app_query_id: str, result: dict, timeout: float = None
    ) -> Response:
        """Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only

        Args:
            web_app_query_id (``str``):
                Identifier of the Web App query

            result (``dict``):
                The result of the query


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerWebAppQuery",
            "web_app_query_id": web_app_query_id,
            "result": result,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCallbackQueryAnswer(
        self, chat_id: int, message_id: int, payload: dict, timeout: float = None
    ) -> Response:
        """Sends a callback query to a bot and returns an answer. Returns an error with code 502 if the bot fails to answer the query before the query timeout expires

        Args:
            chat_id (``int``):
                Identifier of the chat with the message

            message_id (``int``):
                Identifier of the message from which the query originated

            payload (``dict``):
                Query payload


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCallbackQueryAnswer",
            "chat_id": chat_id,
            "message_id": message_id,
            "payload": payload,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerCallbackQuery(
        self,
        callback_query_id: int,
        text: str,
        show_alert: bool,
        url: str,
        cache_time: int,
        timeout: float = None,
    ) -> Response:
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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerCallbackQuery",
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": show_alert,
            "url": url,
            "cache_time": cache_time,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerShippingQuery(
        self,
        shipping_query_id: int,
        shipping_options: list,
        error_message: str,
        timeout: float = None,
    ) -> Response:
        """Sets the result of a shipping query; for bots only

        Args:
            shipping_query_id (``int``):
                Identifier of the shipping query

            shipping_options (``list``):
                Available shipping options

            error_message (``str``):
                An error message, empty on success


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerShippingQuery",
            "shipping_query_id": shipping_query_id,
            "shipping_options": shipping_options,
            "error_message": error_message,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerPreCheckoutQuery(
        self, pre_checkout_query_id: int, error_message: str, timeout: float = None
    ) -> Response:
        """Sets the result of a pre-checkout query; for bots only

        Args:
            pre_checkout_query_id (``int``):
                Identifier of the pre-checkout query

            error_message (``str``):
                An error message, empty on success


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerPreCheckoutQuery",
            "pre_checkout_query_id": pre_checkout_query_id,
            "error_message": error_message,
        }

        return await self.invoke(data, timeout=timeout)

    async def setGameScore(
        self,
        chat_id: int,
        message_id: int,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
        timeout: float = None,
    ) -> Response:
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
                Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def setInlineGameScore(
        self,
        inline_message_id: str,
        edit_message: bool,
        user_id: int,
        score: int,
        force: bool,
        timeout: float = None,
    ) -> Response:
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
                Pass true to update the score even if it decreases. If the score is 0, the user will be deleted from the high score table


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setInlineGameScore",
            "inline_message_id": inline_message_id,
            "edit_message": edit_message,
            "user_id": user_id,
            "score": score,
            "force": force,
        }

        return await self.invoke(data, timeout=timeout)

    async def getGameHighScores(
        self, chat_id: int, message_id: int, user_id: int, timeout: float = None
    ) -> Response:
        """Returns the high scores for a game and some part of the high score table in the range of the specified user; for bots only

        Args:
            chat_id (``int``):
                The chat that contains the message with the game

            message_id (``int``):
                Identifier of the message

            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGameHighScores",
            "chat_id": chat_id,
            "message_id": message_id,
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getInlineGameHighScores(
        self, inline_message_id: str, user_id: int, timeout: float = None
    ) -> Response:
        """Returns game high scores and some part of the high score table in the range of the specified user; for bots only

        Args:
            inline_message_id (``str``):
                Inline message identifier

            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getInlineGameHighScores",
            "inline_message_id": inline_message_id,
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChatReplyMarkup(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Deletes the default reply markup from a chat. Must be called after a one-time keyboard or a ForceReply reply markup has been used. UpdateChatReplyMarkup will be sent if the reply markup is changed

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                The message identifier of the used keyboard


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChatReplyMarkup",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendChatAction(
        self,
        chat_id: int,
        message_thread_id: int,
        action: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sends a notification about user activity in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the action was performed

            action (``dict``, optional):
                The action description; pass null to cancel the currently active action


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendChatAction",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "action": action,
        }

        return await self.invoke(data, timeout=timeout)

    async def openChat(self, chat_id: int, timeout: float = None) -> Response:
        """Informs TDLib that the chat is opened by the user. Many useful activities depend on the chat being opened or closed (e.g., in supergroups and channels all updates are received only for opened chats)

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "openChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def closeChat(self, chat_id: int, timeout: float = None) -> Response:
        """Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "closeChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def viewMessages(
        self,
        chat_id: int,
        message_thread_id: int,
        message_ids: list,
        force_read: bool,
        timeout: float = None,
    ) -> Response:
        """Informs TDLib that messages are being viewed by the user. Sponsored messages must be marked as viewed only when the entire text of the message is shown on the screen (excluding the button). Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels)

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the messages are being viewed

            message_ids (``list``):
                The identifiers of the messages being viewed

            force_read (``bool``):
                Pass true to mark as read the specified messages even the chat is closed


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "viewMessages",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "message_ids": message_ids,
            "force_read": force_read,
        }

        return await self.invoke(data, timeout=timeout)

    async def openMessageContent(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Identifier of the message with the opened content


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "openMessageContent",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def clickAnimatedEmojiMessage(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Informs TDLib that a message with an animated emoji was clicked by the user. Returns a big animated sticker to be played or a 404 error if usual animation needs to be played

        Args:
            chat_id (``int``):
                Chat identifier of the message

            message_id (``int``):
                Identifier of the clicked message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clickAnimatedEmojiMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getInternalLinkType(self, link: str, timeout: float = None) -> Response:
        """Returns information about the type of an internal link. Returns a 404 error if the link is not internal. Can be called before authorization

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getInternalLinkType",
            "link": link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getExternalLinkInfo(self, link: str, timeout: float = None) -> Response:
        """Returns information about an action to be done when the current user clicks an external link. Don't use this method for links from secret chats if web page preview is disabled in secret chats

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getExternalLinkInfo",
            "link": link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getExternalLink(
        self, link: str, allow_write_access: bool, timeout: float = None
    ) -> Response:
        """Returns an HTTP URL which can be used to automatically authorize the current user on a website after clicking an HTTP link. Use the method getExternalLinkInfo to find whether a prior user confirmation is needed

        Args:
            link (``str``):
                The HTTP link

            allow_write_access (``bool``):
                Pass true if the current user allowed the bot, returned in getExternalLinkInfo, to send them messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getExternalLink",
            "link": link,
            "allow_write_access": allow_write_access,
        }

        return await self.invoke(data, timeout=timeout)

    async def readAllChatMentions(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Marks all mentions in a chat as read

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "readAllChatMentions",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def readAllChatReactions(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Marks all reactions in a chat as read

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "readAllChatReactions",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def createPrivateChat(
        self, user_id: int, force: bool, timeout: float = None
    ) -> Response:
        """Returns an existing chat corresponding to a given user

        Args:
            user_id (``int``):
                User identifier

            force (``bool``):
                Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createPrivateChat",
            "user_id": user_id,
            "force": force,
        }

        return await self.invoke(data, timeout=timeout)

    async def createBasicGroupChat(
        self, basic_group_id: int, force: bool, timeout: float = None
    ) -> Response:
        """Returns an existing chat corresponding to a known basic group

        Args:
            basic_group_id (``int``):
                Basic group identifier

            force (``bool``):
                Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createBasicGroupChat",
            "basic_group_id": basic_group_id,
            "force": force,
        }

        return await self.invoke(data, timeout=timeout)

    async def createSupergroupChat(
        self, supergroup_id: int, force: bool, timeout: float = None
    ) -> Response:
        """Returns an existing chat corresponding to a known supergroup or channel

        Args:
            supergroup_id (``int``):
                Supergroup or channel identifier

            force (``bool``):
                Pass true to create the chat without a network request. In this case all information about the chat except its type, title and photo can be incorrect


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createSupergroupChat",
            "supergroup_id": supergroup_id,
            "force": force,
        }

        return await self.invoke(data, timeout=timeout)

    async def createSecretChat(
        self, secret_chat_id: int, timeout: float = None
    ) -> Response:
        """Returns an existing chat corresponding to a known secret chat

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def createNewBasicGroupChat(
        self, user_ids: list, title: str, timeout: float = None
    ) -> Response:
        """Creates a new basic group and sends a corresponding messageBasicGroupChatCreate. Returns the newly created chat

        Args:
            user_ids (``list``):
                Identifiers of users to be added to the basic group

            title (``str``):
                Title of the new basic group; 1-128 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createNewBasicGroupChat",
            "user_ids": user_ids,
            "title": title,
        }

        return await self.invoke(data, timeout=timeout)

    async def createNewSupergroupChat(
        self,
        title: str,
        is_channel: bool,
        description: str,
        for_import: bool,
        location: dict = None,
        timeout: float = None,
    ) -> Response:
        """Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat

        Args:
            title (``str``):
                Title of the new chat; 1-128 characters

            is_channel (``bool``):
                Pass true to create a channel chat

            description (``str``):
                Chat description; 0-255 characters

            for_import (``bool``):
                Pass true to create a supergroup for importing messages using importMessage

            location (``dict``, optional):
                Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createNewSupergroupChat",
            "title": title,
            "is_channel": is_channel,
            "description": description,
            "location": location,
            "for_import": for_import,
        }

        return await self.invoke(data, timeout=timeout)

    async def createNewSecretChat(
        self, user_id: int, timeout: float = None
    ) -> Response:
        """Creates a new secret chat. Returns the newly created chat

        Args:
            user_id (``int``):
                Identifier of the target user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createNewSecretChat",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def upgradeBasicGroupChatToSupergroupChat(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Creates a new supergroup from an existing basic group and sends a corresponding messageChatUpgradeTo and messageChatUpgradeFrom; requires creator privileges. Deactivates the original basic group

        Args:
            chat_id (``int``):
                Identifier of the chat to upgrade


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "upgradeBasicGroupChatToSupergroupChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatListsToAddChat(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns chat lists to which the chat can be added. This is an offline request

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatListsToAddChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addChatToList(
        self, chat_id: int, chat_list: dict, timeout: float = None
    ) -> Response:
        """Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

        Args:
            chat_id (``int``):
                Chat identifier

            chat_list (``dict``):
                The chat list. Use getChatListsToAddChat to get suitable chat lists


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addChatToList",
            "chat_id": chat_id,
            "chat_list": chat_list,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatFilter(
        self, chat_filter_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a chat filter by its identifier

        Args:
            chat_filter_id (``int``):
                Chat filter identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatFilter",
            "chat_filter_id": chat_filter_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def createChatFilter(self, filter: dict, timeout: float = None) -> Response:
        """Creates new chat filter. Returns information about the created chat filter. There can be up to GetOption("chat_filter_count_max") chat filters, but the limit can be increased with Telegram Premium

        Args:
            filter (``dict``):
                Chat filter


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createChatFilter",
            "filter": filter,
        }

        return await self.invoke(data, timeout=timeout)

    async def editChatFilter(
        self, chat_filter_id: int, filter: dict, timeout: float = None
    ) -> Response:
        """Edits existing chat filter. Returns information about the edited chat filter

        Args:
            chat_filter_id (``int``):
                Chat filter identifier

            filter (``dict``):
                The edited chat filter


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editChatFilter",
            "chat_filter_id": chat_filter_id,
            "filter": filter,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteChatFilter(
        self, chat_filter_id: int, timeout: float = None
    ) -> Response:
        """Deletes existing chat filter

        Args:
            chat_filter_id (``int``):
                Chat filter identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteChatFilter",
            "chat_filter_id": chat_filter_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def reorderChatFilters(
        self, chat_filter_ids: list, main_chat_list_position: int, timeout: float = None
    ) -> Response:
        """Changes the order of chat filters

        Args:
            chat_filter_ids (``list``):
                Identifiers of chat filters in the new correct order

            main_chat_list_position (``int``):
                Position of the main chat list among chat filters, 0-based. Can be non-zero only for Premium users


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reorderChatFilters",
            "chat_filter_ids": chat_filter_ids,
            "main_chat_list_position": main_chat_list_position,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecommendedChatFilters(self, timeout: float = None) -> Response:
        """Returns recommended chat filters for the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecommendedChatFilters",
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatFilterDefaultIconName(
        self, filter: dict, timeout: float = None
    ) -> Response:
        """Returns default icon name for a filter. Can be called synchronously

        Args:
            filter (``dict``):
                Chat filter


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatFilterDefaultIconName",
            "filter": filter,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatTitle(
        self, chat_id: int, title: str, timeout: float = None
    ) -> Response:
        """Changes the chat title. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            title (``str``):
                New title of the chat; 1-128 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatTitle",
            "chat_id": chat_id,
            "title": title,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatPhoto(
        self, chat_id: int, photo: dict = None, timeout: float = None
    ) -> Response:
        """Changes the photo of a chat. Supported only for basic groups, supergroups and channels. Requires can_change_info administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            photo (``dict``, optional):
                New chat photo; pass null to delete the chat photo


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatPhoto",
            "chat_id": chat_id,
            "photo": photo,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatMessageTtl(
        self, chat_id: int, ttl: int, timeout: float = None
    ) -> Response:
        """Changes the message TTL in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channels Message TTL can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).

        Args:
            chat_id (``int``):
                Chat identifier

            ttl (``int``):
                New TTL value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatMessageTtl",
            "chat_id": chat_id,
            "ttl": ttl,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatPermissions(
        self, chat_id: int, permissions: dict, timeout: float = None
    ) -> Response:
        """Changes the chat members permissions. Supported only for basic groups and supergroups. Requires can_restrict_members administrator right

        Args:
            chat_id (``int``):
                Chat identifier

            permissions (``dict``):
                New non-administrator members permissions in the chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatPermissions",
            "chat_id": chat_id,
            "permissions": permissions,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatTheme(
        self, chat_id: int, theme_name: str, timeout: float = None
    ) -> Response:
        """Changes the chat theme. Supported only in private and secret chats

        Args:
            chat_id (``int``):
                Chat identifier

            theme_name (``str``):
                Name of the new chat theme; pass an empty string to return the default theme


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatTheme",
            "chat_id": chat_id,
            "theme_name": theme_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatDraftMessage(
        self,
        chat_id: int,
        message_thread_id: int,
        draft_message: dict = None,
        timeout: float = None,
    ) -> Response:
        """Changes the draft message in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            message_thread_id (``int``):
                If not 0, a message thread identifier in which the draft was changed

            draft_message (``dict``, optional):
                New draft message; pass null to remove the draft


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatDraftMessage",
            "chat_id": chat_id,
            "message_thread_id": message_thread_id,
            "draft_message": draft_message,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatNotificationSettings(
        self, chat_id: int, notification_settings: dict, timeout: float = None
    ) -> Response:
        """Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed

        Args:
            chat_id (``int``):
                Chat identifier

            notification_settings (``dict``):
                New notification settings for the chat. If the chat is muted for more than 366 days, it is considered to be muted forever


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatNotificationSettings",
            "chat_id": chat_id,
            "notification_settings": notification_settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleChatHasProtectedContent(
        self, chat_id: int, has_protected_content: bool, timeout: float = None
    ) -> Response:
        """Changes the ability of users to save, forward, or copy chat content. Supported only for basic groups, supergroups and channels. Requires owner privileges

        Args:
            chat_id (``int``):
                Chat identifier

            has_protected_content (``bool``):
                New value of has_protected_content


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleChatHasProtectedContent",
            "chat_id": chat_id,
            "has_protected_content": has_protected_content,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleChatIsMarkedAsUnread(
        self, chat_id: int, is_marked_as_unread: bool, timeout: float = None
    ) -> Response:
        """Changes the marked as unread state of a chat

        Args:
            chat_id (``int``):
                Chat identifier

            is_marked_as_unread (``bool``):
                New value of is_marked_as_unread


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleChatIsMarkedAsUnread",
            "chat_id": chat_id,
            "is_marked_as_unread": is_marked_as_unread,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleChatDefaultDisableNotification(
        self, chat_id: int, default_disable_notification: bool, timeout: float = None
    ) -> Response:
        """Changes the value of the default disable_notification parameter, used when a message is sent to a chat

        Args:
            chat_id (``int``):
                Chat identifier

            default_disable_notification (``bool``):
                New value of default_disable_notification


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleChatDefaultDisableNotification",
            "chat_id": chat_id,
            "default_disable_notification": default_disable_notification,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatAvailableReactions(
        self, chat_id: int, available_reactions: dict, timeout: float = None
    ) -> Response:
        """Changes reactions, available in a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

        Args:
            chat_id (``int``):
                Identifier of the chat

            available_reactions (``dict``):
                Reactions available in the chat. All emoji reactions must be active


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatAvailableReactions",
            "chat_id": chat_id,
            "available_reactions": available_reactions,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatClientData(
        self, chat_id: int, client_data: str, timeout: float = None
    ) -> Response:
        """Changes application-specific data associated with a chat

        Args:
            chat_id (``int``):
                Chat identifier

            client_data (``str``):
                New value of client_data


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatClientData",
            "chat_id": chat_id,
            "client_data": client_data,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatDescription(
        self, chat_id: int, description: str, timeout: float = None
    ) -> Response:
        """Changes information about a chat. Available for basic groups, supergroups, and channels. Requires can_change_info administrator right

        Args:
            chat_id (``int``):
                Identifier of the chat

            description (``str``):
                New chat description; 0-255 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatDescription",
            "chat_id": chat_id,
            "description": description,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatDiscussionGroup(
        self, chat_id: int, discussion_chat_id: int, timeout: float = None
    ) -> Response:
        """Changes the discussion group of a channel chat; requires can_change_info administrator right in the channel if it is specified

        Args:
            chat_id (``int``):
                Identifier of the channel chat. Pass 0 to remove a link from the supergroup passed in the second argument to a linked channel chat (requires can_pin_messages rights in the supergroup)

            discussion_chat_id (``int``):
                Identifier of a new channel's discussion group. Use 0 to remove the discussion group. Use the method getSuitableDiscussionChats to find all suitable groups. Basic group chats must be first upgraded to supergroup chats. If new chat members don't have access to old messages in the supergroup, then toggleSupergroupIsAllHistoryAvailable must be used first to change that


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatDiscussionGroup",
            "chat_id": chat_id,
            "discussion_chat_id": discussion_chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatLocation(
        self, chat_id: int, location: dict, timeout: float = None
    ) -> Response:
        """Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use

        Args:
            chat_id (``int``):
                Chat identifier

            location (``dict``):
                New location for the chat; must be valid and not null


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatLocation",
            "chat_id": chat_id,
            "location": location,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatSlowModeDelay(
        self, chat_id: int, slow_mode_delay: int, timeout: float = None
    ) -> Response:
        """Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights

        Args:
            chat_id (``int``):
                Chat identifier

            slow_mode_delay (``int``):
                New slow mode delay for the chat, in seconds; must be one of 0, 10, 30, 60, 300, 900, 3600


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatSlowModeDelay",
            "chat_id": chat_id,
            "slow_mode_delay": slow_mode_delay,
        }

        return await self.invoke(data, timeout=timeout)

    async def pinChatMessage(
        self,
        chat_id: int,
        message_id: int,
        disable_notification: bool,
        only_for_self: bool,
        timeout: float = None,
    ) -> Response:
        """Pins a message in a chat; requires can_pin_messages rights or can_edit_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_id (``int``):
                Identifier of the new pinned message

            disable_notification (``bool``):
                Pass true to disable notification about the pinned message. Notifications are always disabled in channels and private chats

            only_for_self (``bool``):
                Pass true to pin the message only for self; private chats only


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "pinChatMessage",
            "chat_id": chat_id,
            "message_id": message_id,
            "disable_notification": disable_notification,
            "only_for_self": only_for_self,
        }

        return await self.invoke(data, timeout=timeout)

    async def unpinChatMessage(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat

            message_id (``int``):
                Identifier of the removed pinned message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "unpinChatMessage",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def unpinAllChatMessages(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Removes all pinned messages from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel

        Args:
            chat_id (``int``):
                Identifier of the chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "unpinAllChatMessages",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def joinChat(self, chat_id: int, timeout: float = None) -> Response:
        """Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "joinChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def leaveChat(self, chat_id: int, timeout: float = None) -> Response:
        """Removes the current user from chat members. Private and secret chats can't be left using this method

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "leaveChat",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addChatMember(
        self, chat_id: int, user_id: int, forward_limit: int, timeout: float = None
    ) -> Response:
        """Adds a new member to a chat. Members can't be added to private or secret chats

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user

            forward_limit (``int``):
                The number of earlier messages from the chat to be forwarded to the new member; up to 100. Ignored for supergroups and channels, or if the added user is a bot


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addChatMember",
            "chat_id": chat_id,
            "user_id": user_id,
            "forward_limit": forward_limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def addChatMembers(
        self, chat_id: int, user_ids: list, timeout: float = None
    ) -> Response:
        """Adds multiple new members to a chat. Currently, this method is only available for supergroups and channels. This method can't be used to join a chat. Members can't be added to a channel if it has more than 200 members

        Args:
            chat_id (``int``):
                Chat identifier

            user_ids (``list``):
                Identifiers of the users to be added to the chat. The maximum number of added users is 20 for supergroups and 100 for channels


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addChatMembers",
            "chat_id": chat_id,
            "user_ids": user_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def setChatMemberStatus(
        self, chat_id: int, member_id: dict, status: dict, timeout: float = None
    ) -> Response:
        """Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for transferring chat ownership; use transferChatOwnership instead. Use addChatMember or banChatMember if some additional parameters needs to be passed

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``dict``):
                Member identifier. Chats can be only banned and unbanned in supergroups and channels

            status (``dict``):
                The new status of the member in the chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setChatMemberStatus",
            "chat_id": chat_id,
            "member_id": member_id,
            "status": status,
        }

        return await self.invoke(data, timeout=timeout)

    async def banChatMember(
        self,
        chat_id: int,
        member_id: dict,
        banned_until_date: int,
        revoke_messages: bool,
        timeout: float = None,
    ) -> Response:
        """Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``dict``):
                Member identifier

            banned_until_date (``int``):
                Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups and if a chat is banned

            revoke_messages (``bool``):
                Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "banChatMember",
            "chat_id": chat_id,
            "member_id": member_id,
            "banned_until_date": banned_until_date,
            "revoke_messages": revoke_messages,
        }

        return await self.invoke(data, timeout=timeout)

    async def canTransferOwnership(self, timeout: float = None) -> Response:
        """Checks whether the current session can be used to transfer a chat ownership to another user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "canTransferOwnership",
        }

        return await self.invoke(data, timeout=timeout)

    async def transferChatOwnership(
        self, chat_id: int, user_id: int, password: str, timeout: float = None
    ) -> Response:
        """Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user to which transfer the ownership. The ownership can't be transferred to a bot or to a deleted user

            password (``str``):
                The 2-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "transferChatOwnership",
            "chat_id": chat_id,
            "user_id": user_id,
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatMember(
        self, chat_id: int, member_id: dict, timeout: float = None
    ) -> Response:
        """Returns information about a single member of a chat

        Args:
            chat_id (``int``):
                Chat identifier

            member_id (``dict``):
                Member identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatMember",
            "chat_id": chat_id,
            "member_id": member_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchChatMembers(
        self,
        chat_id: int,
        query: str,
        limit: int,
        filter: dict = None,
        timeout: float = None,
    ) -> Response:
        """Searches for a specified query in the first name, last name and username of the members of a specified chat. Requires administrator rights in channels

        Args:
            chat_id (``int``):
                Chat identifier

            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of users to be returned; up to 200

            filter (``dict``, optional):
                The type of users to search for; pass null to search among all chat members


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchChatMembers",
            "chat_id": chat_id,
            "query": query,
            "limit": limit,
            "filter": filter,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatAdministrators(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns a list of administrators of the chat with their custom titles

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatAdministrators",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def clearAllDraftMessages(
        self, exclude_secret_chats: bool, timeout: float = None
    ) -> Response:
        """Clears message drafts in all chats

        Args:
            exclude_secret_chats (``bool``):
                Pass true to keep local message drafts in secret chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearAllDraftMessages",
            "exclude_secret_chats": exclude_secret_chats,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSavedNotificationSound(
        self, notification_sound_id: int, timeout: float = None
    ) -> Response:
        """Returns saved notification sound by its identifier. Returns a 404 error if there is no saved notification sound with the specified identifier

        Args:
            notification_sound_id (``int``):
                Identifier of the notification sound


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSavedNotificationSound",
            "notification_sound_id": notification_sound_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSavedNotificationSounds(self, timeout: float = None) -> Response:
        """Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSavedNotificationSounds",
        }

        return await self.invoke(data, timeout=timeout)

    async def addSavedNotificationSound(
        self, sound: dict, timeout: float = None
    ) -> Response:
        """Adds a new notification sound to the list of saved notification sounds. The new notification sound is added to the top of the list. If it is already in the list, its position isn't changed

        Args:
            sound (``dict``):
                Notification sound file to add


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addSavedNotificationSound",
            "sound": sound,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeSavedNotificationSound(
        self, notification_sound_id: int, timeout: float = None
    ) -> Response:
        """Removes a notification sound from the list of saved notification sounds

        Args:
            notification_sound_id (``int``):
                Identifier of the notification sound


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeSavedNotificationSound",
            "notification_sound_id": notification_sound_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatNotificationSettingsExceptions(
        self, compare_sound: bool, scope: dict = None, timeout: float = None
    ) -> Response:
        """Returns list of chats with non-default notification settings

        Args:
            compare_sound (``bool``):
                Pass true to include in the response chats with only non-default sound

            scope (``dict``, optional):
                If specified, only chats from the scope will be returned; pass null to return chats from all scopes


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatNotificationSettingsExceptions",
            "scope": scope,
            "compare_sound": compare_sound,
        }

        return await self.invoke(data, timeout=timeout)

    async def getScopeNotificationSettings(
        self, scope: dict, timeout: float = None
    ) -> Response:
        """Returns the notification settings for chats of a given type

        Args:
            scope (``dict``):
                Types of chats for which to return the notification settings information


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getScopeNotificationSettings",
            "scope": scope,
        }

        return await self.invoke(data, timeout=timeout)

    async def setScopeNotificationSettings(
        self, scope: dict, notification_settings: dict, timeout: float = None
    ) -> Response:
        """Changes notification settings for chats of a given type

        Args:
            scope (``dict``):
                Types of chats for which to change the notification settings

            notification_settings (``dict``):
                The new notification settings for the given scope


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setScopeNotificationSettings",
            "scope": scope,
            "notification_settings": notification_settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def resetAllNotificationSettings(self, timeout: float = None) -> Response:
        """Resets all notification settings to their default values. By default, all chats are unmuted and message previews are shown


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resetAllNotificationSettings",
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleChatIsPinned(
        self, chat_list: dict, chat_id: int, is_pinned: bool, timeout: float = None
    ) -> Response:
        """Changes the pinned state of a chat. There can be up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium

        Args:
            chat_list (``dict``):
                Chat list in which to change the pinned state of the chat

            chat_id (``int``):
                Chat identifier

            is_pinned (``bool``):
                Pass true to pin the chat; pass false to unpin it


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleChatIsPinned",
            "chat_list": chat_list,
            "chat_id": chat_id,
            "is_pinned": is_pinned,
        }

        return await self.invoke(data, timeout=timeout)

    async def setPinnedChats(
        self, chat_list: dict, chat_ids: list, timeout: float = None
    ) -> Response:
        """Changes the order of pinned chats

        Args:
            chat_list (``dict``):
                Chat list in which to change the order of pinned chats

            chat_ids (``list``):
                The new list of pinned chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setPinnedChats",
            "chat_list": chat_list,
            "chat_ids": chat_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getAttachmentMenuBot(
        self, bot_user_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a bot that can be added to attachment menu

        Args:
            bot_user_id (``int``):
                Bot's user identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAttachmentMenuBot",
            "bot_user_id": bot_user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleBotIsAddedToAttachmentMenu(
        self, bot_user_id: int, is_added: bool, timeout: float = None
    ) -> Response:
        """Adds or removes a bot to attachment menu. Bot can be added to attachment menu, only if userTypeBot.can_be_added_to_attachment_menu == true

        Args:
            bot_user_id (``int``):
                Bot's user identifier

            is_added (``bool``):
                Pass true to add the bot to attachment menu; pass false to remove the bot from attachment menu


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleBotIsAddedToAttachmentMenu",
            "bot_user_id": bot_user_id,
            "is_added": is_added,
        }

        return await self.invoke(data, timeout=timeout)

    async def getThemedEmojiStatuses(self, timeout: float = None) -> Response:
        """Returns up to 8 themed emoji statuses, which color must be changed to the color of the Telegram Premium badge


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getThemedEmojiStatuses",
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecentEmojiStatuses(self, timeout: float = None) -> Response:
        """Returns recent emoji statuses


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecentEmojiStatuses",
        }

        return await self.invoke(data, timeout=timeout)

    async def getDefaultEmojiStatuses(self, timeout: float = None) -> Response:
        """Returns default emoji statuses


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getDefaultEmojiStatuses",
        }

        return await self.invoke(data, timeout=timeout)

    async def clearRecentEmojiStatuses(self, timeout: float = None) -> Response:
        """Clears the list of recently used emoji statuses


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearRecentEmojiStatuses",
        }

        return await self.invoke(data, timeout=timeout)

    async def downloadFile(
        self,
        file_id: int,
        priority: int,
        offset: int,
        limit: int,
        synchronous: bool,
        timeout: float = None,
    ) -> Response:
        """Downloads a file from the cloud. Download progress and completion of the download will be notified through updateFile updates

        Args:
            file_id (``int``):
                Identifier of the file to download

            priority (``int``):
                Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first

            offset (``int``):
                The starting position from which the file needs to be downloaded

            limit (``int``):
                Number of bytes which need to be downloaded starting from the "offset" position before the download will automatically be canceled; use 0 to download without a limit

            synchronous (``bool``):
                Pass true to return response only after the file download has succeeded, has failed, has been canceled, or a new downloadFile request with different offset/limit parameters was sent; pass false to return file state immediately, just after the download has been started


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "downloadFile",
            "file_id": file_id,
            "priority": priority,
            "offset": offset,
            "limit": limit,
            "synchronous": synchronous,
        }

        return await self.invoke(data, timeout=timeout)

    async def getFileDownloadedPrefixSize(
        self, file_id: int, offset: int, timeout: float = None
    ) -> Response:
        """Returns file downloaded prefix size from a given offset, in bytes

        Args:
            file_id (``int``):
                Identifier of the file

            offset (``int``):
                Offset from which downloaded prefix size needs to be calculated


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getFileDownloadedPrefixSize",
            "file_id": file_id,
            "offset": offset,
        }

        return await self.invoke(data, timeout=timeout)

    async def cancelDownloadFile(
        self, file_id: int, only_if_pending: bool, timeout: float = None
    ) -> Response:
        """Stops the downloading of a file. If a file has already been downloaded, does nothing

        Args:
            file_id (``int``):
                Identifier of a file to stop downloading

            only_if_pending (``bool``):
                Pass true to stop downloading only if it hasn't been started, i.e. request hasn't been sent to server


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "cancelDownloadFile",
            "file_id": file_id,
            "only_if_pending": only_if_pending,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSuggestedFileName(
        self, file_id: int, directory: str, timeout: float = None
    ) -> Response:
        """Returns suggested name for saving a file in a given directory

        Args:
            file_id (``int``):
                Identifier of the file

            directory (``str``):
                Directory in which the file is supposed to be saved


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSuggestedFileName",
            "file_id": file_id,
            "directory": directory,
        }

        return await self.invoke(data, timeout=timeout)

    async def preliminaryUploadFile(
        self, file: dict, priority: int, file_type: dict = None, timeout: float = None
    ) -> Response:
        """Preliminary uploads a file to the cloud before sending it in a message, which can be useful for uploading of being recorded voice and video notes. Updates updateFile will be used to notify about upload progress and successful completion of the upload. The file will not have a persistent remote identifier until it will be sent in a message

        Args:
            file (``dict``):
                File to upload

            priority (``int``):
                Priority of the upload (1-32). The higher the priority, the earlier the file will be uploaded. If the priorities of two files are equal, then the first one for which preliminaryUploadFile was called will be uploaded first

            file_type (``dict``, optional):
                File type; pass null if unknown


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "preliminaryUploadFile",
            "file": file,
            "file_type": file_type,
            "priority": priority,
        }

        return await self.invoke(data, timeout=timeout)

    async def cancelPreliminaryUploadFile(
        self, file_id: int, timeout: float = None
    ) -> Response:
        """Stops the preliminary uploading of a file. Supported only for files uploaded by using preliminaryUploadFile. For other files the behavior is undefined

        Args:
            file_id (``int``):
                Identifier of the file to stop uploading


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "cancelPreliminaryUploadFile",
            "file_id": file_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def writeGeneratedFilePart(
        self, generation_id: int, offset: int, data: bytes, timeout: float = None
    ) -> Response:
        """Writes a part of a generated file. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct write to the destination file

        Args:
            generation_id (``int``):
                The identifier of the generation process

            offset (``int``):
                The offset from which to write the data to the file

            data (``bytes``):
                The data to write


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "writeGeneratedFilePart",
            "generation_id": generation_id,
            "offset": offset,
            "data": data,
        }

        return await self.invoke(data, timeout=timeout)

    async def setFileGenerationProgress(
        self,
        generation_id: int,
        expected_size: int,
        local_prefix_size: int,
        timeout: float = None,
    ) -> Response:
        """Informs TDLib on a file generation progress

        Args:
            generation_id (``int``):
                The identifier of the generation process

            expected_size (``int``):
                Expected size of the generated file, in bytes; 0 if unknown

            local_prefix_size (``int``):
                The number of bytes already generated


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setFileGenerationProgress",
            "generation_id": generation_id,
            "expected_size": expected_size,
            "local_prefix_size": local_prefix_size,
        }

        return await self.invoke(data, timeout=timeout)

    async def finishFileGeneration(
        self, generation_id: int, error: dict = None, timeout: float = None
    ) -> Response:
        """Finishes the file generation

        Args:
            generation_id (``int``):
                The identifier of the generation process

            error (``dict``, optional):
                If passed, the file generation has failed and must be terminated; pass null if the file generation succeeded


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "finishFileGeneration",
            "generation_id": generation_id,
            "error": error,
        }

        return await self.invoke(data, timeout=timeout)

    async def readFilePart(
        self, file_id: int, offset: int, count: int, timeout: float = None
    ) -> Response:
        """Reads a part of a file from the TDLib file cache and returns read bytes. This method is intended to be used only if the application has no direct access to TDLib's file system, because it is usually slower than a direct read from the file

        Args:
            file_id (``int``):
                Identifier of the file. The file must be located in the TDLib file cache

            offset (``int``):
                The offset from which to read the file

            count (``int``):
                Number of bytes to read. An error will be returned if there are not enough bytes available in the file from the specified position. Pass 0 to read all available data from the specified position


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "readFilePart",
            "file_id": file_id,
            "offset": offset,
            "count": count,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteFile(self, file_id: int, timeout: float = None) -> Response:
        """Deletes a file from the TDLib file cache

        Args:
            file_id (``int``):
                Identifier of the file to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteFile",
            "file_id": file_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addFileToDownloads(
        self,
        file_id: int,
        chat_id: int,
        message_id: int,
        priority: int,
        timeout: float = None,
    ) -> Response:
        """Adds a file from a message to the list of file downloads. Download progress and completion of the download will be notified through updateFile updates. If message database is used, the list of file downloads is persistent across application restarts. The downloading is independent from download using downloadFile, i.e. it continues if downloadFile is canceled or is used to download a part of the file

        Args:
            file_id (``int``):
                Identifier of the file to download

            chat_id (``int``):
                Chat identifier of the message with the file

            message_id (``int``):
                Message identifier

            priority (``int``):
                Priority of the download (1-32). The higher the priority, the earlier the file will be downloaded. If the priorities of two files are equal, then the last one for which downloadFile/addFileToDownloads was called will be downloaded first


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addFileToDownloads",
            "file_id": file_id,
            "chat_id": chat_id,
            "message_id": message_id,
            "priority": priority,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleDownloadIsPaused(
        self, file_id: int, is_paused: bool, timeout: float = None
    ) -> Response:
        """Changes pause state of a file in the file download list

        Args:
            file_id (``int``):
                Identifier of the downloaded file

            is_paused (``bool``):
                Pass true if the download is paused


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleDownloadIsPaused",
            "file_id": file_id,
            "is_paused": is_paused,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleAllDownloadsArePaused(
        self, are_paused: bool, timeout: float = None
    ) -> Response:
        """Changes pause state of all files in the file download list

        Args:
            are_paused (``bool``):
                Pass true to pause all downloads; pass false to unpause them


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleAllDownloadsArePaused",
            "are_paused": are_paused,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeFileFromDownloads(
        self, file_id: int, delete_from_cache: bool, timeout: float = None
    ) -> Response:
        """Removes a file from the file download list

        Args:
            file_id (``int``):
                Identifier of the downloaded file

            delete_from_cache (``bool``):
                Pass true to delete the file from the TDLib file cache


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeFileFromDownloads",
            "file_id": file_id,
            "delete_from_cache": delete_from_cache,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeAllFilesFromDownloads(
        self,
        only_active: bool,
        only_completed: bool,
        delete_from_cache: bool,
        timeout: float = None,
    ) -> Response:
        """Removes all files from the file download list

        Args:
            only_active (``bool``):
                Pass true to remove only active downloads, including paused

            only_completed (``bool``):
                Pass true to remove only completed downloads

            delete_from_cache (``bool``):
                Pass true to delete the file from the TDLib file cache


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeAllFilesFromDownloads",
            "only_active": only_active,
            "only_completed": only_completed,
            "delete_from_cache": delete_from_cache,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchFileDownloads(
        self,
        only_active: bool,
        only_completed: bool,
        offset: str,
        limit: int,
        query: str = None,
        timeout: float = None,
    ) -> Response:
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

            query (``str``, optional):
                Query to search for; may be empty to return all downloaded files


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchFileDownloads",
            "query": query,
            "only_active": only_active,
            "only_completed": only_completed,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageFileType(
        self, message_file_head: str, timeout: float = None
    ) -> Response:
        """Returns information about a file with messages exported from another application

        Args:
            message_file_head (``str``):
                Beginning of the message file; up to 100 first lines


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageFileType",
            "message_file_head": message_file_head,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageImportConfirmationText(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns a confirmation text to be shown to the user before starting message import

        Args:
            chat_id (``int``):
                Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageImportConfirmationText",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def importMessages(
        self,
        chat_id: int,
        message_file: dict,
        attached_files: list,
        timeout: float = None,
    ) -> Response:
        """Imports messages exported from another app

        Args:
            chat_id (``int``):
                Identifier of a chat to which the messages will be imported. It must be an identifier of a private chat with a mutual contact or an identifier of a supergroup chat with can_change_info administrator right

            message_file (``dict``):
                File with messages to import. Only inputFileLocal and inputFileGenerated are supported. The file must not be previously uploaded

            attached_files (``list``):
                Files used in the imported messages. Only inputFileLocal and inputFileGenerated are supported. The files must not be previously uploaded


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "importMessages",
            "chat_id": chat_id,
            "message_file": message_file,
            "attached_files": attached_files,
        }

        return await self.invoke(data, timeout=timeout)

    async def replacePrimaryChatInviteLink(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "replacePrimaryChatInviteLink",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def createChatInviteLink(
        self,
        chat_id: int,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
        timeout: float = None,
    ) -> Response:
        """Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat

        Args:
            chat_id (``int``):
                Chat identifier

            name (``str``):
                Invite link name; 0-32 characters

            expiration_date (``int``):
                Point in time (Unix timestamp) when the link will expire; pass 0 if never

            member_limit (``int``):
                The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited

            creates_join_request (``bool``):
                Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createChatInviteLink",
            "chat_id": chat_id,
            "name": name,
            "expiration_date": expiration_date,
            "member_limit": member_limit,
            "creates_join_request": creates_join_request,
        }

        return await self.invoke(data, timeout=timeout)

    async def editChatInviteLink(
        self,
        chat_id: int,
        invite_link: str,
        name: str,
        expiration_date: int,
        member_limit: int,
        creates_join_request: bool,
        timeout: float = None,
    ) -> Response:
        """Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to be edited

            name (``str``):
                Invite link name; 0-32 characters

            expiration_date (``int``):
                Point in time (Unix timestamp) when the link will expire; pass 0 if never

            member_limit (``int``):
                The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited

            creates_join_request (``bool``):
                Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def getChatInviteLink(
        self, chat_id: int, invite_link: str, timeout: float = None
    ) -> Response:
        """Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to get


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatInviteLinkCounts(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatInviteLinkCounts",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatInviteLinks(
        self,
        chat_id: int,
        creator_user_id: int,
        is_revoked: bool,
        offset_date: int,
        offset_invite_link: str,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links

        Args:
            chat_id (``int``):
                Chat identifier

            creator_user_id (``int``):
                User identifier of a chat administrator. Must be an identifier of the current user for non-owner

            is_revoked (``bool``):
                Pass true if revoked links needs to be returned instead of active or expired

            offset_date (``int``):
                Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning

            offset_invite_link (``str``):
                Invite link starting after which to return invite links; use empty string to get results from the beginning

            limit (``int``):
                The maximum number of invite links to return; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def getChatInviteLinkMembers(
        self,
        chat_id: int,
        invite_link: str,
        limit: int,
        offset_member: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to return chat members

            limit (``int``):
                The maximum number of chat members to return; up to 100

            offset_member (``dict``, optional):
                A chat member from which to return next chat members; pass null to get results from the beginning


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatInviteLinkMembers",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "offset_member": offset_member,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def revokeChatInviteLink(
        self, chat_id: int, invite_link: str, timeout: float = None
    ) -> Response:
        """Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to be revoked


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "revokeChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteRevokedChatInviteLink(
        self, chat_id: int, invite_link: str, timeout: float = None
    ) -> Response:
        """Deletes revoked chat invite links. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link to revoke


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteRevokedChatInviteLink",
            "chat_id": chat_id,
            "invite_link": invite_link,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteAllRevokedChatInviteLinks(
        self, chat_id: int, creator_user_id: int, timeout: float = None
    ) -> Response:
        """Deletes all revoked chat invite links created by a given chat administrator. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

        Args:
            chat_id (``int``):
                Chat identifier

            creator_user_id (``int``):
                User identifier of a chat administrator, which links will be deleted. Must be an identifier of the current user for non-owner


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteAllRevokedChatInviteLinks",
            "chat_id": chat_id,
            "creator_user_id": creator_user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkChatInviteLink(
        self, invite_link: str, timeout: float = None
    ) -> Response:
        """Checks the validity of an invite link for a chat and returns information about the corresponding chat

        Args:
            invite_link (``str``):
                Invite link to be checked


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkChatInviteLink",
            "invite_link": invite_link,
        }

        return await self.invoke(data, timeout=timeout)

    async def joinChatByInviteLink(
        self, invite_link: str, timeout: float = None
    ) -> Response:
        """Uses an invite link to add the current user to the chat if possible. May return an error with a message "INVITE_REQUEST_SENT" if only a join request was created

        Args:
            invite_link (``str``):
                Invite link to use


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "joinChatByInviteLink",
            "invite_link": invite_link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatJoinRequests(
        self,
        chat_id: int,
        invite_link: str,
        query: str,
        limit: int,
        offset_request: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns pending join requests in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to return join requests. If empty, all join requests will be returned. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

            query (``str``):
                A query to search for in the first names, last names and usernames of the users to return

            limit (``int``):
                The maximum number of requests to join the chat to return

            offset_request (``dict``, optional):
                A chat join request from which to return next requests; pass null to get results from the beginning


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatJoinRequests",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "query": query,
            "offset_request": offset_request,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def processChatJoinRequest(
        self, chat_id: int, user_id: int, approve: bool, timeout: float = None
    ) -> Response:
        """Handles a pending join request in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            user_id (``int``):
                Identifier of the user that sent the request

            approve (``bool``):
                Pass true to approve the request; pass false to decline it


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "processChatJoinRequest",
            "chat_id": chat_id,
            "user_id": user_id,
            "approve": approve,
        }

        return await self.invoke(data, timeout=timeout)

    async def processChatJoinRequests(
        self, chat_id: int, invite_link: str, approve: bool, timeout: float = None
    ) -> Response:
        """Handles all pending join requests for a given link in a chat

        Args:
            chat_id (``int``):
                Chat identifier

            invite_link (``str``):
                Invite link for which to process join requests. If empty, all join requests will be processed. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links

            approve (``bool``):
                Pass true to approve all requests; pass false to decline them


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "processChatJoinRequests",
            "chat_id": chat_id,
            "invite_link": invite_link,
            "approve": approve,
        }

        return await self.invoke(data, timeout=timeout)

    async def createCall(
        self, user_id: int, protocol: dict, is_video: bool, timeout: float = None
    ) -> Response:
        """Creates a new call

        Args:
            user_id (``int``):
                Identifier of the user to be called

            protocol (``dict``):
                The call protocols supported by the application

            is_video (``bool``):
                Pass true to create a video call


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createCall",
            "user_id": user_id,
            "protocol": protocol,
            "is_video": is_video,
        }

        return await self.invoke(data, timeout=timeout)

    async def acceptCall(
        self, call_id: int, protocol: dict, timeout: float = None
    ) -> Response:
        """Accepts an incoming call

        Args:
            call_id (``int``):
                Call identifier

            protocol (``dict``):
                The call protocols supported by the application


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "acceptCall",
            "call_id": call_id,
            "protocol": protocol,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendCallSignalingData(
        self, call_id: int, data: bytes, timeout: float = None
    ) -> Response:
        """Sends call signaling data

        Args:
            call_id (``int``):
                Call identifier

            data (``bytes``):
                The data


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendCallSignalingData",
            "call_id": call_id,
            "data": data,
        }

        return await self.invoke(data, timeout=timeout)

    async def discardCall(
        self,
        call_id: int,
        is_disconnected: bool,
        duration: int,
        is_video: bool,
        connection_id: int,
        timeout: float = None,
    ) -> Response:
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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "discardCall",
            "call_id": call_id,
            "is_disconnected": is_disconnected,
            "duration": duration,
            "is_video": is_video,
            "connection_id": connection_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendCallRating(
        self,
        call_id: int,
        rating: int,
        comment: str,
        problems: list,
        timeout: float = None,
    ) -> Response:
        """Sends a call rating

        Args:
            call_id (``int``):
                Call identifier

            rating (``int``):
                Call rating; 1-5

            comment (``str``):
                An optional user comment if the rating is less than 5

            problems (``list``):
                List of the exact types of problems with the call, specified by the user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendCallRating",
            "call_id": call_id,
            "rating": rating,
            "comment": comment,
            "problems": problems,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendCallDebugInformation(
        self, call_id: int, debug_information: str, timeout: float = None
    ) -> Response:
        """Sends debug information for a call to Telegram servers

        Args:
            call_id (``int``):
                Call identifier

            debug_information (``str``):
                Debug information in application-specific format


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendCallDebugInformation",
            "call_id": call_id,
            "debug_information": debug_information,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendCallLog(
        self, call_id: int, log_file: dict, timeout: float = None
    ) -> Response:
        """Sends log file for a call to Telegram servers

        Args:
            call_id (``int``):
                Call identifier

            log_file (``dict``):
                Call log file. Only inputFileLocal and inputFileGenerated are supported


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendCallLog",
            "call_id": call_id,
            "log_file": log_file,
        }

        return await self.invoke(data, timeout=timeout)

    async def getVideoChatAvailableParticipants(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns list of participant identifiers, on whose behalf a video chat in the chat can be joined

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getVideoChatAvailableParticipants",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setVideoChatDefaultParticipant(
        self, chat_id: int, default_participant_id: dict, timeout: float = None
    ) -> Response:
        """Changes default participant identifier, on whose behalf a video chat in the chat will be joined

        Args:
            chat_id (``int``):
                Chat identifier

            default_participant_id (``dict``):
                Default group call participant identifier to join the video chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setVideoChatDefaultParticipant",
            "chat_id": chat_id,
            "default_participant_id": default_participant_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def createVideoChat(
        self,
        chat_id: int,
        title: str,
        start_date: int,
        is_rtmp_stream: bool,
        timeout: float = None,
    ) -> Response:
        """Creates a video chat (a group call bound to a chat). Available only for basic groups, supergroups and channels; requires can_manage_video_chats rights

        Args:
            chat_id (``int``):
                Identifier of a chat in which the video chat will be created

            title (``str``):
                Group call title; if empty, chat title will be used

            start_date (``int``):
                Point in time (Unix timestamp) when the group call is supposed to be started by an administrator; 0 to start the video chat immediately. The date must be at least 10 seconds and at most 8 days in the future

            is_rtmp_stream (``bool``):
                Pass true to create an RTMP stream instead of an ordinary video chat; requires creator privileges


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createVideoChat",
            "chat_id": chat_id,
            "title": title,
            "start_date": start_date,
            "is_rtmp_stream": is_rtmp_stream,
        }

        return await self.invoke(data, timeout=timeout)

    async def getVideoChatRtmpUrl(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Returns RTMP URL for streaming to the chat; requires creator privileges

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getVideoChatRtmpUrl",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def replaceVideoChatRtmpUrl(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Replaces the current RTMP URL for streaming to the chat; requires creator privileges

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "replaceVideoChatRtmpUrl",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getGroupCall(self, group_call_id: int, timeout: float = None) -> Response:
        """Returns information about a group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def startScheduledGroupCall(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Starts a scheduled group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "startScheduledGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallEnabledStartNotification(
        self,
        group_call_id: int,
        enabled_start_notification: bool,
        timeout: float = None,
    ) -> Response:
        """Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only

        Args:
            group_call_id (``int``):
                Group call identifier

            enabled_start_notification (``bool``):
                New value of the enabled_start_notification setting


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallEnabledStartNotification",
            "group_call_id": group_call_id,
            "enabled_start_notification": enabled_start_notification,
        }

        return await self.invoke(data, timeout=timeout)

    async def joinGroupCall(
        self,
        group_call_id: int,
        audio_source_id: int,
        payload: str,
        is_muted: bool,
        is_my_video_enabled: bool,
        participant_id: dict = None,
        invite_hash: str = None,
        timeout: float = None,
    ) -> Response:
        """Joins an active group call. Returns join response payload for tgcalls

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

            participant_id (``dict``, optional):
                Identifier of a group call participant, which will be used to join the call; pass null to join as self; video chats only

            invite_hash (``str``, optional):
                If non-empty, invite hash to be used to join the group call without being muted by administrators


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def startGroupCallScreenSharing(
        self,
        group_call_id: int,
        audio_source_id: int,
        payload: str,
        timeout: float = None,
    ) -> Response:
        """Starts screen sharing in a joined group call. Returns join response payload for tgcalls

        Args:
            group_call_id (``int``):
                Group call identifier

            audio_source_id (``int``):
                Screen sharing audio channel synchronization source identifier; received from tgcalls

            payload (``str``):
                Group call join payload; received from tgcalls


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "startGroupCallScreenSharing",
            "group_call_id": group_call_id,
            "audio_source_id": audio_source_id,
            "payload": payload,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallScreenSharingIsPaused(
        self, group_call_id: int, is_paused: bool, timeout: float = None
    ) -> Response:
        """Pauses or unpauses screen sharing in a joined group call

        Args:
            group_call_id (``int``):
                Group call identifier

            is_paused (``bool``):
                True if screen sharing is paused


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallScreenSharingIsPaused",
            "group_call_id": group_call_id,
            "is_paused": is_paused,
        }

        return await self.invoke(data, timeout=timeout)

    async def endGroupCallScreenSharing(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Ends screen sharing in a joined group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "endGroupCallScreenSharing",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setGroupCallTitle(
        self, group_call_id: int, title: str, timeout: float = None
    ) -> Response:
        """Sets group call title. Requires groupCall.can_be_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            title (``str``):
                New group call title; 1-64 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setGroupCallTitle",
            "group_call_id": group_call_id,
            "title": title,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallMuteNewParticipants(
        self, group_call_id: int, mute_new_participants: bool, timeout: float = None
    ) -> Response:
        """Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            mute_new_participants (``bool``):
                New value of the mute_new_participants setting


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallMuteNewParticipants",
            "group_call_id": group_call_id,
            "mute_new_participants": mute_new_participants,
        }

        return await self.invoke(data, timeout=timeout)

    async def inviteGroupCallParticipants(
        self, group_call_id: int, user_ids: list, timeout: float = None
    ) -> Response:
        """Invites users to an active group call. Sends a service message of type messageInviteToGroupCall for video chats

        Args:
            group_call_id (``int``):
                Group call identifier

            user_ids (``list``):
                User identifiers. At most 10 users can be invited simultaneously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "inviteGroupCallParticipants",
            "group_call_id": group_call_id,
            "user_ids": user_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getGroupCallInviteLink(
        self, group_call_id: int, can_self_unmute: bool, timeout: float = None
    ) -> Response:
        """Returns invite link to a video chat in a public chat

        Args:
            group_call_id (``int``):
                Group call identifier

            can_self_unmute (``bool``):
                Pass true if the invite link needs to contain an invite hash, passing which to joinGroupCall would allow the invited user to unmute themselves. Requires groupCall.can_be_managed group call flag


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGroupCallInviteLink",
            "group_call_id": group_call_id,
            "can_self_unmute": can_self_unmute,
        }

        return await self.invoke(data, timeout=timeout)

    async def revokeGroupCallInviteLink(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Revokes invite link for a group call. Requires groupCall.can_be_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "revokeGroupCallInviteLink",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def startGroupCallRecording(
        self,
        group_call_id: int,
        title: str,
        record_video: bool,
        use_portrait_orientation: bool,
        timeout: float = None,
    ) -> Response:
        """Starts recording of an active group call. Requires groupCall.can_be_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier

            title (``str``):
                Group call recording title; 0-64 characters

            record_video (``bool``):
                Pass true to record a video file instead of an audio file

            use_portrait_orientation (``bool``):
                Pass true to use portrait orientation for video instead of landscape one


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "startGroupCallRecording",
            "group_call_id": group_call_id,
            "title": title,
            "record_video": record_video,
            "use_portrait_orientation": use_portrait_orientation,
        }

        return await self.invoke(data, timeout=timeout)

    async def endGroupCallRecording(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Ends recording of an active group call. Requires groupCall.can_be_managed group call flag

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "endGroupCallRecording",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallIsMyVideoPaused(
        self, group_call_id: int, is_my_video_paused: bool, timeout: float = None
    ) -> Response:
        """Toggles whether current user's video is paused

        Args:
            group_call_id (``int``):
                Group call identifier

            is_my_video_paused (``bool``):
                Pass true if the current user's video is paused


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallIsMyVideoPaused",
            "group_call_id": group_call_id,
            "is_my_video_paused": is_my_video_paused,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallIsMyVideoEnabled(
        self, group_call_id: int, is_my_video_enabled: bool, timeout: float = None
    ) -> Response:
        """Toggles whether current user's video is enabled

        Args:
            group_call_id (``int``):
                Group call identifier

            is_my_video_enabled (``bool``):
                Pass true if the current user's video is enabled


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallIsMyVideoEnabled",
            "group_call_id": group_call_id,
            "is_my_video_enabled": is_my_video_enabled,
        }

        return await self.invoke(data, timeout=timeout)

    async def setGroupCallParticipantIsSpeaking(
        self,
        group_call_id: int,
        audio_source: int,
        is_speaking: bool,
        timeout: float = None,
    ) -> Response:
        """Informs TDLib that speaking state of a participant of an active group has changed

        Args:
            group_call_id (``int``):
                Group call identifier

            audio_source (``int``):
                Group call participant's synchronization audio source identifier, or 0 for the current user

            is_speaking (``bool``):
                Pass true if the user is speaking


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setGroupCallParticipantIsSpeaking",
            "group_call_id": group_call_id,
            "audio_source": audio_source,
            "is_speaking": is_speaking,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallParticipantIsMuted(
        self,
        group_call_id: int,
        participant_id: dict,
        is_muted: bool,
        timeout: float = None,
    ) -> Response:
        """Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``dict``):
                Participant identifier

            is_muted (``bool``):
                Pass true to mute the user; pass false to unmute the them


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallParticipantIsMuted",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "is_muted": is_muted,
        }

        return await self.invoke(data, timeout=timeout)

    async def setGroupCallParticipantVolumeLevel(
        self,
        group_call_id: int,
        participant_id: dict,
        volume_level: int,
        timeout: float = None,
    ) -> Response:
        """Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``dict``):
                Participant identifier

            volume_level (``int``):
                New participant's volume level; 1-20000 in hundreds of percents


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setGroupCallParticipantVolumeLevel",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "volume_level": volume_level,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleGroupCallParticipantIsHandRaised(
        self,
        group_call_id: int,
        participant_id: dict,
        is_hand_raised: bool,
        timeout: float = None,
    ) -> Response:
        """Toggles whether a group call participant hand is rased

        Args:
            group_call_id (``int``):
                Group call identifier

            participant_id (``dict``):
                Participant identifier

            is_hand_raised (``bool``):
                Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleGroupCallParticipantIsHandRaised",
            "group_call_id": group_call_id,
            "participant_id": participant_id,
            "is_hand_raised": is_hand_raised,
        }

        return await self.invoke(data, timeout=timeout)

    async def loadGroupCallParticipants(
        self, group_call_id: int, limit: int, timeout: float = None
    ) -> Response:
        """Loads more participants of a group call. The loaded participants will be received through updates. Use the field groupCall.loaded_all_participants to check whether all participants have already been loaded

        Args:
            group_call_id (``int``):
                Group call identifier. The group call must be previously received through getGroupCall and must be joined or being joined

            limit (``int``):
                The maximum number of participants to load; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "loadGroupCallParticipants",
            "group_call_id": group_call_id,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def leaveGroupCall(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Leaves a group call

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "leaveGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def endGroupCall(self, group_call_id: int, timeout: float = None) -> Response:
        """Ends a group call. Requires groupCall.can_be_managed

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "endGroupCall",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getGroupCallStreams(
        self, group_call_id: int, timeout: float = None
    ) -> Response:
        """Returns information about available group call streams

        Args:
            group_call_id (``int``):
                Group call identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGroupCallStreams",
            "group_call_id": group_call_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getGroupCallStreamSegment(
        self,
        group_call_id: int,
        time_offset: int,
        scale: int,
        channel_id: int,
        video_quality: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video

        Args:
            group_call_id (``int``):
                Group call identifier

            time_offset (``int``):
                Point in time when the stream segment begins; Unix timestamp in milliseconds

            scale (``int``):
                Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds

            channel_id (``int``):
                Identifier of an audio/video channel to get as received from tgcalls

            video_quality (``dict``, optional):
                Video quality as received from tgcalls; pass null to get the worst available quality


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getGroupCallStreamSegment",
            "group_call_id": group_call_id,
            "time_offset": time_offset,
            "scale": scale,
            "channel_id": channel_id,
            "video_quality": video_quality,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleMessageSenderIsBlocked(
        self, sender_id: dict, is_blocked: bool, timeout: float = None
    ) -> Response:
        """Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked

        Args:
            sender_id (``dict``):
                Identifier of a message sender to block/unblock

            is_blocked (``bool``):
                New value of is_blocked


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleMessageSenderIsBlocked",
            "sender_id": sender_id,
            "is_blocked": is_blocked,
        }

        return await self.invoke(data, timeout=timeout)

    async def blockMessageSenderFromReplies(
        self,
        message_id: int,
        delete_message: bool,
        delete_all_messages: bool,
        report_spam: bool,
        timeout: float = None,
    ) -> Response:
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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "blockMessageSenderFromReplies",
            "message_id": message_id,
            "delete_message": delete_message,
            "delete_all_messages": delete_all_messages,
            "report_spam": report_spam,
        }

        return await self.invoke(data, timeout=timeout)

    async def getBlockedMessageSenders(
        self, offset: int, limit: int, timeout: float = None
    ) -> Response:
        """Returns users and chats that were blocked by the current user

        Args:
            offset (``int``):
                Number of users and chats to skip in the result; must be non-negative

            limit (``int``):
                The maximum number of users and chats to return; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBlockedMessageSenders",
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def addContact(
        self, contact: dict, share_phone_number: bool, timeout: float = None
    ) -> Response:
        """Adds a user to the contact list or edits an existing contact by their user identifier

        Args:
            contact (``dict``):
                The contact to add or edit; phone number may be empty and needs to be specified only if known, vCard is ignored

            share_phone_number (``bool``):
                Pass true to share the current user's phone number with the new contact. A corresponding rule to userPrivacySettingShowPhoneNumber will be added if needed. Use the field userFullInfo.need_phone_number_privacy_exception to check whether the current user needs to be asked to share their phone number


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addContact",
            "contact": contact,
            "share_phone_number": share_phone_number,
        }

        return await self.invoke(data, timeout=timeout)

    async def importContacts(self, contacts: list, timeout: float = None) -> Response:
        """Adds new contacts or edits existing contacts by their phone numbers; contacts' user identifiers are ignored

        Args:
            contacts (``list``):
                The list of contacts to import or edit; contacts' vCard are ignored and are not imported


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "importContacts",
            "contacts": contacts,
        }

        return await self.invoke(data, timeout=timeout)

    async def getContacts(self, timeout: float = None) -> Response:
        """Returns all user contacts


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getContacts",
        }

        return await self.invoke(data, timeout=timeout)

    async def searchContacts(
        self, limit: int, query: str = None, timeout: float = None
    ) -> Response:
        """Searches for the specified query in the first names, last names and usernames of the known user contacts

        Args:
            limit (``int``):
                The maximum number of users to be returned

            query (``str``, optional):
                Query to search for; may be empty to return all contacts


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchContacts",
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeContacts(self, user_ids: list, timeout: float = None) -> Response:
        """Removes users from the contact list

        Args:
            user_ids (``list``):
                Identifiers of users to be deleted


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeContacts",
            "user_ids": user_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getImportedContactCount(self, timeout: float = None) -> Response:
        """Returns the total number of imported contacts


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getImportedContactCount",
        }

        return await self.invoke(data, timeout=timeout)

    async def changeImportedContacts(
        self, contacts: list, timeout: float = None
    ) -> Response:
        """Changes imported contacts using the list of contacts saved on the device. Imports newly added contacts and, if at least the file database is enabled, deletes recently deleted contacts. Query result depends on the result of the previous query, so only one query is possible at the same time

        Args:
            contacts (``list``):
                The new list of contacts, contact's vCard are ignored and are not imported


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "changeImportedContacts",
            "contacts": contacts,
        }

        return await self.invoke(data, timeout=timeout)

    async def clearImportedContacts(self, timeout: float = None) -> Response:
        """Clears all imported contacts, contact list remains unchanged


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearImportedContacts",
        }

        return await self.invoke(data, timeout=timeout)

    async def searchUserByPhoneNumber(
        self, phone_number: str, timeout: float = None
    ) -> Response:
        """Searches a user by their phone number. Returns a 404 error if the user can't be found

        Args:
            phone_number (``str``):
                Phone number to search for


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchUserByPhoneNumber",
            "phone_number": phone_number,
        }

        return await self.invoke(data, timeout=timeout)

    async def sharePhoneNumber(self, user_id: int, timeout: float = None) -> Response:
        """Shares the phone number of the current user with a mutual contact. Supposed to be called when the user clicks on chatActionBarSharePhoneNumber

        Args:
            user_id (``int``):
                Identifier of the user with whom to share the phone number. The user must be a mutual contact


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sharePhoneNumber",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getUserProfilePhotos(
        self, user_id: int, offset: int, limit: int, timeout: float = None
    ) -> Response:
        """Returns the profile photos of a user. The result of this query may be outdated: some photos might have been deleted already

        Args:
            user_id (``int``):
                User identifier

            offset (``int``):
                The number of photos to skip; must be non-negative

            limit (``int``):
                The maximum number of photos to be returned; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getUserProfilePhotos",
            "user_id": user_id,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStickers(
        self,
        sticker_type: dict,
        query: str,
        limit: int,
        chat_id: int,
        timeout: float = None,
    ) -> Response:
        """Returns stickers from the installed sticker sets that correspond to a given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned

        Args:
            sticker_type (``dict``):
                Type of the stickers to return

            query (``str``):
                Search query; an emoji or a keyword prefix. If empty, returns all known installed stickers

            limit (``int``):
                The maximum number of stickers to be returned

            chat_id (``int``):
                Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStickers",
            "sticker_type": sticker_type,
            "query": query,
            "limit": limit,
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchStickers(
        self, emoji: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for stickers from public sticker sets that correspond to a given emoji

        Args:
            emoji (``str``):
                String representation of emoji; must be non-empty

            limit (``int``):
                The maximum number of stickers to be returned; 0-100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchStickers",
            "emoji": emoji,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPremiumStickers(self, limit: int, timeout: float = None) -> Response:
        """Returns premium stickers from regular sticker sets

        Args:
            limit (``int``):
                The maximum number of stickers to be returned; 0-100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPremiumStickers",
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getInstalledStickerSets(
        self, sticker_type: dict, timeout: float = None
    ) -> Response:
        """Returns a list of installed sticker sets

        Args:
            sticker_type (``dict``):
                Type of the sticker sets to return


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getInstalledStickerSets",
            "sticker_type": sticker_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getArchivedStickerSets(
        self,
        sticker_type: dict,
        offset_sticker_set_id: int,
        limit: int,
        timeout: float = None,
    ) -> Response:
        """Returns a list of archived sticker sets

        Args:
            sticker_type (``dict``):
                Type of the sticker sets to return

            offset_sticker_set_id (``int``):
                Identifier of the sticker set from which to return the result

            limit (``int``):
                The maximum number of sticker sets to return; up to 100


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getArchivedStickerSets",
            "sticker_type": sticker_type,
            "offset_sticker_set_id": offset_sticker_set_id,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getTrendingStickerSets(
        self, sticker_type: dict, offset: int, limit: int, timeout: float = None
    ) -> Response:
        """Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib

        Args:
            sticker_type (``dict``):
                Type of the sticker sets to return

            offset (``int``):
                The offset from which to return the sticker sets; must be non-negative

            limit (``int``):
                The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getTrendingStickerSets",
            "sticker_type": sticker_type,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getAttachedStickerSets(
        self, file_id: int, timeout: float = None
    ) -> Response:
        """Returns a list of sticker sets attached to a file. Currently, only photos and videos can have attached sticker sets

        Args:
            file_id (``int``):
                File identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAttachedStickerSets",
            "file_id": file_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStickerSet(self, set_id: int, timeout: float = None) -> Response:
        """Returns information about a sticker set by its identifier

        Args:
            set_id (``int``):
                Identifier of the sticker set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStickerSet",
            "set_id": set_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchStickerSet(self, name: str, timeout: float = None) -> Response:
        """Searches for a sticker set by its name

        Args:
            name (``str``):
                Name of the sticker set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchStickerSet",
            "name": name,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchInstalledStickerSets(
        self, sticker_type: dict, query: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for installed sticker sets by looking for specified query in their title and name

        Args:
            sticker_type (``dict``):
                Type of the sticker sets to search for

            query (``str``):
                Query to search for

            limit (``int``):
                The maximum number of sticker sets to return


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchInstalledStickerSets",
            "sticker_type": sticker_type,
            "query": query,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchStickerSets(self, query: str, timeout: float = None) -> Response:
        """Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results

        Args:
            query (``str``):
                Query to search for


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchStickerSets",
            "query": query,
        }

        return await self.invoke(data, timeout=timeout)

    async def changeStickerSet(
        self, set_id: int, is_installed: bool, is_archived: bool, timeout: float = None
    ) -> Response:
        """Installs/uninstalls or activates/archives a sticker set

        Args:
            set_id (``int``):
                Identifier of the sticker set

            is_installed (``bool``):
                The new value of is_installed

            is_archived (``bool``):
                The new value of is_archived. A sticker set can't be installed and archived simultaneously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "changeStickerSet",
            "set_id": set_id,
            "is_installed": is_installed,
            "is_archived": is_archived,
        }

        return await self.invoke(data, timeout=timeout)

    async def viewTrendingStickerSets(
        self, sticker_set_ids: list, timeout: float = None
    ) -> Response:
        """Informs the server that some trending sticker sets have been viewed by the user

        Args:
            sticker_set_ids (``list``):
                Identifiers of viewed trending sticker sets


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "viewTrendingStickerSets",
            "sticker_set_ids": sticker_set_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def reorderInstalledStickerSets(
        self, sticker_type: dict, sticker_set_ids: list, timeout: float = None
    ) -> Response:
        """Changes the order of installed sticker sets

        Args:
            sticker_type (``dict``):
                Type of the sticker sets to reorder

            sticker_set_ids (``list``):
                Identifiers of installed sticker sets in the new correct order


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reorderInstalledStickerSets",
            "sticker_type": sticker_type,
            "sticker_set_ids": sticker_set_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecentStickers(
        self, is_attached: bool, timeout: float = None
    ) -> Response:
        """Returns a list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to return stickers and masks that were recently attached to photos or video files; pass false to return recently sent stickers


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecentStickers",
            "is_attached": is_attached,
        }

        return await self.invoke(data, timeout=timeout)

    async def addRecentSticker(
        self, is_attached: bool, sticker: dict, timeout: float = None
    ) -> Response:
        """Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list. Emoji stickers can't be added to recent stickers

        Args:
            is_attached (``bool``):
                Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers

            sticker (``dict``):
                Sticker file to add


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addRecentSticker",
            "is_attached": is_attached,
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeRecentSticker(
        self, is_attached: bool, sticker: dict, timeout: float = None
    ) -> Response:
        """Removes a sticker from the list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers

            sticker (``dict``):
                Sticker file to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeRecentSticker",
            "is_attached": is_attached,
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def clearRecentStickers(
        self, is_attached: bool, timeout: float = None
    ) -> Response:
        """Clears the list of recently used stickers

        Args:
            is_attached (``bool``):
                Pass true to clear the list of stickers recently attached to photo or video files; pass false to clear the list of recently sent stickers


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clearRecentStickers",
            "is_attached": is_attached,
        }

        return await self.invoke(data, timeout=timeout)

    async def getFavoriteStickers(self, timeout: float = None) -> Response:
        """Returns favorite stickers


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getFavoriteStickers",
        }

        return await self.invoke(data, timeout=timeout)

    async def addFavoriteSticker(
        self, sticker: dict, timeout: float = None
    ) -> Response:
        """Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list. Emoji stickers can't be added to favorite stickers

        Args:
            sticker (``dict``):
                Sticker file to add


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addFavoriteSticker",
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeFavoriteSticker(
        self, sticker: dict, timeout: float = None
    ) -> Response:
        """Removes a sticker from the list of favorite stickers

        Args:
            sticker (``dict``):
                Sticker file to delete from the list


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeFavoriteSticker",
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStickerEmojis(self, sticker: dict, timeout: float = None) -> Response:
        """Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object

        Args:
            sticker (``dict``):
                Sticker file identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStickerEmojis",
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchEmojis(
        self,
        text: str,
        exact_match: bool,
        input_language_codes: list = None,
        timeout: float = None,
    ) -> Response:
        """Searches for emojis by keywords. Supported only if the file database is enabled

        Args:
            text (``str``):
                Text to search for

            exact_match (``bool``):
                Pass true if only emojis, which exactly match the text, needs to be returned

            input_language_codes (``list``, optional):
                List of possible IETF language tags of the user's input language; may be empty if unknown


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchEmojis",
            "text": text,
            "exact_match": exact_match,
            "input_language_codes": input_language_codes,
        }

        return await self.invoke(data, timeout=timeout)

    async def getAnimatedEmoji(self, emoji: str, timeout: float = None) -> Response:
        """Returns an animated emoji corresponding to a given emoji. Returns a 404 error if the emoji has no animated emoji

        Args:
            emoji (``str``):
                The emoji


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAnimatedEmoji",
            "emoji": emoji,
        }

        return await self.invoke(data, timeout=timeout)

    async def getEmojiSuggestionsUrl(
        self, language_code: str, timeout: float = None
    ) -> Response:
        """Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation

        Args:
            language_code (``str``):
                Language code for which the emoji replacements will be suggested


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getEmojiSuggestionsUrl",
            "language_code": language_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCustomEmojiStickers(
        self, custom_emoji_ids: list, timeout: float = None
    ) -> Response:
        """Returns list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned

        Args:
            custom_emoji_ids (``list``):
                Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCustomEmojiStickers",
            "custom_emoji_ids": custom_emoji_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSavedAnimations(self, timeout: float = None) -> Response:
        """Returns saved animations


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSavedAnimations",
        }

        return await self.invoke(data, timeout=timeout)

    async def addSavedAnimation(
        self, animation: dict, timeout: float = None
    ) -> Response:
        """Manually adds a new animation to the list of saved animations. The new animation is added to the beginning of the list. If the animation was already in the list, it is removed first. Only non-secret video animations with MIME type "video/mp4" can be added to the list

        Args:
            animation (``dict``):
                The animation file to be added. Only animations known to the server (i.e., successfully sent via a message) can be added to the list


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addSavedAnimation",
            "animation": animation,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeSavedAnimation(
        self, animation: dict, timeout: float = None
    ) -> Response:
        """Removes an animation from the list of saved animations

        Args:
            animation (``dict``):
                Animation file to be removed


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeSavedAnimation",
            "animation": animation,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecentInlineBots(self, timeout: float = None) -> Response:
        """Returns up to 20 recently used inline bots in the order of their last usage


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecentInlineBots",
        }

        return await self.invoke(data, timeout=timeout)

    async def searchHashtags(
        self, prefix: str, limit: int, timeout: float = None
    ) -> Response:
        """Searches for recently used hashtags by their prefix

        Args:
            prefix (``str``):
                Hashtag prefix to search for

            limit (``int``):
                The maximum number of hashtags to be returned


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchHashtags",
            "prefix": prefix,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeRecentHashtag(
        self, hashtag: str, timeout: float = None
    ) -> Response:
        """Removes a hashtag from the list of recently used hashtags

        Args:
            hashtag (``str``):
                Hashtag to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeRecentHashtag",
            "hashtag": hashtag,
        }

        return await self.invoke(data, timeout=timeout)

    async def getWebPagePreview(self, text: dict, timeout: float = None) -> Response:
        """Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview

        Args:
            text (``dict``):
                Message text with formatting


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getWebPagePreview",
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def getWebPageInstantView(
        self, url: str, force_full: bool, timeout: float = None
    ) -> Response:
        """Returns an instant view version of a web page if available. Returns a 404 error if the web page has no instant view page

        Args:
            url (``str``):
                The web page URL

            force_full (``bool``):
                Pass true to get full instant view for the web page


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getWebPageInstantView",
            "url": url,
            "force_full": force_full,
        }

        return await self.invoke(data, timeout=timeout)

    async def setProfilePhoto(self, photo: dict, timeout: float = None) -> Response:
        """Changes a profile photo for the current user

        Args:
            photo (``dict``):
                Profile photo to set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setProfilePhoto",
            "photo": photo,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteProfilePhoto(
        self, profile_photo_id: int, timeout: float = None
    ) -> Response:
        """Deletes a profile photo

        Args:
            profile_photo_id (``int``):
                Identifier of the profile photo to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteProfilePhoto",
            "profile_photo_id": profile_photo_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setName(
        self, first_name: str, last_name: str, timeout: float = None
    ) -> Response:
        """Changes the first and last name of the current user

        Args:
            first_name (``str``):
                The new value of the first name for the current user; 1-64 characters

            last_name (``str``):
                The new value of the optional last name for the current user; 0-64 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setName",
            "first_name": first_name,
            "last_name": last_name,
        }

        return await self.invoke(data, timeout=timeout)

    async def setBio(self, bio: str, timeout: float = None) -> Response:
        """Changes the bio of the current user

        Args:
            bio (``str``):
                The new value of the user bio; 0-GetOption("bio_length_max") characters without line feeds


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setBio",
            "bio": bio,
        }

        return await self.invoke(data, timeout=timeout)

    async def setUsername(self, username: str, timeout: float = None) -> Response:
        """Changes the username of the current user

        Args:
            username (``str``):
                The new value of the username. Use an empty string to remove the username


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setUsername",
            "username": username,
        }

        return await self.invoke(data, timeout=timeout)

    async def setEmojiStatus(
        self, duration: int, emoji_status: dict = None, timeout: float = None
    ) -> Response:
        """Changes the emoji status of the current user; for Telegram Premium users only

        Args:
            duration (``int``):
                Duration of the status, in seconds; pass 0 to keep the status active until it will be changed manually

            emoji_status (``dict``, optional):
                New emoji status; pass null to switch to the default badge


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setEmojiStatus",
            "emoji_status": emoji_status,
            "duration": duration,
        }

        return await self.invoke(data, timeout=timeout)

    async def setLocation(self, location: dict, timeout: float = None) -> Response:
        """Changes the location of the current user. Needs to be called if GetOption("is_location_visible") is true and location changes for more than 1 kilometer

        Args:
            location (``dict``):
                The new location of the user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setLocation",
            "location": location,
        }

        return await self.invoke(data, timeout=timeout)

    async def changePhoneNumber(
        self, phone_number: str, settings: dict = None, timeout: float = None
    ) -> Response:
        """Changes the phone number of the user and sends an authentication code to the user's new phone number. On success, returns information about the sent code

        Args:
            phone_number (``str``):
                The new phone number of the user in international format

            settings (``dict``, optional):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "changePhoneNumber",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendChangePhoneNumberCode(self, timeout: float = None) -> Response:
        """Resends the authentication code sent to confirm a new phone number for the current user. Works only if the previously received authenticationCodeInfo next_code_type was not null and the server-specified timeout has passed


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendChangePhoneNumberCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkChangePhoneNumberCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks the authentication code sent to confirm a new phone number of the user

        Args:
            code (``str``):
                Authentication code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkChangePhoneNumberCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def setCommands(
        self,
        language_code: str,
        commands: list,
        scope: dict = None,
        timeout: float = None,
    ) -> Response:
        """Sets the list of commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two-letter ISO 639-1 language code. If empty, the commands will be applied to all users from the given scope, for which language there are no dedicated commands

            commands (``list``):
                List of the bot's commands

            scope (``dict``, optional):
                The scope to which the commands are relevant; pass null to change commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setCommands",
            "scope": scope,
            "language_code": language_code,
            "commands": commands,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteCommands(
        self, language_code: str, scope: dict = None, timeout: float = None
    ) -> Response:
        """Deletes commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two-letter ISO 639-1 language code or an empty string

            scope (``dict``, optional):
                The scope to which the commands are relevant; pass null to delete commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteCommands",
            "scope": scope,
            "language_code": language_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCommands(
        self, language_code: str, scope: dict = None, timeout: float = None
    ) -> Response:
        """Returns the list of commands supported by the bot for the given user scope and language; for bots only

        Args:
            language_code (``str``):
                A two-letter ISO 639-1 language code or an empty string

            scope (``dict``, optional):
                The scope to which the commands are relevant; pass null to get commands in the default bot command scope


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCommands",
            "scope": scope,
            "language_code": language_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def setMenuButton(
        self, user_id: int, menu_button: dict, timeout: float = None
    ) -> Response:
        """Sets menu button for the given user or for all users; for bots only

        Args:
            user_id (``int``):
                Identifier of the user or 0 to set menu button for all users

            menu_button (``dict``):
                New menu button


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setMenuButton",
            "user_id": user_id,
            "menu_button": menu_button,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMenuButton(self, user_id: int, timeout: float = None) -> Response:
        """Returns menu button set by the bot for the given user; for bots only

        Args:
            user_id (``int``):
                Identifier of the user or 0 to get the default menu button


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMenuButton",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setDefaultGroupAdministratorRights(
        self, default_group_administrator_rights: dict = None, timeout: float = None
    ) -> Response:
        """Sets default administrator rights for adding the bot to basic group and supergroup chats; for bots only

        Args:
            default_group_administrator_rights (``dict``, optional):
                Default administrator rights for adding the bot to basic group and supergroup chats; may be null


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setDefaultGroupAdministratorRights",
            "default_group_administrator_rights": default_group_administrator_rights,
        }

        return await self.invoke(data, timeout=timeout)

    async def setDefaultChannelAdministratorRights(
        self, default_channel_administrator_rights: dict = None, timeout: float = None
    ) -> Response:
        """Sets default administrator rights for adding the bot to channel chats; for bots only

        Args:
            default_channel_administrator_rights (``dict``, optional):
                Default administrator rights for adding the bot to channels; may be null


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setDefaultChannelAdministratorRights",
            "default_channel_administrator_rights": default_channel_administrator_rights,
        }

        return await self.invoke(data, timeout=timeout)

    async def getActiveSessions(self, timeout: float = None) -> Response:
        """Returns all active sessions of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getActiveSessions",
        }

        return await self.invoke(data, timeout=timeout)

    async def terminateSession(
        self, session_id: int, timeout: float = None
    ) -> Response:
        """Terminates a session of the current user

        Args:
            session_id (``int``):
                Session identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "terminateSession",
            "session_id": session_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def terminateAllOtherSessions(self, timeout: float = None) -> Response:
        """Terminates all other sessions of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "terminateAllOtherSessions",
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSessionCanAcceptCalls(
        self, session_id: int, can_accept_calls: bool, timeout: float = None
    ) -> Response:
        """Toggles whether a session can accept incoming calls

        Args:
            session_id (``int``):
                Session identifier

            can_accept_calls (``bool``):
                Pass true to allow accepting incoming calls by the session; pass false otherwise


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSessionCanAcceptCalls",
            "session_id": session_id,
            "can_accept_calls": can_accept_calls,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSessionCanAcceptSecretChats(
        self, session_id: int, can_accept_secret_chats: bool, timeout: float = None
    ) -> Response:
        """Toggles whether a session can accept incoming secret chats

        Args:
            session_id (``int``):
                Session identifier

            can_accept_secret_chats (``bool``):
                Pass true to allow accepring secret chats by the session; pass false otherwise


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSessionCanAcceptSecretChats",
            "session_id": session_id,
            "can_accept_secret_chats": can_accept_secret_chats,
        }

        return await self.invoke(data, timeout=timeout)

    async def setInactiveSessionTtl(
        self, inactive_session_ttl_days: int, timeout: float = None
    ) -> Response:
        """Changes the period of inactivity after which sessions will automatically be terminated

        Args:
            inactive_session_ttl_days (``int``):
                New number of days of inactivity before sessions will be automatically terminated; 1-366 days


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setInactiveSessionTtl",
            "inactive_session_ttl_days": inactive_session_ttl_days,
        }

        return await self.invoke(data, timeout=timeout)

    async def getConnectedWebsites(self, timeout: float = None) -> Response:
        """Returns all website where the current user used Telegram to log in


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getConnectedWebsites",
        }

        return await self.invoke(data, timeout=timeout)

    async def disconnectWebsite(
        self, website_id: int, timeout: float = None
    ) -> Response:
        """Disconnects website from the current user's Telegram account

        Args:
            website_id (``int``):
                Website identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "disconnectWebsite",
            "website_id": website_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def disconnectAllWebsites(self, timeout: float = None) -> Response:
        """Disconnects all websites from the current user's Telegram account


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "disconnectAllWebsites",
        }

        return await self.invoke(data, timeout=timeout)

    async def setSupergroupUsername(
        self, supergroup_id: int, username: str, timeout: float = None
    ) -> Response:
        """Changes the username of a supergroup or channel, requires owner privileges in the supergroup or channel

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            username (``str``):
                New value of the username. Use an empty string to remove the username


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setSupergroupUsername",
            "supergroup_id": supergroup_id,
            "username": username,
        }

        return await self.invoke(data, timeout=timeout)

    async def setSupergroupStickerSet(
        self, supergroup_id: int, sticker_set_id: int, timeout: float = None
    ) -> Response:
        """Changes the sticker set of a supergroup; requires can_change_info administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            sticker_set_id (``int``):
                New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setSupergroupStickerSet",
            "supergroup_id": supergroup_id,
            "sticker_set_id": sticker_set_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSupergroupSignMessages(
        self, supergroup_id: int, sign_messages: bool, timeout: float = None
    ) -> Response:
        """Toggles whether sender signature is added to sent messages in a channel; requires can_change_info administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the channel

            sign_messages (``bool``):
                New value of sign_messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSupergroupSignMessages",
            "supergroup_id": supergroup_id,
            "sign_messages": sign_messages,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSupergroupJoinToSendMessages(
        self, supergroup_id: int, join_to_send_messages: bool, timeout: float = None
    ) -> Response:
        """Toggles whether joining is mandatory to send messages to a discussion supergroup; requires can_restrict_members administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup

            join_to_send_messages (``bool``):
                New value of join_to_send_messages


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSupergroupJoinToSendMessages",
            "supergroup_id": supergroup_id,
            "join_to_send_messages": join_to_send_messages,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSupergroupJoinByRequest(
        self, supergroup_id: int, join_by_request: bool, timeout: float = None
    ) -> Response:
        """Toggles whether all users directly joining the supergroup need to be approved by supergroup administrators; requires can_restrict_members administrator right

        Args:
            supergroup_id (``int``):
                Identifier of the channel

            join_by_request (``bool``):
                New value of join_by_request


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSupergroupJoinByRequest",
            "supergroup_id": supergroup_id,
            "join_by_request": join_by_request,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSupergroupIsAllHistoryAvailable(
        self, supergroup_id: int, is_all_history_available: bool, timeout: float = None
    ) -> Response:
        """Toggles whether the message history of a supergroup is available to new members; requires can_change_info administrator right

        Args:
            supergroup_id (``int``):
                The identifier of the supergroup

            is_all_history_available (``bool``):
                The new value of is_all_history_available


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSupergroupIsAllHistoryAvailable",
            "supergroup_id": supergroup_id,
            "is_all_history_available": is_all_history_available,
        }

        return await self.invoke(data, timeout=timeout)

    async def toggleSupergroupIsBroadcastGroup(
        self, supergroup_id: int, timeout: float = None
    ) -> Response:
        """Upgrades supergroup to a broadcast group; requires owner privileges in the supergroup

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "toggleSupergroupIsBroadcastGroup",
            "supergroup_id": supergroup_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def reportSupergroupSpam(
        self, supergroup_id: int, message_ids: list, timeout: float = None
    ) -> Response:
        """Reports messages in a supergroup as spam; requires administrator rights in the supergroup

        Args:
            supergroup_id (``int``):
                Supergroup identifier

            message_ids (``list``):
                Identifiers of messages to report


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reportSupergroupSpam",
            "supergroup_id": supergroup_id,
            "message_ids": message_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSupergroupMembers(
        self,
        supergroup_id: int,
        offset: int,
        limit: int,
        filter: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns information about members or banned users in a supergroup or channel. Can be used only if supergroupFullInfo.can_get_members == true; additionally, administrator privileges may be required for some filters

        Args:
            supergroup_id (``int``):
                Identifier of the supergroup or channel

            offset (``int``):
                Number of users to skip

            limit (``int``):
                The maximum number of users be returned; up to 200

            filter (``dict``, optional):
                The type of users to return; pass null to use supergroupMembersFilterRecent


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSupergroupMembers",
            "supergroup_id": supergroup_id,
            "filter": filter,
            "offset": offset,
            "limit": limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def closeSecretChat(
        self, secret_chat_id: int, timeout: float = None
    ) -> Response:
        """Closes a secret chat, effectively transferring its state to secretChatStateClosed

        Args:
            secret_chat_id (``int``):
                Secret chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "closeSecretChat",
            "secret_chat_id": secret_chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatEventLog(
        self,
        chat_id: int,
        query: str,
        from_event_id: int,
        limit: int,
        user_ids: list,
        filters: dict = None,
        timeout: float = None,
    ) -> Response:
        """Returns a list of service actions taken by chat members and administrators in the last 48 hours. Available only for supergroups and channels. Requires administrator rights. Returns results in reverse chronological order (i.e., in order of decreasing event_id)

        Args:
            chat_id (``int``):
                Chat identifier

            query (``str``):
                Search query by which to filter events

            from_event_id (``int``):
                Identifier of an event from which to return results. Use 0 to get results from the latest events

            limit (``int``):
                The maximum number of events to return; up to 100

            user_ids (``list``):
                User identifiers by which to filter events. By default, events relating to all users will be returned

            filters (``dict``, optional):
                The types of events to return; pass null to get chat events of all types


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def getPaymentForm(
        self, input_invoice: dict, theme: dict = None, timeout: float = None
    ) -> Response:
        """Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy

        Args:
            input_invoice (``dict``):
                The invoice

            theme (``dict``, optional):
                Preferred payment form theme; pass null to use the default theme


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPaymentForm",
            "input_invoice": input_invoice,
            "theme": theme,
        }

        return await self.invoke(data, timeout=timeout)

    async def validateOrderInfo(
        self,
        input_invoice: dict,
        allow_save: bool,
        order_info: dict = None,
        timeout: float = None,
    ) -> Response:
        """Validates the order information provided by a user and returns the available shipping options for a flexible invoice

        Args:
            input_invoice (``dict``):
                The invoice

            allow_save (``bool``):
                Pass true to save the order information

            order_info (``dict``, optional):
                The order information, provided by the user; pass null if empty


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "validateOrderInfo",
            "input_invoice": input_invoice,
            "order_info": order_info,
            "allow_save": allow_save,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendPaymentForm(
        self,
        input_invoice: dict,
        payment_form_id: int,
        order_info_id: str,
        shipping_option_id: str,
        credentials: dict,
        tip_amount: int,
        timeout: float = None,
    ) -> Response:
        """Sends a filled-out payment form to the bot for final verification

        Args:
            input_invoice (``dict``):
                The invoice

            payment_form_id (``int``):
                Payment form identifier returned by getPaymentForm

            order_info_id (``str``):
                Identifier returned by validateOrderInfo, or an empty string

            shipping_option_id (``str``):
                Identifier of a chosen shipping option, if applicable

            credentials (``dict``):
                The credentials chosen by user for payment

            tip_amount (``int``):
                Chosen by the user amount of tip in the smallest units of the currency


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def getPaymentReceipt(
        self, chat_id: int, message_id: int, timeout: float = None
    ) -> Response:
        """Returns information about a successful payment

        Args:
            chat_id (``int``):
                Chat identifier of the PaymentSuccessful message

            message_id (``int``):
                Message identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPaymentReceipt",
            "chat_id": chat_id,
            "message_id": message_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSavedOrderInfo(self, timeout: float = None) -> Response:
        """Returns saved order information. Returns a 404 error if there is no saved order information


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSavedOrderInfo",
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteSavedOrderInfo(self, timeout: float = None) -> Response:
        """Deletes saved order information


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteSavedOrderInfo",
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteSavedCredentials(self, timeout: float = None) -> Response:
        """Deletes saved credentials for all payment provider bots


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteSavedCredentials",
        }

        return await self.invoke(data, timeout=timeout)

    async def createInvoiceLink(self, invoice: dict, timeout: float = None) -> Response:
        """Creates a link for the given invoice; for bots only

        Args:
            invoice (``dict``):
                Information about the invoice of the type inputMessageInvoice


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createInvoiceLink",
            "invoice": invoice,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSupportUser(self, timeout: float = None) -> Response:
        """Returns a user that can be contacted to get support


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSupportUser",
        }

        return await self.invoke(data, timeout=timeout)

    async def getBackgrounds(
        self, for_dark_theme: bool, timeout: float = None
    ) -> Response:
        """Returns backgrounds installed by the user

        Args:
            for_dark_theme (``bool``):
                Pass true to order returned backgrounds for a dark theme


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBackgrounds",
            "for_dark_theme": for_dark_theme,
        }

        return await self.invoke(data, timeout=timeout)

    async def getBackgroundUrl(
        self, name: str, type: dict, timeout: float = None
    ) -> Response:
        """Constructs a persistent HTTP URL for a background

        Args:
            name (``str``):
                Background name

            type (``dict``):
                Background type


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBackgroundUrl",
            "name": name,
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def searchBackground(self, name: str, timeout: float = None) -> Response:
        """Searches for a background by its name

        Args:
            name (``str``):
                The name of the background


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "searchBackground",
            "name": name,
        }

        return await self.invoke(data, timeout=timeout)

    async def setBackground(
        self,
        for_dark_theme: bool,
        background: dict = None,
        type: dict = None,
        timeout: float = None,
    ) -> Response:
        """Changes the background selected by the user; adds background to the list of installed backgrounds

        Args:
            for_dark_theme (``bool``):
                Pass true if the background is changed for a dark theme

            background (``dict``, optional):
                The input background to use; pass null to create a new filled backgrounds or to remove the current background

            type (``dict``, optional):
                Background type; pass null to use the default type of the remote background or to remove the current background


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setBackground",
            "background": background,
            "type": type,
            "for_dark_theme": for_dark_theme,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeBackground(
        self, background_id: int, timeout: float = None
    ) -> Response:
        """Removes background from the list of installed backgrounds

        Args:
            background_id (``int``):
                The background identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeBackground",
            "background_id": background_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def resetBackgrounds(self, timeout: float = None) -> Response:
        """Resets list of installed backgrounds to its default value


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resetBackgrounds",
        }

        return await self.invoke(data, timeout=timeout)

    async def getLocalizationTargetInfo(
        self, only_local: bool, timeout: float = None
    ) -> Response:
        """Returns information about the current localization target. This is an offline request if only_local is true. Can be called before authorization

        Args:
            only_local (``bool``):
                Pass true to get only locally available information without sending network requests


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLocalizationTargetInfo",
            "only_local": only_local,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLanguagePackInfo(
        self, language_pack_id: str, timeout: float = None
    ) -> Response:
        """Returns information about a language pack. Returned language pack identifier may be different from a provided one. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLanguagePackInfo",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLanguagePackStrings(
        self, language_pack_id: str, keys: list, timeout: float = None
    ) -> Response:
        """Returns strings from a language pack in the current localization target by their keys. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier of the strings to be returned

            keys (``list``):
                Language pack keys of the strings to be returned; leave empty to request all available strings


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLanguagePackStrings",
            "language_pack_id": language_pack_id,
            "keys": keys,
        }

        return await self.invoke(data, timeout=timeout)

    async def synchronizeLanguagePack(
        self, language_pack_id: str, timeout: float = None
    ) -> Response:
        """Fetches the latest versions of all strings from a language pack in the current localization target from the server. This method doesn't need to be called explicitly for the current used/base language packs. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Language pack identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "synchronizeLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def addCustomServerLanguagePack(
        self, language_pack_id: str, timeout: float = None
    ) -> Response:
        """Adds a custom server language pack to the list of installed language packs in current localization target. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of a language pack to be added; may be different from a name that is used in an "https://t.me/setlanguage/" link


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addCustomServerLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setCustomLanguagePack(
        self, info: dict, strings: list, timeout: float = None
    ) -> Response:
        """Adds or changes a custom local language pack to the current localization target

        Args:
            info (``dict``):
                Information about the language pack. Language pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization

            strings (``list``):
                Strings of the new language pack


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setCustomLanguagePack",
            "info": info,
            "strings": strings,
        }

        return await self.invoke(data, timeout=timeout)

    async def editCustomLanguagePackInfo(
        self, info: dict, timeout: float = None
    ) -> Response:
        """Edits information about a custom local language pack in the current localization target. Can be called before authorization

        Args:
            info (``dict``):
                New information about the custom local language pack


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editCustomLanguagePackInfo",
            "info": info,
        }

        return await self.invoke(data, timeout=timeout)

    async def setCustomLanguagePackString(
        self, language_pack_id: str, new_string: dict, timeout: float = None
    ) -> Response:
        """Adds, edits or deletes a string in a custom local language pack. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of a previously added custom local language pack in the current localization target

            new_string (``dict``):
                New language pack string


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setCustomLanguagePackString",
            "language_pack_id": language_pack_id,
            "new_string": new_string,
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteLanguagePack(
        self, language_pack_id: str, timeout: float = None
    ) -> Response:
        """Deletes all information about a language pack in the current localization target. The language pack which is currently in use (including base language pack) or is being synchronized can't be deleted. Can be called before authorization

        Args:
            language_pack_id (``str``):
                Identifier of the language pack to delete


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteLanguagePack",
            "language_pack_id": language_pack_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def registerDevice(
        self, device_token: dict, other_user_ids: list, timeout: float = None
    ) -> Response:
        """Registers the currently used device for receiving push notifications. Returns a globally unique identifier of the push notification subscription

        Args:
            device_token (``dict``):
                Device token

            other_user_ids (``list``):
                List of user identifiers of other users currently using the application


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "registerDevice",
            "device_token": device_token,
            "other_user_ids": other_user_ids,
        }

        return await self.invoke(data, timeout=timeout)

    async def processPushNotification(
        self, payload: str, timeout: float = None
    ) -> Response:
        """Handles a push notification. Returns error with code 406 if the push notification is not supported and connection to the server is required to fetch new data. Can be called before authorization

        Args:
            payload (``str``):
                JSON-encoded push notification payload with all fields sent by the server, and "google.sent_time" and "google.notification.sound" fields added


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "processPushNotification",
            "payload": payload,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPushReceiverId(self, payload: str, timeout: float = None) -> Response:
        """Returns a globally unique push notification subscription identifier for identification of an account, which has received a push notification. Can be called synchronously

        Args:
            payload (``str``):
                JSON-encoded push notification payload


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPushReceiverId",
            "payload": payload,
        }

        return await self.invoke(data, timeout=timeout)

    async def getRecentlyVisitedTMeUrls(
        self, referrer: str, timeout: float = None
    ) -> Response:
        """Returns t.me URLs recently visited by a newly registered user

        Args:
            referrer (``str``):
                Google Play referrer to identify the user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getRecentlyVisitedTMeUrls",
            "referrer": referrer,
        }

        return await self.invoke(data, timeout=timeout)

    async def setUserPrivacySettingRules(
        self, setting: dict, rules: dict, timeout: float = None
    ) -> Response:
        """Changes user privacy settings

        Args:
            setting (``dict``):
                The privacy setting

            rules (``dict``):
                The new privacy rules


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setUserPrivacySettingRules",
            "setting": setting,
            "rules": rules,
        }

        return await self.invoke(data, timeout=timeout)

    async def getUserPrivacySettingRules(
        self, setting: dict, timeout: float = None
    ) -> Response:
        """Returns the current privacy settings

        Args:
            setting (``dict``):
                The privacy setting


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getUserPrivacySettingRules",
            "setting": setting,
        }

        return await self.invoke(data, timeout=timeout)

    async def getOption(self, name: str, timeout: float = None) -> Response:
        """Returns the value of an option by its name. (Check the list of available options on https://core.telegram.org/tdlib/options.) Can be called before authorization. Can be called synchronously for options "version" and "commit_hash"

        Args:
            name (``str``):
                The name of the option


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getOption",
            "name": name,
        }

        return await self.invoke(data, timeout=timeout)

    async def setOption(
        self, name: str, value: dict = None, timeout: float = None
    ) -> Response:
        """Sets the value of an option. (Check the list of available options on https://core.telegram.org/tdlib/options.) Only writable options can be set. Can be called before authorization

        Args:
            name (``str``):
                The name of the option

            value (``dict``, optional):
                The new value of the option; pass null to reset option value to a default value


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setOption",
            "name": name,
            "value": value,
        }

        return await self.invoke(data, timeout=timeout)

    async def setAccountTtl(self, ttl: dict, timeout: float = None) -> Response:
        """Changes the period of inactivity after which the account of the current user will automatically be deleted

        Args:
            ttl (``dict``):
                New account TTL


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setAccountTtl",
            "ttl": ttl,
        }

        return await self.invoke(data, timeout=timeout)

    async def getAccountTtl(self, timeout: float = None) -> Response:
        """Returns the period of inactivity after which the account of the current user will automatically be deleted


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAccountTtl",
        }

        return await self.invoke(data, timeout=timeout)

    async def deleteAccount(
        self, reason: str, password: str, timeout: float = None
    ) -> Response:
        """Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword

        Args:
            reason (``str``):
                The reason why the account was deleted; optional

            password (``str``):
                The 2-step verification password of the current user. If not specified, account deletion can be canceled within one week


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deleteAccount",
            "reason": reason,
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeChatActionBar(
        self, chat_id: int, timeout: float = None
    ) -> Response:
        """Removes a chat action bar without any other action

        Args:
            chat_id (``int``):
                Chat identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeChatActionBar",
            "chat_id": chat_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def reportChat(
        self,
        chat_id: int,
        reason: dict,
        text: str,
        message_ids: list = None,
        timeout: float = None,
    ) -> Response:
        """Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported

        Args:
            chat_id (``int``):
                Chat identifier

            reason (``dict``):
                The reason for reporting the chat

            text (``str``):
                Additional report details; 0-1024 characters

            message_ids (``list``, optional):
                Identifiers of reported messages; may be empty to report the whole chat


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reportChat",
            "chat_id": chat_id,
            "message_ids": message_ids,
            "reason": reason,
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def reportChatPhoto(
        self, chat_id: int, file_id: int, reason: dict, text: str, timeout: float = None
    ) -> Response:
        """Reports a chat photo to the Telegram moderators. A chat photo can be reported only if chat.can_be_reported

        Args:
            chat_id (``int``):
                Chat identifier

            file_id (``int``):
                Identifier of the photo to report. Only full photos from chatPhoto can be reported

            reason (``dict``):
                The reason for reporting the chat photo

            text (``str``):
                Additional report details; 0-1024 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reportChatPhoto",
            "chat_id": chat_id,
            "file_id": file_id,
            "reason": reason,
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def reportMessageReactions(
        self, chat_id: int, message_id: int, sender_id: dict, timeout: float = None
    ) -> Response:
        """Reports reactions set on a message to the Telegram moderators. Reactions on a message can be reported only if message.can_report_reactions

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier

            sender_id (``dict``):
                Identifier of the sender, which added the reaction


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "reportMessageReactions",
            "chat_id": chat_id,
            "message_id": message_id,
            "sender_id": sender_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getChatStatistics(
        self, chat_id: int, is_dark: bool, timeout: float = None
    ) -> Response:
        """Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true

        Args:
            chat_id (``int``):
                Chat identifier

            is_dark (``bool``):
                Pass true if a dark theme is used by the application


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getChatStatistics",
            "chat_id": chat_id,
            "is_dark": is_dark,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMessageStatistics(
        self, chat_id: int, message_id: int, is_dark: bool, timeout: float = None
    ) -> Response:
        """Returns detailed statistics about a message. Can be used only if message.can_get_statistics == true

        Args:
            chat_id (``int``):
                Chat identifier

            message_id (``int``):
                Message identifier

            is_dark (``bool``):
                Pass true if a dark theme is used by the application


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getMessageStatistics",
            "chat_id": chat_id,
            "message_id": message_id,
            "is_dark": is_dark,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStatisticalGraph(
        self, chat_id: int, token: str, x: int, timeout: float = None
    ) -> Response:
        """Loads an asynchronous or a zoomed in statistical graph

        Args:
            chat_id (``int``):
                Chat identifier

            token (``str``):
                The token for graph loading

            x (``int``):
                X-value for zoomed in graph or 0 otherwise


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStatisticalGraph",
            "chat_id": chat_id,
            "token": token,
            "x": x,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStorageStatistics(
        self, chat_limit: int, timeout: float = None
    ) -> Response:
        """Returns storage usage statistics. Can be called before authorization

        Args:
            chat_limit (``int``):
                The maximum number of chats with the largest storage usage for which separate statistics need to be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStorageStatistics",
            "chat_limit": chat_limit,
        }

        return await self.invoke(data, timeout=timeout)

    async def getStorageStatisticsFast(self, timeout: float = None) -> Response:
        """Quickly returns approximate storage usage statistics. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getStorageStatisticsFast",
        }

        return await self.invoke(data, timeout=timeout)

    async def getDatabaseStatistics(self, timeout: float = None) -> Response:
        """Returns database statistics


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getDatabaseStatistics",
        }

        return await self.invoke(data, timeout=timeout)

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
        timeout: float = None,
    ) -> Response:
        """Optimizes storage usage, i.e. deletes some files and returns new storage usage statistics. Secret thumbnails can't be deleted

        Args:
            size (``int``):
                Limit on the total size of files after deletion, in bytes. Pass -1 to use the default limit

            ttl (``int``):
                Limit on the time that has passed since the last time a file was accessed (or creation time for some filesystems). Pass -1 to use the default limit

            count (``int``):
                Limit on the total number of files after deletion. Pass -1 to use the default limit

            immunity_delay (``int``):
                The amount of time after the creation of a file during which it can't be deleted, in seconds. Pass -1 to use the default value

            return_deleted_file_statistics (``bool``):
                Pass true if statistics about the files that were deleted must be returned instead of the whole storage usage statistics. Affects only returned statistics

            chat_limit (``int``):
                Same as in getStorageStatistics. Affects only returned statistics

            file_types (``list``, optional):
                If non-empty, only files with the given types are considered. By default, all types except thumbnails, profile photos, stickers and wallpapers are deleted

            chat_ids (``list``, optional):
                If non-empty, only files from the given chats are considered. Use 0 as chat identifier to delete files not belonging to any chat (e.g., profile photos)

            exclude_chat_ids (``list``, optional):
                If non-empty, files from the given chats are excluded. Use 0 as chat identifier to exclude all files not belonging to any chat (e.g., profile photos)


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def setNetworkType(
        self, type: dict = None, timeout: float = None
    ) -> Response:
        """Sets the current network type. Can be called before authorization. Calling this method forces all network connections to reopen, mitigating the delay in switching between different networks, so it must be called whenever the network is changed, even if the network type remains the same. Network type is used to check whether the library can use the network at all and also for collecting detailed network data usage statistics

        Args:
            type (``dict``, optional):
                The new network type; pass null to set network type to networkTypeOther


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setNetworkType",
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getNetworkStatistics(
        self, only_current: bool, timeout: float = None
    ) -> Response:
        """Returns network data usage statistics. Can be called before authorization

        Args:
            only_current (``bool``):
                Pass true to get statistics only for the current library launch


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getNetworkStatistics",
            "only_current": only_current,
        }

        return await self.invoke(data, timeout=timeout)

    async def addNetworkStatistics(
        self, entry: dict, timeout: float = None
    ) -> Response:
        """Adds the specified data to data usage statistics. Can be called before authorization

        Args:
            entry (``dict``):
                The network statistics entry with the data to be added to statistics


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addNetworkStatistics",
            "entry": entry,
        }

        return await self.invoke(data, timeout=timeout)

    async def resetNetworkStatistics(self, timeout: float = None) -> Response:
        """Resets all network data usage statistics to zero. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resetNetworkStatistics",
        }

        return await self.invoke(data, timeout=timeout)

    async def getAutoDownloadSettingsPresets(self, timeout: float = None) -> Response:
        """Returns auto-download settings presets for the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAutoDownloadSettingsPresets",
        }

        return await self.invoke(data, timeout=timeout)

    async def setAutoDownloadSettings(
        self, settings: dict, type: dict, timeout: float = None
    ) -> Response:
        """Sets auto-download settings

        Args:
            settings (``dict``):
                New user auto-download settings

            type (``dict``):
                Type of the network for which the new settings are relevant


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setAutoDownloadSettings",
            "settings": settings,
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getBankCardInfo(
        self, bank_card_number: str, timeout: float = None
    ) -> Response:
        """Returns information about a bank card

        Args:
            bank_card_number (``str``):
                The bank card number


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getBankCardInfo",
            "bank_card_number": bank_card_number,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPassportElement(
        self, type: dict, password: str, timeout: float = None
    ) -> Response:
        """Returns one of the available Telegram Passport elements

        Args:
            type (``dict``):
                Telegram Passport element type

            password (``str``):
                The 2-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPassportElement",
            "type": type,
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def getAllPassportElements(
        self, password: str, timeout: float = None
    ) -> Response:
        """Returns all available Telegram Passport elements

        Args:
            password (``str``):
                The 2-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getAllPassportElements",
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def setPassportElement(
        self, element: dict, password: str, timeout: float = None
    ) -> Response:
        """Adds an element to the user's Telegram Passport. May return an error with a message "PHONE_VERIFICATION_NEEDED" or "EMAIL_VERIFICATION_NEEDED" if the chosen phone number or the chosen email address must be verified first

        Args:
            element (``dict``):
                Input Telegram Passport element

            password (``str``):
                The 2-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setPassportElement",
            "element": element,
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def deletePassportElement(
        self, type: dict, timeout: float = None
    ) -> Response:
        """Deletes a Telegram Passport element

        Args:
            type (``dict``):
                Element type


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "deletePassportElement",
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def setPassportElementErrors(
        self, user_id: int, errors: list, timeout: float = None
    ) -> Response:
        """Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed

        Args:
            user_id (``int``):
                User identifier

            errors (``list``):
                The errors


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setPassportElementErrors",
            "user_id": user_id,
            "errors": errors,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPreferredCountryLanguage(
        self, country_code: str, timeout: float = None
    ) -> Response:
        """Returns an IETF language tag of the language preferred in the country, which must be used to fill native fields in Telegram Passport personal details. Returns a 404 error if unknown

        Args:
            country_code (``str``):
                A two-letter ISO 3166-1 alpha-2 country code


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPreferredCountryLanguage",
            "country_code": country_code,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendPhoneNumberVerificationCode(
        self, phone_number: str, settings: dict = None, timeout: float = None
    ) -> Response:
        """Sends a code to verify a phone number to be added to a user's Telegram Passport

        Args:
            phone_number (``str``):
                The phone number of the user, in international format

            settings (``dict``, optional):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendPhoneNumberVerificationCode",
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendPhoneNumberVerificationCode(
        self, timeout: float = None
    ) -> Response:
        """Resends the code to verify a phone number to be added to a user's Telegram Passport


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendPhoneNumberVerificationCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkPhoneNumberVerificationCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks the phone number verification code for Telegram Passport

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkPhoneNumberVerificationCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendEmailAddressVerificationCode(
        self, email_address: str, timeout: float = None
    ) -> Response:
        """Sends a code to verify an email address to be added to a user's Telegram Passport

        Args:
            email_address (``str``):
                Email address


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendEmailAddressVerificationCode",
            "email_address": email_address,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendEmailAddressVerificationCode(
        self, timeout: float = None
    ) -> Response:
        """Resends the code to verify an email address to be added to a user's Telegram Passport


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendEmailAddressVerificationCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkEmailAddressVerificationCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks the email address verification code for Telegram Passport

        Args:
            code (``str``):
                Verification code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkEmailAddressVerificationCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPassportAuthorizationForm(
        self,
        bot_user_id: int,
        scope: str,
        public_key: str,
        nonce: str,
        timeout: float = None,
    ) -> Response:
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
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPassportAuthorizationForm",
            "bot_user_id": bot_user_id,
            "scope": scope,
            "public_key": public_key,
            "nonce": nonce,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPassportAuthorizationFormAvailableElements(
        self, autorization_form_id: int, password: str, timeout: float = None
    ) -> Response:
        """Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form

        Args:
            autorization_form_id (``int``):
                Authorization form identifier

            password (``str``):
                The 2-step verification password of the current user


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPassportAuthorizationFormAvailableElements",
            "autorization_form_id": autorization_form_id,
            "password": password,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendPassportAuthorizationForm(
        self, autorization_form_id: int, types: list, timeout: float = None
    ) -> Response:
        """Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements are going to be reused

        Args:
            autorization_form_id (``int``):
                Authorization form identifier

            types (``list``):
                Types of Telegram Passport elements chosen by user to complete the authorization form


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendPassportAuthorizationForm",
            "autorization_form_id": autorization_form_id,
            "types": types,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendPhoneNumberConfirmationCode(
        self, hash: str, phone_number: str, settings: dict = None, timeout: float = None
    ) -> Response:
        """Sends phone number confirmation code to handle links of the type internalLinkTypePhoneNumberConfirmation

        Args:
            hash (``str``):
                Hash value from the link

            phone_number (``str``):
                Phone number value from the link

            settings (``dict``, optional):
                Settings for the authentication of the user's phone number; pass null to use default settings


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendPhoneNumberConfirmationCode",
            "hash": hash,
            "phone_number": phone_number,
            "settings": settings,
        }

        return await self.invoke(data, timeout=timeout)

    async def resendPhoneNumberConfirmationCode(
        self, timeout: float = None
    ) -> Response:
        """Resends phone number confirmation code


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "resendPhoneNumberConfirmationCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def checkPhoneNumberConfirmationCode(
        self, code: str, timeout: float = None
    ) -> Response:
        """Checks phone number confirmation code

        Args:
            code (``str``):
                Confirmation code to check


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkPhoneNumberConfirmationCode",
            "code": code,
        }

        return await self.invoke(data, timeout=timeout)

    async def setBotUpdatesStatus(
        self, pending_update_count: int, error_message: str, timeout: float = None
    ) -> Response:
        """Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only

        Args:
            pending_update_count (``int``):
                The number of pending updates

            error_message (``str``):
                The last error message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setBotUpdatesStatus",
            "pending_update_count": pending_update_count,
            "error_message": error_message,
        }

        return await self.invoke(data, timeout=timeout)

    async def uploadStickerFile(
        self, user_id: int, sticker: dict, timeout: float = None
    ) -> Response:
        """Uploads a file with a sticker; returns the uploaded file

        Args:
            user_id (``int``):
                Sticker file owner; ignored for regular users

            sticker (``dict``):
                Sticker file to upload


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "uploadStickerFile",
            "user_id": user_id,
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def getSuggestedStickerSetName(
        self, title: str, timeout: float = None
    ) -> Response:
        """Returns a suggested name for a new sticker set with a given title

        Args:
            title (``str``):
                Sticker set title; 1-64 characters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getSuggestedStickerSetName",
            "title": title,
        }

        return await self.invoke(data, timeout=timeout)

    async def checkStickerSetName(self, name: str, timeout: float = None) -> Response:
        """Checks whether a name can be used for a new sticker set

        Args:
            name (``str``):
                Name to be checked


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "checkStickerSetName",
            "name": name,
        }

        return await self.invoke(data, timeout=timeout)

    async def createNewStickerSet(
        self,
        user_id: int,
        title: str,
        name: str,
        sticker_type: dict,
        stickers: list,
        source: str = None,
        timeout: float = None,
    ) -> Response:
        """Creates a new sticker set. Returns the newly created sticker set

        Args:
            user_id (``int``):
                Sticker set owner; ignored for regular users

            title (``str``):
                Sticker set title; 1-64 characters

            name (``str``):
                Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive) for bots; 1-64 characters

            sticker_type (``dict``):
                Type of the stickers in the set

            stickers (``list``):
                List of stickers to be added to the set; must be non-empty. All stickers must have the same format. For TGS stickers, uploadStickerFile must be used before the sticker is shown

            source (``str``, optional):
                Source of the sticker set; may be empty if unknown


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "createNewStickerSet",
            "user_id": user_id,
            "title": title,
            "name": name,
            "sticker_type": sticker_type,
            "stickers": stickers,
            "source": source,
        }

        return await self.invoke(data, timeout=timeout)

    async def addStickerToSet(
        self, user_id: int, name: str, sticker: dict, timeout: float = None
    ) -> Response:
        """Adds a new sticker to a set; for bots only. Returns the sticker set

        Args:
            user_id (``int``):
                Sticker set owner

            name (``str``):
                Sticker set name

            sticker (``dict``):
                Sticker to add to the set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addStickerToSet",
            "user_id": user_id,
            "name": name,
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def setStickerSetThumbnail(
        self, user_id: int, name: str, thumbnail: dict = None, timeout: float = None
    ) -> Response:
        """Sets a sticker set thumbnail; for bots only. Returns the sticker set

        Args:
            user_id (``int``):
                Sticker set owner

            name (``str``):
                Sticker set name

            thumbnail (``dict``, optional):
                Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail. Thumbnail format must match the format of stickers in the set


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setStickerSetThumbnail",
            "user_id": user_id,
            "name": name,
            "thumbnail": thumbnail,
        }

        return await self.invoke(data, timeout=timeout)

    async def setStickerPositionInSet(
        self, sticker: dict, position: int, timeout: float = None
    ) -> Response:
        """Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot

        Args:
            sticker (``dict``):
                Sticker

            position (``int``):
                New position of the sticker in the set, 0-based


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setStickerPositionInSet",
            "sticker": sticker,
            "position": position,
        }

        return await self.invoke(data, timeout=timeout)

    async def removeStickerFromSet(
        self, sticker: dict, timeout: float = None
    ) -> Response:
        """Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot

        Args:
            sticker (``dict``):
                Sticker


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeStickerFromSet",
            "sticker": sticker,
        }

        return await self.invoke(data, timeout=timeout)

    async def getMapThumbnailFile(
        self,
        location: dict,
        zoom: int,
        width: int,
        height: int,
        scale: int,
        chat_id: int,
        timeout: float = None,
    ) -> Response:
        """Returns information about a file with a map thumbnail in PNG format. Only map thumbnail files with size less than 1MB can be downloaded

        Args:
            location (``dict``):
                Location of the map center

            zoom (``int``):
                Map zoom level; 13-20

            width (``int``):
                Map width in pixels before applying scale; 16-1024

            height (``int``):
                Map height in pixels before applying scale; 16-1024

            scale (``int``):
                Map scale; 1-3

            chat_id (``int``):
                Identifier of a chat in which the thumbnail will be shown. Use 0 if unknown


        Returns:
            :class:`~pytdbot.types.Response`
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

        return await self.invoke(data, timeout=timeout)

    async def getPremiumLimit(
        self, limit_type: dict, timeout: float = None
    ) -> Response:
        """Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown

        Args:
            limit_type (``dict``):
                Type of the limit


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPremiumLimit",
            "limit_type": limit_type,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPremiumFeatures(
        self, source: dict = None, timeout: float = None
    ) -> Response:
        """Returns information about features, available to Premium users

        Args:
            source (``dict``, optional):
                Source of the request; pass null if the method is called from some non-standard source


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPremiumFeatures",
            "source": source,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPremiumStickerExamples(self, timeout: float = None) -> Response:
        """Returns examples of premium stickers for demonstration purposes


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPremiumStickerExamples",
        }

        return await self.invoke(data, timeout=timeout)

    async def viewPremiumFeature(
        self, feature: dict, timeout: float = None
    ) -> Response:
        """Informs TDLib that the user viewed detailed information about a Premium feature on the Premium features screen

        Args:
            feature (``dict``):
                The viewed premium feature


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "viewPremiumFeature",
            "feature": feature,
        }

        return await self.invoke(data, timeout=timeout)

    async def clickPremiumSubscriptionButton(self, timeout: float = None) -> Response:
        """Informs TDLib that the user clicked Premium subscription button on the Premium features screen


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "clickPremiumSubscriptionButton",
        }

        return await self.invoke(data, timeout=timeout)

    async def getPremiumState(self, timeout: float = None) -> Response:
        """Returns state of Telegram Premium subscription and promotion videos for Premium features


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPremiumState",
        }

        return await self.invoke(data, timeout=timeout)

    async def canPurchasePremium(
        self, purpose: dict, timeout: float = None
    ) -> Response:
        """Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase

        Args:
            purpose (``dict``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "canPurchasePremium",
            "purpose": purpose,
        }

        return await self.invoke(data, timeout=timeout)

    async def assignAppStoreTransaction(
        self, receipt: bytes, purpose: dict, timeout: float = None
    ) -> Response:
        """Informs server about a purchase through App Store. For official applications only

        Args:
            receipt (``bytes``):
                App Store receipt

            purpose (``dict``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "assignAppStoreTransaction",
            "receipt": receipt,
            "purpose": purpose,
        }

        return await self.invoke(data, timeout=timeout)

    async def assignGooglePlayTransaction(
        self,
        package_name: str,
        store_product_id: str,
        purchase_token: str,
        purpose: dict,
        timeout: float = None,
    ) -> Response:
        """Informs server about a purchase through Google Play. For official applications only

        Args:
            package_name (``str``):
                Application package name

            store_product_id (``str``):
                Identifier of the purchased store product

            purchase_token (``str``):
                Google Play purchase token

            purpose (``dict``):
                Transaction purpose


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "assignGooglePlayTransaction",
            "package_name": package_name,
            "store_product_id": store_product_id,
            "purchase_token": purchase_token,
            "purpose": purpose,
        }

        return await self.invoke(data, timeout=timeout)

    async def acceptTermsOfService(
        self, terms_of_service_id: str, timeout: float = None
    ) -> Response:
        """Accepts Telegram terms of services

        Args:
            terms_of_service_id (``str``):
                Terms of service identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "acceptTermsOfService",
            "terms_of_service_id": terms_of_service_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def sendCustomRequest(
        self, method: str, parameters: str, timeout: float = None
    ) -> Response:
        """Sends a custom request; for bots only

        Args:
            method (``str``):
                The method name

            parameters (``str``):
                JSON-serialized method parameters


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "sendCustomRequest",
            "method": method,
            "parameters": parameters,
        }

        return await self.invoke(data, timeout=timeout)

    async def answerCustomQuery(
        self, custom_query_id: int, data: str, timeout: float = None
    ) -> Response:
        """Answers a custom query; for bots only

        Args:
            custom_query_id (``int``):
                Identifier of a custom query

            data (``str``):
                JSON-serialized answer to the query


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "answerCustomQuery",
            "custom_query_id": custom_query_id,
            "data": data,
        }

        return await self.invoke(data, timeout=timeout)

    async def setAlarm(self, seconds: float, timeout: float = None) -> Response:
        """Succeeds after a specified amount of time has passed. Can be called before initialization

        Args:
            seconds (``float``):
                Number of seconds before the function returns


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setAlarm",
            "seconds": seconds,
        }

        return await self.invoke(data, timeout=timeout)

    async def getCountries(self, timeout: float = None) -> Response:
        """Returns information about existing countries. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCountries",
        }

        return await self.invoke(data, timeout=timeout)

    async def getCountryCode(self, timeout: float = None) -> Response:
        """Uses the current IP address to find the current country. Returns two-letter ISO 3166-1 alpha-2 country code. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getCountryCode",
        }

        return await self.invoke(data, timeout=timeout)

    async def getPhoneNumberInfo(
        self, phone_number_prefix: str, timeout: float = None
    ) -> Response:
        """Returns information about a phone number by its prefix. Can be called before authorization

        Args:
            phone_number_prefix (``str``):
                The phone number prefix


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPhoneNumberInfo",
            "phone_number_prefix": phone_number_prefix,
        }

        return await self.invoke(data, timeout=timeout)

    async def getPhoneNumberInfoSync(
        self, language_code: str, phone_number_prefix: str, timeout: float = None
    ) -> Response:
        """Returns information about a phone number by its prefix synchronously. getCountries must be called at least once after changing localization to the specified language if properly localized country information is expected. Can be called synchronously

        Args:
            language_code (``str``):
                A two-letter ISO 639-1 language code for country information localization

            phone_number_prefix (``str``):
                The phone number prefix


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getPhoneNumberInfoSync",
            "language_code": language_code,
            "phone_number_prefix": phone_number_prefix,
        }

        return await self.invoke(data, timeout=timeout)

    async def getApplicationDownloadLink(self, timeout: float = None) -> Response:
        """Returns the link for downloading official Telegram application to be used when the current user invites friends to Telegram


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getApplicationDownloadLink",
        }

        return await self.invoke(data, timeout=timeout)

    async def getDeepLinkInfo(self, link: str, timeout: float = None) -> Response:
        """Returns information about a tg:// deep link. Use "tg://need_update_for_some_feature" or "tg:some_unsupported_feature" for testing. Returns a 404 error for unknown links. Can be called before authorization

        Args:
            link (``str``):
                The link


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getDeepLinkInfo",
            "link": link,
        }

        return await self.invoke(data, timeout=timeout)

    async def getApplicationConfig(self, timeout: float = None) -> Response:
        """Returns application config, provided by the server. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getApplicationConfig",
        }

        return await self.invoke(data, timeout=timeout)

    async def saveApplicationLogEvent(
        self, type: str, chat_id: int, data: dict, timeout: float = None
    ) -> Response:
        """Saves application log event on the server. Can be called before authorization

        Args:
            type (``str``):
                Event type

            chat_id (``int``):
                Optional chat identifier, associated with the event

            data (``dict``):
                The log event data


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "saveApplicationLogEvent",
            "type": type,
            "chat_id": chat_id,
            "data": data,
        }

        return await self.invoke(data, timeout=timeout)

    async def addProxy(
        self, server: str, port: int, enable: bool, type: dict, timeout: float = None
    ) -> Response:
        """Adds a proxy server for network requests. Can be called before authorization

        Args:
            server (``str``):
                Proxy server IP address

            port (``int``):
                Proxy server port

            enable (``bool``):
                Pass true to immediately enable the proxy

            type (``dict``):
                Proxy type


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addProxy",
            "server": server,
            "port": port,
            "enable": enable,
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def editProxy(
        self,
        proxy_id: int,
        server: str,
        port: int,
        enable: bool,
        type: dict,
        timeout: float = None,
    ) -> Response:
        """Edits an existing proxy server for network requests. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier

            server (``str``):
                Proxy server IP address

            port (``int``):
                Proxy server port

            enable (``bool``):
                Pass true to immediately enable the proxy

            type (``dict``):
                Proxy type


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "editProxy",
            "proxy_id": proxy_id,
            "server": server,
            "port": port,
            "enable": enable,
            "type": type,
        }

        return await self.invoke(data, timeout=timeout)

    async def enableProxy(self, proxy_id: int, timeout: float = None) -> Response:
        """Enables a proxy. Only one proxy can be enabled at a time. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "enableProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def disableProxy(self, timeout: float = None) -> Response:
        """Disables the currently enabled proxy. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "disableProxy",
        }

        return await self.invoke(data, timeout=timeout)

    async def removeProxy(self, proxy_id: int, timeout: float = None) -> Response:
        """Removes a proxy server. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "removeProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def getProxies(self, timeout: float = None) -> Response:
        """Returns list of proxies that are currently set up. Can be called before authorization


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getProxies",
        }

        return await self.invoke(data, timeout=timeout)

    async def getProxyLink(self, proxy_id: int, timeout: float = None) -> Response:
        """Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getProxyLink",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def pingProxy(self, proxy_id: int, timeout: float = None) -> Response:
        """Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization

        Args:
            proxy_id (``int``):
                Proxy identifier. Use 0 to ping a Telegram server without a proxy


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "pingProxy",
            "proxy_id": proxy_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setLogStream(self, log_stream: dict, timeout: float = None) -> Response:
        """Sets new log stream for internal logging of TDLib. Can be called synchronously

        Args:
            log_stream (``dict``):
                New log stream


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setLogStream",
            "log_stream": log_stream,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLogStream(self, timeout: float = None) -> Response:
        """Returns information about currently used log stream for internal logging of TDLib. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLogStream",
        }

        return await self.invoke(data, timeout=timeout)

    async def setLogVerbosityLevel(
        self, new_verbosity_level: int, timeout: float = None
    ) -> Response:
        """Sets the verbosity level of the internal logging of TDLib. Can be called synchronously

        Args:
            new_verbosity_level (``int``):
                New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setLogVerbosityLevel",
            "new_verbosity_level": new_verbosity_level,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLogVerbosityLevel(self, timeout: float = None) -> Response:
        """Returns current verbosity level of the internal logging of TDLib. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLogVerbosityLevel",
        }

        return await self.invoke(data, timeout=timeout)

    async def getLogTags(self, timeout: float = None) -> Response:
        """Returns list of available TDLib internal log tags, for example, ["actor", "binlog", "connections", "notifications", "proxy"]. Can be called synchronously


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLogTags",
        }

        return await self.invoke(data, timeout=timeout)

    async def setLogTagVerbosityLevel(
        self, tag: str, new_verbosity_level: int, timeout: float = None
    ) -> Response:
        """Sets the verbosity level for a specified TDLib internal log tag. Can be called synchronously

        Args:
            tag (``str``):
                Logging tag to change verbosity level

            new_verbosity_level (``int``):
                New verbosity level; 1-1024


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setLogTagVerbosityLevel",
            "tag": tag,
            "new_verbosity_level": new_verbosity_level,
        }

        return await self.invoke(data, timeout=timeout)

    async def getLogTagVerbosityLevel(
        self, tag: str, timeout: float = None
    ) -> Response:
        """Returns current verbosity level for a specified TDLib internal log tag. Can be called synchronously

        Args:
            tag (``str``):
                Logging tag to change verbosity level


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getLogTagVerbosityLevel",
            "tag": tag,
        }

        return await self.invoke(data, timeout=timeout)

    async def addLogMessage(
        self, verbosity_level: int, text: str, timeout: float = None
    ) -> Response:
        """Adds a message to TDLib internal log. Can be called synchronously

        Args:
            verbosity_level (``int``):
                The minimum verbosity level needed for the message to be logged; 0-1023

            text (``str``):
                Text of a message to log


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "addLogMessage",
            "verbosity_level": verbosity_level,
            "text": text,
        }

        return await self.invoke(data, timeout=timeout)

    async def getUserSupportInfo(self, user_id: int, timeout: float = None) -> Response:
        """Returns support information for the given user; for Telegram support only

        Args:
            user_id (``int``):
                User identifier


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "getUserSupportInfo",
            "user_id": user_id,
        }

        return await self.invoke(data, timeout=timeout)

    async def setUserSupportInfo(
        self, user_id: int, message: dict, timeout: float = None
    ) -> Response:
        """Sets support information for the given user; for Telegram support only

        Args:
            user_id (``int``):
                User identifier

            message (``dict``):
                New information message


        Returns:
            :class:`~pytdbot.types.Response`
        """

        data = {
            "@type": "setUserSupportInfo",
            "user_id": user_id,
            "message": message,
        }

        return await self.invoke(data, timeout=timeout)
