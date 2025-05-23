"""
+-------------------+      +-------------------+
| <<abstract>>      |      | <<abstract>>      |
| Notification      |<-----| NotificationSender|
+-------------------+      +-------------------+
| - recipient       |      | + send()          |
| + send() (abstract)|      +-------------------+
+-------------------+                ^
          ^                          |
          |                          |
+-------------------+      +-------------------+
| EmailNotification |      | EmailSender       |
+-------------------+      +-------------------+
| - subject         |      | + send(email_notif)|
| - body            |      +-------------------+
| + send()          |                ^
+-------------------+                |
          ^                          |
          |                          |
+-------------------+      +-------------------+
| SMSNotification   |      | SMSSender         |
+-------------------+      +-------------------+
| - message         |      | + send(sms_notif) |
+-------------------+      +-------------------+
          ^                          ^
          |                          |
+-------------------+      +-------------------+
| PushNotification  |      | PushSender        |
+-------------------+      +-------------------+
| - title           |      | + send(push_notif)|
| - body            |      +-------------------+
+-------------------+
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract base class for all notification types.
    Defines common properties and an abstract 'send' method.
    """

    def __init__(self, recipient: str):
        if not recipient:
            raise ValueError("Recipient cannot be empty.")
        self.recipient = recipient

    @abstractmethod
    def get_details(self) -> dict:
        """
        Returns a dictionary of notification-specific details.
        """
        pass

    def __str__(self):
        return f"Notification to: {self.recipient}"


# 2. Concrete Notification Classes
class EmailNotification(Notification):
    """
    Represents an email notification.
    """

    def __init__(self, recipient: str, subject: str, body: str):
        super().__init__(recipient)
        if not subject:
            raise ValueError("Email subject cannot be empty.")
        if not body:
            raise ValueError("Email body cannot be empty.")
        self.subject = subject
        self.body = body

    def get_details(self) -> dict:
        return {"subject": self.subject, "body": self.body}

    def __str__(self):
        return (
            f"Email to: {self.recipient}, Subject: {self.subject},"
            f" Body: {self.body[:50]}..."
        )


class SMSNotification(Notification):
    """
    Represents an SMS notification.
    """

    def __init__(self, recipient: str, message: str):
        super().__init__(recipient)
        if not message:
            raise ValueError("SMS message cannot be empty.")
        self.message = message

    def get_details(self) -> dict:
        return {"message": self.message}

    def __str__(self):
        return (
            f"SMS to: {self.recipient}, Message (excerpt):"
            f" {self.message[:50]}..."
        )


class PushNotification(Notification):
    """
    Represents a push notification.
    """

    def __init__(self, recipient: str, title: str, body: str):
        super().__init__(recipient)
        if not title:
            raise ValueError("Push notification title cannot be empty.")
        if not body:
            raise ValueError("Push notification body cannot be empty.")
        self.title = title
        self.body = body

    def get_details(self) -> dict:
        return {"title": self.title, "body": self.body}

    def __str__(self):
        return (
            f"Push Notification to: {self.recipient}, Title: {self.title},"
            f" Body (excerpt): {self.body[:50]}..."
        )


# 3. Sending Mechanism (Strategy Pattern)
class NotificationSender(ABC):
    """
    Abstract base class for all notification senders.
    """

    @abstractmethod
    def send(self, notification: Notification):
        """
        Abstract method to send a notification.
        """
        pass


class EmailSender(NotificationSender):
    """
    Concrete sender for email notifications.
    """

    def send(self, notification: EmailNotification):
        if not isinstance(notification, EmailNotification):
            raise TypeError("Expected an EmailNotification object.")
        print(
            f"Sending Email to {notification.recipient}:"
            f" Subject='{notification.subject}', Body='{notification.body}'"
        )
        # In a real system, this would integrate with an email sending library e.g., smtplib, a third-party email API.


class SMSSender(NotificationSender):
    """
    Concrete sender for SMS notifications.
    """

    def send(self, notification: SMSNotification):
        if not isinstance(notification, SMSNotification):
            raise TypeError("Expected an SMSNotification object.")
        print(
            f"Sending SMS to {notification.recipient}:"
            f" Message='{notification.message}'"
        )
        # In a real system, this would integrate with an SMS gateway API e.g., Twilio, Nexmo.


