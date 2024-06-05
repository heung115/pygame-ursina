from PIL import Image, ImageDraw, ImageFont


# 지정하는 텍스트 이미지 생성
def create_text_texture(text, size, font_size=50):
    # 투명 배경 이미지 생성
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    # 텍스트 바운딩 박스 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    position = ((size - text_width) / 2, (size - text_height) / 2)

    # 이미지에 텍스트를 그림
    draw.text(position, text, font=font, fill=(255, 255, 255, 255))

    return image
