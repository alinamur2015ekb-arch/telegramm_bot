from hendlers import router
from aiogram import F
from aiogram.types import Message
from start import Bot

@router.message(F.photo)
async def photo(message: Message):
    photo = message.photo[-1]
    file_id = photo.file_id


    await message.answer(
        f"Вы отправиль фото \n ID photo: <code>{file_id}</code>",
        parse_mode  = "HTML"
    )
    await message.answer_photo(file_id, caption="Ваше фото")


@router.message(F.video)
async def video(message: Message):
    video = message.video
    file_id = video.file_id
    duration = video.duration


    await message.answer(
        f"Вы отправиль видео \n ID video: <code>{file_id}</code>\n Видео идет <code>{duration}</code> секунд",
        parse_mode  = "HTML"
    )
    await message.answer_video(file_id, caption="Ваше видео")


@router.message(F.animation)
async def animation(message: Message):
    animation = message.animation
    

    await message.answer(
        f"Вы отправиль анимацию",
        parse_mode  = "HTML"
    )
    await message.answer_animation(animation.file_id, caption="Ваша анимация")


@router.message(F.document)
async def document(message: Message, bot: Bot):
    document = message.document
    file_id = document.file_id

    file = await bot.get_file(file_id)
    file_path = file.file_path

    local_path = f'downoloads/{document.file_name}'

    await bot.download_file(file_path=file_path, destination=local_path)

    await message.answer("Файл сохранен")
