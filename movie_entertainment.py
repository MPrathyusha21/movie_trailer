import moviemedia

import fresh_tomatoes
GeethaGovindam=moviemedia.Movies("GeethaGovindam","Romantic comedy",
                                                                         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYrS5uFWGFvPAJ9u9X9M_DB0swfl5NHGL6igOu5XIW0N6u_WdyZg",
                                                                         "https://youtu.be/Ct4_0Jg3xGA")
Kali=moviemedia.Movies("Kali","Thriller/Action",
                                                "https://upload.wikimedia.org/wikipedia/en/thumb/0/0b/"
                                                 "Kali_Malayalam_Movie_First_Look_Poster.jpg/220px-Kali_Malayalam_Movie_First_Look_Poster.jpg",
                                                 "https://youtu.be/vJ72PkYYZHs")
Yehjawaanihaideewani=moviemedia.Movies("Yeh jawaani hai deewani","Romantic drama",
                                                                                     "https://i.pinimg.com/originals/34/5f/ec/345fecf5e269212d9a287508648ec173.jpg",
                                                                                     "https://youtu.be/Rbp2XUSeUNE")
Dumbo=moviemedia.Movies("Dumbo"," Fantasy/Animation",
                                                        "https://lumiere-a.akamaihd.net/v1/images/teaser-"
                                                        "richbanner_c05787a8.jpeg?region=0%2C0%2C1600%2C900",
                                                        "https://youtu.be/mgcrMHAezS0")
Kirikparty=moviemedia.Movies("Kirikparty"," Drama/Comedy",
                                                             "https://i0.wp.com/fnn.9db.myftpupload.com/wp-content/uploads/2017/08/"
                                                             "Kirik-Party-Kannada-poster-Samyukta-Hegde-e1502170885309.jpg?resize=484%2C369",
                                                             "https://youtu.be/IfvnbER_6sQ")
Premam=moviemedia.Movies("Premam","Drama/Romance",
                                                        "http://www.bhavanidvd.com/images/premam-dvd-m.jpg",
                                                            "https://youtu.be/NLu1kgfEfpo")
movies=[GeethaGovindam,Kali,Yehjawaanihaideewani,Dumbo,Kirikparty,Premam]
fresh_tomatoes.open_movies_page(movies)
