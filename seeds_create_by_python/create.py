import random

path = 'seed.txt'

msg_header  = "Book.create!(\n"
msg_header += "  [\n"
msg_body    = ""
msg_footer  = "  ]\n"
msg_footer += ")"

with open(path, mode='w') as f:
    for idx in range(10):
        name    = "テストユーザー"
        code_id = int( random.uniform(1.0, 50000.0) )

        msg_body += "    {\n"
        msg_body += "      name: '{}_{}',\n".format(name, idx)
        msg_body += "      code_id: {}\n".format(code_id)
        msg_body += "    },\n"

    msg = msg_header + msg_body + msg_footer
    f.write(msg)
