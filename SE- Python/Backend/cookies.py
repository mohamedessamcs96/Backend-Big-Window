from http.cookies import SimpleCookie, CookieError

out_cookie = SimpleCookie()
out_cookie["bearname"] = "Smokey Bear"
out_cookie["bearname"]["max-age"] = 600
out_cookie["bearname"]["httponly"] = True


#self.send_header("Set-Cookie", out_cookie["bearname"].OutputString())

print(out_cookie["bearname"]['max-age'])

#in_cookie = SimpleCookie(self.headers["Cookie"])
#in_data = in_cookie["bearname"].value