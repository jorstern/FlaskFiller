"""empty message

Revision ID: 47b13842becd
Revises: None
Create Date: 2018-04-06 22:36:09.328052

"""

# revision identifiers, used by Alembic.
revision = '47b13842becd'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('fname', sa.String(length=128), nullable=False),
    sa.Column('lname', sa.String(length=128), nullable=False),
    sa.Column('password_digest', sa.String(length=192), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_token', sa.String(length=40), nullable=True),
    sa.Column('update_token', sa.String(length=40), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sessions_user_id'), 'sessions', ['user_id'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sessions_user_id'), table_name='sessions')
    op.drop_table('sessions')
    op.drop_table('users')
    ### end Alembic commands ###
