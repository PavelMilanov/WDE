"""init db

Revision ID: c73fcaab58e2
Revises: 
Create Date: 2023-01-02 22:05:29.822137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c73fcaab58e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('login'),
    sa.UniqueConstraint('password')
    )
    op.create_table('templates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    op.create_table('tokens',
    sa.Column('registration_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=True),
    sa.Column('expire_of', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['registration_id'], ['registrations.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('registration_id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('second_name', sa.String(length=20), nullable=True),
    sa.Column('surname', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['registrations.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('tokens')
    op.drop_table('templates')
    op.drop_table('registrations')
    # ### end Alembic commands ###
