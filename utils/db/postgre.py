import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from typing import Union

from data import config


class Database:
    def __init__(self):
        self.pool: Pool = Pool

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += 'AND'.join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)
        ])

        return sql, tuple(parameters.values())

    async def add_user(self, fname, id_tg, groupus):
        sql = """INSERT INTO users(fname, id_tg, groupus) VALUES ($1,$2,$3)"""

        return await self.execute(sql,fname,id_tg,groupus, fetchrow=True)

    async def add_pas(self,id_tg):
        sql = """INSERT INTO pasusers(id_tg) VALUES ($1)"""
        return await self.execute(sql,id_tg, fetchrow=True)

    async def check_teacher(self,fname):
        sql = """SELECT * FROM teachers WHERE fname = ($1)"""
        return await self.execute(sql,fname, execute=True)

    async def delete_users(self,id_tg):
        sql = """DELETE FROM users WHERE id_tg = ($1) """
        await self.execute(sql, id_tg, execute=True)

    async def select_shedules(self, group_user, dayi, updown):
        sql = """SELECT schedule FROM schedules WHERE (group_user = ($1) AND dayi = ($2) AND updown = ($3));"""
        return await self.execute(sql, group_user, dayi,updown,fetchval=True)

    async def select_group(self,id_tg):
        sql = """SELECT groupus FROM users WHERE (id_tg = ($1))"""
        return await self.execute(sql, id_tg, fetchval=True)

    async def select_pas(self):
        sql = "SELECT  id_tg FROM pasusers"
        return await self.execute(sql,fetch=True)

    async def count_userspas(self):
        sql = "SELECT COUNT(*) FROM pasusers"
        return await self.execute(sql, fetchval=True)

    async def select_shedules_th(self, fname, dayi, updown):
        sql = """SELECT schedule FROM teachers WHERE (fname = ($1) AND dayi = ($2) AND updown = ($3))"""
        return await self.execute(sql, fname, dayi, updown, fetchval=True)

