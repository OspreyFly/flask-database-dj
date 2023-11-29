from models import Playlist, Song, PlaylistSong, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    s1 = Song(title="Jump Around", artist="FrE-FlO")
    s2 = Song(title="Somewhere", artist="Bradley Nyugen")
    s3 = Song(title="How about that", artist="Outbreak")

    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)

    db.session.commit()

    p1 = Playlist(name="Rock & Roll", description="Are you ready to rock?")
    p2 = Playlist(name="Classics", description="Less lip flapping; More substance.")
    p3 = Playlist(
        name="Relaxation Ambience",
        description="Relax while listening to sounds of nature.",
    )

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)

    db.session.commit()
