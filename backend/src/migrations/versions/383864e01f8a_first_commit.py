"""First commit

Revision ID: 383864e01f8a
Revises: 
Create Date: 2023-08-22 16:19:56.316206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '383864e01f8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parking',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rtsp', sa.String(length=256), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('conf', sa.Integer(), nullable=False),
    sa.Column('iou', sa.Integer(), nullable=False),
    sa.Column('circle', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rtsp')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parking')
    # ### end Alembic commands ###
