from models.section import Section
from infra.repository.section_repository import SectionRepository

def exec(input):

    section = Section(
        id=input.id,
        title=input.title,
        topics=input.topics
    )

    print(section)

    section_repository = SectionRepository()
    section_repository.update(section)