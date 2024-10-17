import click
import emoji
import random
import string

alphabet = list(string.ascii_lowercase)

emoji_list = [emoji.emojize(f':{name}:') for name in [
    'grinning_face', 'smiling_face_with_hearts', 'face_with_tears_of_joy', 
    'sunglasses', 'winking_face', 'crying_face', 'angry_face', 'thinking_face', 
    'astonished_face', 'confused_face', 'nerd_face', 'zipper_mouth_face', 
    'exploding_head', 'rolling_on_the_floor_laughing', 'hugging_face', 
    'face_with_raised_eyebrow', 'face_with_hand_over_mouth', 'grimacing_face', 
    'smiling_face_with_halo', 'shushing_face', 'smiling_face_with_sunglasses', 
    'neutral_face', 'face_with_steam_from_nose', 'money_mouth_face', 
    'star_struck', 'face_with_thermometer'
]]

random.shuffle(emoji_list)

char_to_emoji = dict(zip(alphabet, emoji_list))

emoji_to_char = {v: k for k, v in char_to_emoji.items()}

@click.group()
def cli():
    pass

@cli.command()
@click.argument('message')
def encode(message):
    encoded_message = ""
    for char in message.lower():
        if char in char_to_emoji:
            encoded_message += char_to_emoji[char]
        else:
            encoded_message += char
    click.echo(f"Encoded Message: {encoded_message}")

@cli.command()
@click.argument('message')
def decode(message):
    decoded_message = ""
    emoji_buffer = ""
    for char in message:
        emoji_buffer += char
        if emoji_buffer in emoji_to_char:
            decoded_message += emoji_to_char[emoji_buffer]
            emoji_buffer = ""
        elif emoji_buffer not in emoji_to_char and len(emoji_buffer) > 1:
            decoded_message += emoji_buffer
            emoji_buffer = ""
    click.echo(f"Decoded Message: {decoded_message}")

if __name__ == '__main__':
    cli()