class PushSender(NotificationSender):
    """
    Concrete sender for push notifications.
    """

    def send(self, notification: PushNotification):
        if not isinstance(notification, PushNotification):
            raise TypeError("Expected a PushNotification object.")
        print(
            f"Sending Push Notification to {notification.recipient}:"
            f" Title='{notification.title}', Body='{notification.body}'"
        )
        # In a real system, this would integrate with a push notification service e.g., Firebase Cloud Messaging (FCM), Apple Push Notification service (APNS).


# 4. Unified Sending Interface
class NotificationService:
    """
    Provides a unified interface for sending different types of notifications.
    Uses a dictionary to map notification types to their respective senders.
    """

    def __init__(self):
        self._senders = {
            EmailNotification: EmailSender(),
            SMSNotification: SMSSender(),
            PushNotification: PushSender(),
        }

    def register_sender(self, notification_type: type, sender: NotificationSender):
        """Allows dynamic registration of new notification types and their senders."""
        if not issubclass(notification_type, Notification):
            raise TypeError("notification_type must be a subclass of Notification.")
        if not isinstance(sender, NotificationSender):
            raise TypeError("sender must be an instance of NotificationSender.")
        self._senders[notification_type] = sender
        print(
            f"Registered sender for {notification_type.__name__}:"
            f" {sender.__class__.__name__}"
        )

    def send_notification(self, notification: Notification):
        """
        Sends a notification through the appropriate sender.
        """
        sender_class = type(notification)
        sender = self._senders.get(sender_class)

        if sender:
            sender.send(notification)
        else:
            raise ValueError(
                f"No sender registered for notification type:"
                f" {sender_class.__name__}"
            )


if __name__ == "__main__":
    notification_service = NotificationService()

    email_notif = EmailNotification(
        "user@example.com",
        "Welcome to Our Service!",
        "Thank you for signing up. We hope you enjoy your experience.",
    )
    sms_notif = SMSNotification(
        "+1234567890",
        "Your order #12345 has been shipped and will arrive in 2-3 business days.",
    )
    push_notif = PushNotification(
        "device_token_abc",
        "New Message!",
        "You have a new message from John Doe.",
    )

    print("--- Sending Notifications ---")
    notification_service.send_notification(email_notif)
    notification_service.send_notification(sms_notif)
    notification_service.send_notification(push_notif)

    print("\n--- Adding a New Notification Type (Future Extensibility) ---")

    class InAppNotification(Notification):
        def __init__(self, recipient: str, message: str, action_url: str = None):
            super().__init__(recipient)
            self.message = message
            self.action_url = action_url

        def get_details(self) -> dict:
            return {"message": self.message, "action_url": self.action_url}

        def __str__(self):
            return (
                f"In-App Notification to: {self.recipient}, Message:"
                f" {self.message[:50]}..."
            )

    class InAppSender(NotificationSender):
        def send(self, notification: InAppNotification):
            if not isinstance(notification, InAppNotification):
                raise TypeError("Expected an InAppNotification object.")
            print(
                f"Displaying In-App Notification for {notification.recipient}:"
                f" Message='{notification.message}', Action URL:"
                f" '{notification.action_url}'"
            )
            # This would typically involve sending a message to a WebSocket,
            # or updating a database for the user's next login to display
            # in-app.

    # Register the new notification type and its sender
    notification_service.register_sender(InAppNotification, InAppSender())

    inapp_notif = InAppNotification(
        "user_id_123",
        "A new product is available!",
        "https://example.com/new-product",
    )

    print("\n--- Sending the new In-App Notification ---")
    notification_service.send_notification(inapp_notif)

    # Example of handling a missing sender
    print("\n--- Attempting to send an unregistered type ---")
    try:
        class UnregisteredNotification(Notification):
            def __init__(self, recipient: str, data: str):
                super().__init__(recipient)
                self.data = data
            def get_details(self) -> dict:
                return {"data": self.data}
        unregistered_notif = UnregisteredNotification("test_user", "some data")
        notification_service.send_notification(unregistered_notif)
    except ValueError as e:
        print(f"Error: {e}")

    # Example of invalid sender registration
    print("\n--- Attempting to register an invalid sender ---")
    try:
        class InvalidSender: # Not inheriting from NotificationSender
            def send(self, notif):
                pass
        notification_service.register_sender(EmailNotification, InvalidSender())
    except TypeError as e:
        print(f"Error during registration: {e}")