
# 在数据库迁移脚本中添加以下内容
def upgrade():
    op.add_column('place_ratings', sa.Column('id', sa.Integer(), nullable=False))
    op.create_unique_constraint('unique_user_place', 'place_ratings', ['username', 'place_id'])

def downgrade():
    op.drop_constraint('unique_user_place', 'place_ratings', type_='unique')
    op.drop_column('place_ratings', 'id')
