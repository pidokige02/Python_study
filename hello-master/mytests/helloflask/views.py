from flask import render_template, request, Response, session, jsonify, make_response, redirect, flash
from datetime import datetime, date
from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from helloflask import app
from helloflask.classes import FormInput
from helloflask.init_db import db_session
from helloflask.models import User, Song, Album, Artist, SongArtist, SongRank


def songlist(dt):
    sr = SongRank.query.filter_by(rankdt=dt).options(joinedload(SongRank.song))
    sr = sr.options(joinedload(SongRank.song, Song.album))
    sr = sr.options(joinedload(SongRank.song, Song.songartists))
    sr = sr.filter("atype=0")
    return sr


@app.route('/')
def idx():
    lives = songlist('2019-01-29')
    todays = songlist('2019-01-28')
    return render_template("app.html", lives=lives, todays=todays)


@app.route('/regist', methods=['GET'])
def regist():
    return render_template("regist.html")


@app.route('/regist', methods=['POST'])
def regist_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')
    nickname = request.form.get('nickname')

    if passwd != passwd2:
        flash("암호를 정확히 입력하세요!!")
        return render_template("regist.html", email=email, nickname=nickname)
    else:
        u = User(email, passwd, nickname, True)
        try:
            db_session.add(u)
            db_session.commit()

        except:
            db_session.rollback()

        flash("%s 님, 가입을 환영합니다!" % nickname)
        return redirect("/login")


@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')
    u = User.query.filter('email = :email and passwd = sha2(:passwd, 256)').params(
        email=email, passwd=passwd).first()
    if u is not None:
        session['loginUser'] = {'useid': u.id, 'name': u.nickname}
        return redirect('/')
    else:
        flash("해당 사용자가 없습니다!!")
        return render_template("login.html", email=email)


@app.route('/logout')
def logout():
    if session.get('loginUser'):
        del session['loginUser']

    return redirect('/')


@app.route('/songinfo/<songno>')
def songinfo(songno):
    # song = SongArtist.query.filter_by(songno = songno).first()
    song = Song.query.filter_by(songno = songno).first()

    return render_template("songinfo.html", likecnt=song.likecnt)
    # s = SongArtist.query.filter_by(songno=songno).order_by(SongArtist.atype).options(joinedload(SongArtist.artist)).all()
    # ll = [ss.json() for ss in s]
    # print("ssssssssssSS>>", s)
    # return make_response(jsonify(ll))


@app.route('/ajax1')
def ajax1(songno):
    aaa = { "id": 1, "name": 'aaaaa'}
    return aaa