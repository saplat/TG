import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from typing import Union

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False,
                      fetchrow: bool = False, execute: bool = False):
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

    async def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS Ust(
                    id SERIAL PRIMARY KEY ,
                    fname VARCHAR(255) NOT NULL,
                    id_tg BIGINT NOT NULL UNIQUE 
                );"""
        await self.execute(sql, execute=True)

    async def add_user(self, fname, id_tg, groupus):
        sql = """INSERT INTO users(fname, id_tg, groupus) VALUES ($1,$2,$3)"""

        return await self.execute(sql,fname,id_tg,groupus, fetchrow=True)

    async def add_group(self, group_name):
        sql = """INSERT INTO groupi(group_name) VALUES ($1)"""
        return await self.execute(sql, group_name, fetchrow=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def check_teacher(self,tx):
        sql = """SELECT EXISTS(SELECT 1 FROM teachers WHERE fname = tx)"""
        return sql
