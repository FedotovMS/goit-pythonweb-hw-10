from sqlalchemy.ext.asyncio import AsyncSession
from src.entity.models import Contact
from src.repository.contacts import ContactRepository
from src.schemas.contacts import ContactCreate
from src.schemas.users import UserResponse


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def search_contacts(self, query: str, user: UserResponse):
        return await self.repository.search_contacts(query, user)

    async def create_contact(self, contact_data: ContactCreate, user: UserResponse):
        new_contact = Contact(**contact_data.model_dump(), user_id=user.id)
        return await self.repository.create(new_contact)

    async def get_contacts(self, user: UserResponse):
        return await self.repository.get_all(user)

    async def get_contact(self, contact_id: int, user: UserResponse):
        return await self.repository.get_by_id(contact_id, user)

    async def update_contact(
        self, contact_id: int, updated_data: ContactCreate, user: UserResponse
    ):
        return await self.repository.update(contact_id, updated_data, user)

    async def delete_contact(self, contact_id: int, user: UserResponse):
        return await self.repository.delete(contact_id, user)

    async def get_upcoming_birthdays(self, user: UserResponse):
        return await self.repository.get_upcoming_birthdays(user)
