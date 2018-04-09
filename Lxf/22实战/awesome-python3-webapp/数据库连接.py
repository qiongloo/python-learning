
import asyncio
import logging; logging.basicConfig(level=logging.INFO)


##连接池
import aiomysql

async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool =  await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )



#Select模块
async def select(sql, args, size=None):
    #log(sql, args)
    global __pool
    with (await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.execute(sql.repalce('?','%s'),args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            re = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs



#Insert, Update, Delete
async def execute(sql, args, autocommit=True):
    #log(sql)
    async with  __pool.acquire() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await  cur.execute(sql.repalce('?','%s'),args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return  affected




        # try:
        #     cur = await conn.cursor()
        #     await cur.execute(sql.replace('?', '%s'), args)
        #     affected = cur.rowcount
        #     await cur.close()
        # except BaseException as e:
        #     raise
        # return affected



#
# from orm import Model, StringField, IntegerField
#
# class User(Model):
#     __table__ = 'users'
#
#     id = IntegerField(primary_key=True)
#     name = StringField()



