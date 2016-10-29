import os.path
import tensorflow as tf

# Basic model parameters as external flags.
flags = tf.app.flags
FLAGS = flags.FLAGS
flags.DEFINE_string('input_dir', 'input', 'Input Directory.')

def run_training():
  csv_file = os.path.join(FLAGS.input_dir, 'input.csv');
  filename_queue = tf.train.string_input_producer([csv_file])
  key, value = tf.TextLineReader().read(filename_queue)

  col1, col2 = tf.decode_csv(value, record_defaults=[[1], [1]])

  x = tf.placeholder("float") # Create a placeholder 'x'
  w = tf.Variable(5.0, name="weights")
  y = tf.mul(w, x)

  with tf.Session() as sess:
    # Add the variable initializer Op.
    tf.initialize_all_variables().run()

    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    for i in range(2):
      # Retrieve a single instance:
      x1, x2 = sess.run([col1, col2])
      print(sess.run(y, feed_dict={x: x1}))
      print(sess.run(y, feed_dict={x: x2}))

    coord.request_stop()
    coord.join(threads)

def main(_):
  run_training()

if __name__ == '__main__':
  tf.app.run()