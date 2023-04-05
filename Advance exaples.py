def logger(message):
    def logger_message():
        print(f"{message} srinu")
    return logger_message()


message = logger("Hello")

def html_tag(tag):
    def html_wrap(message):
        print(f"<{tag}>{message}<\\{tag}>")
    return html_wrap


print_h1 = html_tag("h1")
print_h1("Hello World")
print_h1("this is me")

print_p1 = html_tag("p1")
print_p1("this is a new paragraph")

