import os.path
import tensorflow as tf

# Basic model parameters as external flags.
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('output_dir', 'output', 'Output Directory.')


def run_training():
    x = tf.placeholder("float") # Create a placeholder 'x'
    w = tf.Variable(5.0, name="weights")
    y = tf.mul(w, x)

    with tf.Session() as sess:
        # Add the variable initializer Op.
        tf.initialize_all_variables().run()

        print(sess.run(y, feed_dict={x: 1.0}))
        print(sess.run(y, feed_dict={x: 2.0}))

        # Create a saver for writing training checkpoints.
        saver = tf.train.Saver()
        checkpoint_file = os.path.join(FLAGS.output_dir, 'checkpoint')
        saver.save(sess, checkpoint_file, global_step=0)


def main(_):
    run_training()

if __name__ == '__main__':
    tf.app.run()